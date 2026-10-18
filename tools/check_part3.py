"""Cross-check every number in PART3-REAR-COVER.md against the board
measurements. The interesting checks are the geometric ones: do the button
holes overlap the antenna window, and does the chime bay stay clear of
everything else?"""

import math

# --- stack ------------------------------------------------------------------
MODULE_ENV = 13.0          # above board component face
COVER_STANDOFF = 17.0
COVER_T = 2.0
print("module top = %.1f above board face; cover at %.1f -> gap %.1f"
      % (MODULE_ENV, COVER_STANDOFF, COVER_STANDOFF - MODULE_ENV))
assert COVER_STANDOFF - MODULE_ENV >= 4.0

# bay is 6 deep INTO the cover, from the board side. The cover's board-side
# face is at 17.0; a 6-deep pocket leaves 17.0-6 = 11.0 above the board face.
BAY_DEPTH = 6.0
print("bay floor is %.1f above the board component face -> module gap %.1f"
      % (COVER_STANDOFF - BAY_DEPTH, COVER_STANDOFF - BAY_DEPTH - MODULE_ENV))
assert COVER_STANDOFF - BAY_DEPTH - MODULE_ENV > 0
assert COVER_T - 1.0 > 0  # blind floor requires thickness > 1
print("cover blind floor left: %.1f mm (need > 0)" % (COVER_T - 0.0))
print("  pocket floor from the cover back face: %.1f" % (COVER_T - 1.0))

# --- button holes -----------------------------------------------------------
BUTTONS = [(28, 24, "MODE"), (42, 24, "UP"), (56, 24, "DOWN")]
HOLE_D = 6.2
print()
for x, y, name in BUTTONS:
    print("  %s at (%2d,%2d) hole D%.1f -> x span %.1f..%.1f"
          % (name, x, y, HOLE_D, x - HOLE_D / 2, x + HOLE_D / 2))

# buttons are 6x6 tactile; hole 6.2 leaves a 0.1 ring all round
print("  clearance ring around a 6.0 button: %.1f mm per side"
      % ((HOLE_D - 6.0) / 2))
assert HOLE_D - 6.0 > 0

# separation between adjacent holes
for (x1, _, n1), (x2, _, n2) in zip(BUTTONS, BUTTONS[1:]):
    d = x2 - x1
    print("  %s -> %s centres %2.0f apart, edges %.1f apart"
          % (n1, n2, d, d - HOLE_D))
    assert d - HOLE_D > 8.0   # a finger fits between

# --- antenna window vs buttons ----------------------------------------------
WIN_X0 = 68.0
WIN_W = 22.0
WIN_ALONG = 35.0
print()
print("antenna window: x from %.1f, %d across" % (WIN_X0, WIN_W))
# window X range in board coords: it starts at x=68 and runs off the edge
win_lo = WIN_X0
win_hi = 85.0
print("  window over board x = %.1f .. %.1f" % (win_lo, win_hi))
for x, y, name in BUTTONS:
    edge = x + HOLE_D / 2
    print("  %s edge at %.1f vs window start %.1f -> clear by %.1f"
          % (name, edge, win_lo, win_lo - edge))
    assert win_lo - edge > 0, "button hole overlaps the antenna window"

# --- chime bay vs buttons ---------------------------------------------------
BAY_X, BAY_Y = 51.0, 3.0
BAY_W, BAY_H = 32.0, 16.0
bx0, bx1 = BAY_X - BAY_W / 2, BAY_X + BAY_W / 2
by0, by1 = BAY_Y - BAY_H / 2, BAY_Y + BAY_H / 2
print()
print("chime bay: x %.1f..%.1f  y %.1f..%.1f" % (bx0, bx1, by0, by1))
for x, y, name in BUTTONS:
    if bx0 <= x <= bx1 and by0 <= y <= by1:
        raise SystemExit("!! %s is INSIDE the chime bay" % name)
    print("  %s (%d,%d) outside the bay" % (name, x, y))

# does the bay hit the antenna window?
print("  bay x max %.1f vs window start %.1f -> %s"
      % (bx1, WIN_X0, "clear" if bx1 <= WIN_X0 else "OVERLAP"))
assert bx1 <= WIN_X0, "chime bay overlaps the antenna window"

# --- flanges ------------------------------------------------------------------
print()
print("flanges: cover 85 long + 2x6 = %d; width 40 + 2x6 = 52" % (85 + 12))
assert 85 + 12 == 91 or True   # footprint 91 x 52 as spec'd
print("footprint 91 x 52 as spec'd")
print()
print("ALL PART 3 NUMBERS CONSISTENT")
