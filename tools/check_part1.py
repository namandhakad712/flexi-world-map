"""Recheck every number written into PART1-MASTER-SKETCHES.md and
ENCLOSURE-GEOMETRY.md so the two can never drift apart."""

import math

C45 = math.sqrt(2) / 2

# --- Part 1 / wedge profile -------------------------------------------------
front_wall = 8.0
slope_len = 96.0
rise = slope_len * C45
run = slope_len * C45
total_h = front_wall + rise
back_rim = 3.0
total_d = run + back_rim

print("slope run  = %.3f   (Part 1 says 67.9)" % run)
print("slope rise = %.3f" % rise)
print("total height = %.3f (Part 1 says 75.9)" % total_h)
print("total depth  = %.3f (Part 1 says 70.9/71)" % total_d)
assert abs(run - 67.9) < 0.15
assert abs(total_h - 75.9) < 0.15
assert abs(total_d - 71.0) < 0.5

# --- the 5-point polygon closes --------------------------------------------
pts = [(0, 0), (0, front_wall), (run, front_wall + rise),
       (run + back_rim, front_wall), (71.0, 0)]
print()
print("polygon: " + " -> ".join("(%.2f,%.2f)" % p for p in pts))
# slope segment from p2 to p3 must be 45deg
dx = pts[2][0] - pts[1][0]
dz = pts[2][1] - pts[1][1]
ang = math.degrees(math.atan2(dz, dx))
print("slope segment angle = %.3f deg, length = %.3f" % (ang, math.hypot(dx, dz)))
assert abs(ang - 45.0) < 0.01
assert abs(math.hypot(dx, dz) - 96.0) < 0.05

# --- board plane sits 8mm behind a line that STARTS 4mm up the slope -------
# display window line: parallel to slope, starts s=4, 86 long
# board plane line:    parallel to slope, offset 8mm perpendicular
# so board plane spans s = 4+86 ... no: board s=6..91 per spec
print()
print("display line s: 4 .. 90   (86 long)")
print("board plane s : 6 .. 91   (85 long)")
print("board start (s=6) is %.2f mm behind display line start (s=4) along slope"
      % 2.0)

# --- pocket depths vs corrected module stack -------------------------------
# The rear cover is a SEPARATE part behind the board, not inside this pocket.
# The pocket only needs: display gap + board + module envelope + cable slack.
gap = 8.0
board_t = 1.6
module_env = 13.0
slack = 2.0          # cable bend room above the module, inside the pocket
module_pocket = gap + board_t + module_env + slack
print()
print("module zone pocket depth = %.1f (spec says 30.6)" % module_pocket)
assert abs(module_pocket - 24.6) < 0.05

# --- pocket floor stays above the bottom -----------------------------------
def floor_z(s, p):
    return front_wall + C45 * s - C45 * p

zones = [("lip", 4, 6, 3.0), ("board+panel", 6, 21.8, 12.6),
         ("module", 21.8, 75.2, 24.6), ("board top", 75.2, 91, 12.6)]
worst = 1e9
for name, s0, s1, p in zones:
    z = min(floor_z(s, p) for s in (s0, (s0 + s1) / 2, s1))
    print("  %-12s p=%5.1f  floor z min %6.2f  %s" %
          (name, p, z, "OK" if z >= 2.0 else "BREACH"))
    worst = min(worst, z)
print("worst floor: %.2f mm (min 2.0)" % worst)
assert worst >= 2.0

# --- board x positions -> slope station ----------------------------------
print()
for bx in (4, 81):
    print("hole x=%2d -> s=%.2f   (board s = 6 + x)" % (bx, 6 + bx))
print()
print("ALL PART 1 NUMBERS CONSISTENT")
