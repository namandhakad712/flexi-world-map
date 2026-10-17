"""Cross-check every number in PART2-WEDGE-BASE.md against the committed
wedge arithmetic and the board measurements.

Geometry model (open-rear shell -- the ONLY one that is consistent):

  depth, measured perpendicular from the slope face, going inward:

     0.0   slope face
     0..2  display window lip / panel sits here, retained by 0.9 lip
     2.0   cavity floor = the shell wall (uniform, NOT stepped)
     3.0   display panel back face (recessed behind the window)
    11.0   board solder-side face = 3.0 recess + 8.0 gap
    12.6   board component-side face = 11.0 + 1.6 PCB
   25.6    module envelope top = 12.6 + 13

  The module (12.6 .. 25.6) extends toward the open rear and exits through
  the rear opening -- that is the whole point of the open-rear shell. There
  is no pocket floor step under the module, because there is no floor there.
"""

import math

C45 = math.sqrt(2) / 2
FRONT_WALL = 8.0
WALL = 2.0
WIDTH = 56.0
SLOPE_LEN = 96.0

# --- the stack --------------------------------------------------------------
RECESS = 3.0          # display panel beds this far in
GAP = 8.0             # display back face -> board solder side
BOARD_T = 1.6
MODULE_ENV = 13.0

BOARD_IN = RECESS + GAP          # 11.0
BOARD_FAR = BOARD_IN + BOARD_T   # 12.6
MODULE_TOP = BOARD_FAR + MODULE_ENV  # 25.6

print("stack: slope 0 -> floor 2.0 -> panel-back 3.0 -> board 11.0 -> 12.6 -> module top %.1f"
      % MODULE_TOP)

# --- boss height ------------------------------------------------------------
# Bosses rise from the cavity floor (depth 2.0) to the board (depth 11.0).
boss_needed = BOARD_IN - WALL
print()
print("boss height = board depth %.1f - shell %.1f = %.1f" %
      (BOARD_IN, WALL, boss_needed))
assert abs(boss_needed - 9.0) < 0.01

# --- boss wall and screw/insert fit -----------------------------------------
print("boss OD 7.0, hole 3.8 -> wall each side %.1f mm" % ((7.0 - 3.8) / 2))
print("insert 4.0 long in 9.0 boss -> %.1f mm to spare" % (boss_needed - 4.0))
print("M3x12 screw: PCB 1.6 + boss 9.0 = %.1f of travel, screw 12 long -> %.1f to spare"
      % (BOARD_T + boss_needed, 12 - (BOARD_T + boss_needed)))

# bosses sit at hole positions -----------------------------------------------
HOLES = ((4, 4), (81, 4), (4, 36), (81, 36))
print()
for bx, by in HOLES:
    s = 6.0 + bx   # board x -> slope station
    print("hole (%2d,%2d) -> s=%5.2f  (module zone is s 21.8..75.2: %s)"
          % (bx, by, s, "outside" if (s < 21.8 or s > 75.2) else "INSIDE"))
    assert s < 21.8 or s > 75.2, "boss would collide with the module envelope"

# --- window ------------------------------------------------------------------
ACTIVE = (43.2, 57.6)
LIP = 0.9
win = (ACTIVE[0] + 2 * LIP, ACTIVE[1] + 2 * LIP)
print()
print("window = active + 2*0.9 = %.1f x %.1f  (spec 45 x 59.4)" % win)
assert abs(win[0] - 45.0) < 0.01 and abs(win[1] - 59.4) < 0.01
print("window inside the 86-long panel span: margin per end = %.1f"
      % ((86.0 - 59.4) / 2))

# --- width -------------------------------------------------------------------
print()
print("width = display 50 + 2x1.0 clear + 2x2.0 wall = %.1f" %
      (50 + 2 * 1.0 + 2 * WALL))
assert WIDTH == 56.0

# --- shell floor vs the outer bottom ----------------------------------------
# The cavity floor is a plane 2mm perpendicular from the slope. The material
# under it, down to z=0, grows with s. Verify it never exits the part.
def slope_z(s):
    return FRONT_WALL + C45 * s

worst = 1e9
for s in (0.0, 4.0, 6.0, 21.8, 45.0, 75.2, 91.0, 96.0):
    z_floor = slope_z(s) - C45 * WALL
    if z_floor < worst:
        worst = z_floor
    print("  s=%5.1f  floor z=%6.2f" % (s, z_floor))
print("worst cavity-floor height above z=0: %.2f mm (must be > 0)" % worst)
assert worst > 0

# --- front wall and total envelope ------------------------------------------
rise = SLOPE_LEN * C45
print()
print("front wall 8, slope 96 at 45deg -> rise %.3f, total height %.3f"
      % (rise, FRONT_WALL + rise))
assert abs((FRONT_WALL + rise) - 75.9) < 0.1

print()
print("ALL PART 2 NUMBERS CONSISTENT (boss height corrected to 9.0)")
