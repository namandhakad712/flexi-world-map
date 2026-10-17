#!/usr/bin/env python3
"""check_pocket.py - does the stepped pocket fit inside the wedge?

CORRECTED MODEL. The geometry doc originally drew a closed-back wedge with a
pocket cut into the slope. That is geometrically impossible: the module zone
needs 26.6 mm of perpendicular depth and only 22.75 mm exists between the
slope face and a 71 mm-deep back wall.

The right model (and the one the reference stand uses) is an OPEN-REAR shell:
the wedge is a hollow shell with a floor, two side walls, a front wall and a
sloped face; the pocket cut opens at the rear, and the separate REAR COVER
closes it. Nothing needs to fit "behind" the module -- the module faces open
air, which is exactly what the antenna wants anyway.

This verifies the real constraint: the pocket floor, which lies parallel to
the slope at depth p, must stay above the outer bottom (z=0) with at least
the minimum wall thickness, at every slope station of every zone.

    zone          slope span   depth p (mm)
    display only   s  4.. 6     3.0
    board + panel  s  6..21.8   12.6   (panel 3 + gap 8 + board 1.6)
    module zone    s 21.8..75.2 26.6   (+ module envelope 10.6 + slack)
    board top      s 75.2..91   12.6
"""

import math

C45 = math.sqrt(2) / 2
FRONT_WALL = 8.0
WALL_MIN = 2.0

ZONES = [
    ("display lip", 4.0, 6.0, 3.0),
    ("board+panel", 6.0, 21.8, 12.6),
    ("module", 21.8, 75.2, 26.6),
    ("board top", 75.2, 91.0, 12.6),
]


def slope_z(s):
    return FRONT_WALL + C45 * s


def pocket_floor_z(s, p):
    """z of the pocket floor at slope station s, cut depth p."""
    return slope_z(s) - C45 * p


def main():
    print("open-rear shell: pocket floor vs wall above the outer bottom")
    print("(must stay >= WALL_MIN above z=0)\n")
    worst = float("inf")
    worst_at = None
    for name, s0, s1, p in ZONES:
        zs = [pocket_floor_z(s, p) for s in (s0, (s0 + s1) / 2, s1)]
        zmin = min(zs)
        ok = zmin >= WALL_MIN
        if zmin < worst:
            worst, worst_at = zmin, (name, s0, s1, p)
        print(f"  {name:12} s {s0:5.1f}..{s1:5.1f}  p={p:5.1f}  "
              f"floor z min {zmin:6.2f}  {'OK' if ok else 'BREAKS THROUGH'}")
    print()
    print(f"worst remaining wall: {worst:.2f} mm  at {worst_at[0]}")
    print("req: >= %.1f mm" % WALL_MIN)

    # envelope check
    print()
    top = slope_z(91.0)
    print("slope reach: board top at s=90 -> z = %.2f; s=91 (pocket end) "
          "-> z = %.2f" % (slope_z(90), top))


if __name__ == "__main__":
    main()
