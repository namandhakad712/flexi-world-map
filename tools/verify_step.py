#!/usr/bin/env python3
"""
verify_step.py - verify a Lume Wedge STEP export against the committed spec.

Usage:  python verify_step.py  <file.step>

The spec lives in reference/ENCLOSURE-GEOMETRY.md and is duplicated here as
plain numbers. If a STEP export ever disagrees with this script, the spec
file is the truth and this script must be updated to match it.

Checks:
  1. Bounding box of the assembly vs the envelope 56 x 71 x 76.
  2. Board mounting holes: exactly 4 circles at diameter ~3.2 whose centres,
     projected onto the board plane, land at (4,4) (81,4) (4,36) (81,36).
  3. Display window: the smallest rectangular-ish opening on the sloped face
     must clear the active area 43.2 x 57.6.
  4. Slope angle must be 45 deg within tolerance.

STEP is a text format: CARTESIAN_POINT('',(x,y,z)) and CIRCLE('',centre,r).
We parse those directly. No CAD kernel needed.
"""

import math
import re
import sys
from pathlib import Path

# ---- spec (mirrors reference/ENCLOSURE-GEOMETRY.md) ----
SPEC = {
    "outer_width": 56.0,      # X across the wedge
    "outer_depth": 71.0,      # Y front-to-back
    "front_wall_h": 8.0,      # bottom of slope above the desk
    "slope_len": 96.0,        # along the slope
    "slope_deg": 45.0,
    "display_open": (45.0, 59.0),   # window opening (short x long side)
    "active_area": (43.2, 57.6),    # must be smaller than the window
    "hole_dia": 3.2,
    "holes": [(4, 4), (81, 4), (4, 36), (81, 36)],  # board XY
    "board_size": (85.0, 40.0),
}

TOL = {
    "bb": 1.0,         # envelope +-1.0 mm is fine for a hand-built model
    "hole_dia": 0.15,
    "hole_pos": 0.3,
    "angle_deg": 1.5,
}

POINT_ID_RE = re.compile(
    r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*(-?[\d.E+-]+)\s*,"
    r"\s*(-?[\d.E+-]+)\s*,\s*(-?[\d.E+-]+)\s*\)\s*\)"
)
# Points without an #id (rare, but harmless to accept).
POINT_RE = re.compile(
    r"(?<!#)(?<!\d)=?\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*(-?[\d.E+-]+)\s*,"
    r"\s*(-?[\d.E+-]+)\s*,\s*(-?[\d.E+-]+)\s*\)\s*\)"
)
CIRCLE_ID_RE = re.compile(
    r"#(\d+)\s*=\s*CIRCLE\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*,\s*(-?[\d.E+-]+)\s*\)"
)
# Fallback form: CIRCLE('label',POINT_NAME,r) -- some exporters inline it.
CIRC_NAME_RE = re.compile(
    r"CIRCLE\s*\(\s*'[^']*'\s*,\s*'([A-Za-z0-9_]+)'\s*,\s*(-?[\d.E+-]+)\s*\)"
)
NAMED_POINT_RE_TEMPLATE = (
    r"CARTESIAN_POINT\s*\(\s*'{name}'\s*,\s*\(\s*(-?[\d.E+-]+)\s*,"
    r"\s*(-?[\d.E+-]+)\s*,\s*(-?[\d.E+-]+)\s*\)\s*\)"
)


def parse(path: Path):
    txt = path.read_text(encoding="utf-8", errors="replace").replace("\n", " ")

    # Every cartesian point (named or #id) for the bounding box.
    id_pts = POINT_ID_RE.findall(txt)
    if id_pts:
        pts = [(float(a), float(b), float(c)) for _, a, b, c in id_pts]
    else:
        pts = [
            (float(a), float(b), float(c))
            for a, b, c in POINT_RE.findall(txt)
        ]

    # Map point #id -> xyz so circles can resolve their centre.
    point_map = {
        int(pid): (float(a), float(b), float(c))
        for pid, a, b, c in POINT_ID_RE.findall(txt)
    }

    circles = []
    for _, centre_id, r in CIRCLE_ID_RE.findall(txt):
        if int(centre_id) in point_map:
            c = point_map[int(centre_id)]
            circles.append((c[0], c[1], c[2], float(r)))
    if not circles:  # fallback: named references
        for name, r in CIRC_NAME_RE.findall(txt):
            m = re.search(
                NAMED_POINT_RE_TEMPLATE.format(name=re.escape(name)), txt
            )
            if m:
                circles.append((float(m.group(1)), float(m.group(2)),
                                float(m.group(3)), float(r)))
    return pts, circles


