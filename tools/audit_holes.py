#!/usr/bin/env python3
"""audit_holes.py - clearance audit for the 4 M3 mount holes.

Reads the real lume-coaster.kicad_pcb and, for every footprint, builds a
plan bounding box from its drawing entities (F.Fab + F.SilkS). Then checks
each hole against every footprint whose bbox comes within the screw-head
keepout radius.

The board is mounted component-side toward the OPEN BACK in Fork A, so M3
screw HEADS sit on the component side. Southampton rule: anything closer
than head_radius + margin is flagged.
"""

import math
import re
import sys
from pathlib import Path

HOLES = [(4, 4), (81, 4), (4, 36), (81, 36)]
HEAD_R = 2.75        # M3 SHCS head radius
MARGIN_FAB = 1.0     # clearance to part bodies
CHECK_R = HEAD_R + MARGIN_FAB

PCB = Path(r"C:\Projects\HalfLife-Deskbuddy\carrier-board\lume-coaster\lume-coaster.kicad_pcb")

FP_SPLIT = re.compile(r'\n\s*\(footprint "')
AT_RE = re.compile(r'\(at\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s+(-?[\d.]+))?\)')
REF_RE = re.compile(r'\(property "Reference" "([^"]+)"')
VAL_RE = re.compile(r'\(property "Value" "([^"]+)"')
LINE_RE = re.compile(
    r'\(start\s+(-?[\d.]+)\s+(-?[\d.]+)\)\s*\n?\s*\(end\s+(-?[\d.]+)\s+(-?[\d.]+)',
    re.DOTALL,
)
# KiCad pads also carry geometry worth seeing.
PAD_RE = re.compile(
    r'\(pad "[^"]+"\s+[a-z_]+\s+\S+\s*\(at\s+(-?[\d.]+)\s+(-?[\d.]+)'
)


def footprints(txt):
    """Yield (ref, value, x, y, rot, bbox) for each footprint block."""
    starts = [m.start() for m in re.finditer(r'\(footprint "', txt)]
    if not starts:
        return
    for i in range(len(starts)):
        head = txt[starts[i]:starts[i + 1]] if i + 1 < len(starts) else txt[starts[i]:]
        # a footprint block closes at the line that returns to the
        # outer "(footprint" nesting depth -- stop at the first
        #  )\n	) sequence following the last property/pad entity.
        # Simpler + robust: cut at the first '\n\t)\n' that appears AFTER
        # the (at ...) line and is followed by a non-indented entity.
        ref = REF_RE.search(head)
        val = VAL_RE.search(head)
        at = AT_RE.search(head[:2500])
        if not (ref and at):
            continue
        x, y = float(at.group(1)), float(at.group(2))
        rot = float(at.group(3) or 0)
        # local bbox from every drawn line + every pad, but only within
        # this footprint's own block (stop at the closing paren balanced
        # to the '(footprint' token).
        depth = 0
        endpos = len(head)
        inblk = False
        for ci, ch in enumerate(head):
            if ch == "(":
                depth += 1
                inblk = True
            elif ch == ")":
                depth -= 1
                if inblk and depth == 0:
                    endpos = ci + 1
                    break
        head = head[:endpos]
        xs, ys = [], []
        for a, b, c, d in LINE_RE.findall(head):
            xs += [float(a), float(c)]
            ys += [float(b), float(d)]
        for a, b in PAD_RE.findall(head):
            xs += [float(a)]
            ys += [float(b)]
        if not xs:
            continue
        r = math.radians(rot)
        corners = []
        for lx, ly in [(min(xs), min(ys)), (max(xs), max(ys)),
                       (min(xs), max(ys)), (max(xs), min(ys))]:
            wx = x + lx * math.cos(r) - ly * math.sin(r)
            wy = y + lx * math.sin(r) + ly * math.cos(r)
            corners.append((wx, wy))
        bx = [c[0] for c in corners]
        by = [c[1] for c in corners]
        yield (ref.group(1), val.group(1), x, y, rot,
               (min(bx), max(bx), min(by), max(by)))


def main():
    if not PCB.exists():
        print(f"audit: PCB not found: {PCB}")
        return 2
    txt = PCB.read_text(encoding="utf-8", errors="replace")
    fps = list(footprints(txt))
    print(f"PCB: {PCB.name}")
    print(f"footprints parsed: {len(fps)}   (entities checked: F.Fab + F.SilkS)")
    print()

    rc = 0
    for hx, hy in HOLES:
        print(f"-- H at ({hx},{hy})  keepout circle R={CHECK_R:.2f}")
        hits = []
        for ref, val, x, y, rot, bbox in fps:
            if ref == f"H" or "MountingHole" in (val or ""):
                continue
            x0, x1, y0, y1 = bbox
            # nearest point on bbox to the hole centre
            nx = max(x0, min(hx, x1))
            ny = max(y0, min(hy, y1))
            d = math.dist((hx, hy), (nx, ny))
            if d <= CHECK_R:
                # component height class from the value/ref
                tall = ref.upper().startswith(("J", "Q", "C_DISP", "SW", "BT"))
                hits.append((d, ref, val, (x0, x1, y0, y1), tall))
        if not hits:
            print("     clear")
        else:
            for d, ref, val, bb, tall in sorted(hits):
                tag = "TALL-CHECK" if tall else "traces"
                print(f"     [{tag}] {ref:9} {val:18} bbox=({bb[0]:.1f},{bb[1]:.1f})x({bb[2]:.1f},{bb[3]:.1f})  gap={d:.2f}")
                if tall and d < HEAD_R:
                    rc = 1
    print()
    print("RESULT: " + ("HEAD COLLISION" if rc == 1 else "no tall part sits under a screw head"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
