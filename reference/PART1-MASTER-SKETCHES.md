# Part 1 of 5 — Master sketches (the ONLY thing to build in this step)

> **For Gemini.** This is a step in a 5-part build. Do Part 1 and stop.
> Do not extrude, do not build solids, do not start Part 2.

## What you are modeling

A **desk wedge stand** for a carrier board. Two sketches define everything:

- **Sketch "board plane"** — the carrier board outline + its 4 mounting holes,
  drawn 1:1, on a plane tilted 45°.
- **Sketch "wedge profile"** — the side silhouette of the wedge stand, closed
  polygon, in the front view plane.

## Sketch 1 — "board plane"

Create a plane **tilted 45°** from horizontal, then on it draw the carrier:

| Element | Geometry |
| --- | --- |
| Board outline | rectangle **85.0 × 40.0**, origin lower-left corner |
| Mount holes | 4 circles Ø **3.2** at **(4,4) (81,4) (4,36) (81,36)** |

The board's Y axis along the slope; X across the width. (The real module is
72.3 × 44.2 mm with 25.4 mm header-row spacing and sits **13 mm above** this
plane — but do NOT draw the module. Only the board outline and the 4 holes.)

All 4 hole positions must be **explicitly dimensioned** (not inferred).

## Sketch 2 — "wedge profile" (side view)

Closed polygon, sitting on a ground line, in the plane you see the wedge from
the side. Points in order:

| # | Point | Note |
| --- | --- | --- |
| 1 | (0, 0) | front-bottom corner on the ground |
| 2 | (0, 8) | top of the **front wall** (8 mm tall) |
| 3 | (67.9, 75.9) | top of the slope — slope length 96.0 at 45° |
| 4 | (70.9, 8) | bottom of the open rear, 3 mm behind the slope's horizontal reach |
| 5 | (71, 0) | back-bottom corner on the ground |

That is a **5-point closed polygon**: (0,0) → (0,8) → (67.9,75.9) → (70.9,8) →
(71,0) → close.

The segment from point 2 to point 3 is **the 45° slope face** — it must carry a
real 45.000° dimension. Its length is 96.0.

Also add, as **construction geometry only** (no cut, no solid):

| Construction line | Where |
| --- | --- |
| Display window on the slope | a line parallel to the slope, offset, starting 4 mm up the slope, **86 mm** long |
| Board plane | a second line parallel to the slope, offset **8 mm** perpendicular inward from the display-window line — this is where Sketch 1's plane sits |

## Hard constraints

1. The 45° on the slope is a **real dimension**, value 45.000°.
2. The 4 hole positions are **explicitly dimensioned** to (4,4) (81,4) (4,36) (81,36).
3. The board outline is exactly 85 × 40.
4. Everything sits on or above the ground line y = 0.
5. Sketches are named **`board plane`** and **`wedge profile`**.

## What you must output

1. The exact Onshape click sequence for both sketches: which plane/tool, what
   was typed into which dimension field.
2. A plain list of the final dimension values used, one per line:
   ```
   board_width = 85.000
   board_height = 40.000
   hole_diameter = 3.200
   hole_1_x = 4.000 hole_1_y = 4.000
   ... etc
   slope_angle = 45.000
   slope_length = 96.000
   front_wall_height = 8.000
   total_depth = 71.000
   total_height = 76.000
   ```
3. Confirm you stopped and did not extrude.

## The 5-part plan (context — do not start)

Part 2 extrudes the profile across 56 mm and hollows the shell. Part 3 is the
rear cover. Part 4 is the assembly + interference check. Part 5 is export
(STEP + 3 screenshots).