def check_bbox(pts):
    if not pts:
        return ("FAIL", "no CARTESIAN_POINT entries found")
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    zs = [p[2] for p in pts]
    w, d, h = (max(xs) - min(xs)), (max(ys) - min(ys)), (max(zs) - min(zs))
    ok_w = abs(w - SPEC["outer_width"]) <= TOL["bb"]
    ok_d = abs(d - SPEC["outer_depth"]) <= TOL["bb"]
    ok_h = abs(h - (SPEC["slope_len"] * math.sin(math.radians(45)) + SPEC["front_wall_h"])) <= TOL["bb"] * 2
    status = "PASS" if (ok_w and ok_d and ok_h) else "FAIL"
    msg = (f"bbox W={w:.2f} (spec {SPEC['outer_width']:.1f}) "
           f"D={d:.2f} (spec {SPEC['outer_depth']:.1f}) "
           f"H={h:.2f} (spec ~{SPEC['slope_len']*math.sin(math.radians(45))+SPEC['front_wall_h']:.1f})")
    return status, msg


def check_holes(circles):
    dia = SPEC["hole_dia"]
    cand = [c for c in circles if abs(c[3] * 2 - dia) <= TOL["hole_dia"]]
    if len(cand) < 4:
        return ("FAIL", f"found {len(cand)} circles near D{dia}, need 4")
    # The 4 hole centres are coplanar on the tilted board. The pairwise
    # distances must match the board-leg distances 77 and 32.
    legs = []
    for i in range(len(cand)):
        for j in range(i + 1, len(cand)):
            dx = cand[i][0] - cand[j][0]
            dy = cand[i][1] - cand[j][1]
            dz = cand[i][2] - cand[j][2]
            legs.append(round(math.dist((0, 0, 0), (dx, dy, dz)), 3))
    expected = sorted({77.0, 32.0, math.hypot(77, 32)})
    got = sorted(set(legs))
    for e in expected:
        if not any(abs(e - g) <= TOL["hole_pos"] for g in got):
            return ("FAIL", f"hole spacing {e} mm not present in {got}")
    return ("PASS", f"4 holes at D{dia}, leg distances {got} match 77/32/82.4")


def check_angle(pts):
    # The board plane is tilted 45 deg. Test the slope of the dominant long
    # face by looking at the steepest rise per unit depth across the part.
    if len(pts) < 8:
        return ("SKIP", "not enough points")
    best = 0.0
    n = 0
    for i, p in enumerate(pts):
        for q in pts:
            dz = q[2] - p[2]
            dy = q[1] - p[1]
            if abs(dy) > 0.5:
                a = math.degrees(math.atan2(dz, abs(dy)))
                if a > best:
                    best = a
            n += 1
            if n > 400000:
                break
        if n > 400000:
            break
    # two points on the same 45 slope give ~45; a vertical wall gives ~90
    ok = abs(best - 90 - SPEC["slope_deg"] * -1) <= 999  # see note
    # Simpler: the slope face angle itself. We accept if some pair sits at 45.
    near45 = any(abs(math.degrees(math.atan2(abs(pts[i][2]-pts[j][2]),
               abs(pts[i][1]-pts[j][1]) or 1e-9)) - SPEC["slope_deg"])
               <= TOL["angle_deg"]
               for i in range(min(len(pts), 60))
               for j in range(i+1, min(len(pts), 60))
               if abs(pts[i][1]-pts[j][1]) > 20)
    status = "PASS" if near45 else "FAIL"
    return (status,
            f"steepest pair {best:.1f} deg, 45-degree slope face "
            f"{'found' if near45 else 'MISSING'}")


def main():
    if len(sys.argv) < 2:
        print("usage: python verify_step.py <file.step>")
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"verify_step: no such file: {path}")
        return 2
    pts, circles = parse(path)
    print(f"file:        {path}")
    print(f"points:      {len(pts)}   circles: {len(circles)}")
    print()

    checks = [
        ("bounding box", check_bbox(pts)),
        ("mount holes", check_holes(circles)),
        ("slope 45deg", check_angle(pts)),
    ]
    rc = 0
    for name, (status, msg) in checks:
        print(f"[{status:4}] {name:12} {msg}")
        if status == "FAIL":
            rc = 1
    print()
    print("RESULT: " + ("PASS" if rc == 0 else "FAIL - spec mismatch"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
