# Part 2 of 5 — Wedge base (the front shell)

> **For Gemini.** Part 1 (two master sketches) should already exist. This step
> builds the front shell as one part. Do not start Part 3.

## From Part 1, reuse

- `board plane` sketch (85 × 40 board + 4 × Ø3.2 holes at (4,4) (81,4)
  (4,36) (81,36)), on the 45° plane.
- `wedge profile` sketch (the 5-point polygon, 45° slope, 96 long).

## What to build

### 2.1 The solid wedge

Extrude the `wedge profile` polygon **across the width**, 56.0 mm total. Use a
symmetric extrude so the profile is centred in the width. Result: the raw
wedge brick, 71 × 76 × 56.

### 2.2 Hollow it into an open-rear shell

- **Floor**: 2.0 mm thick — the pocket floor must stay ≥ 3.33 mm above the
  outer bottom in the board+panel zone (already verified; keep 2.0).
- **Side walls**: 2.0 mm, both sides.
- **Front wall**: keep the full 8.0 mm.
- **Rear**: open. No back wall. (A closed back wall was proven to breach the
  floor — see [SHELL-MODEL.md](SHELL-MODEL.md).)
- **Sloped face**: keep 2.0 mm of material between the outer slope and the
  cavity.

The cavity is cut from the slope side, leaving the rear fully open.

### 2.3 The display window

In the sloped face, cut a rectangular window opening **45.0 × 59.4** (in the
slope plane), centred across the width. Retaining lip: 0.9 mm of material
over the active area all round.

The window opens into the cavity so the display panel can be inserted from
inside.

### 2.4 The four board bosses

On the cavity floor (slope side), at the 4 hole locations from `board plane`,
add bosses that are **perpendicular to the cavity floor** (not vertical):

| Item | Value |
| --- | --- |
| Boss OD | 7.0 |
| Centre hole | Ø3.8 |
| Height above cavity floor | **9.0** (board plane is 11.0 in from the slope; the floor is the 2.0 shell wall, so the boss is 11.0 − 2.0) |
| Position | at the 4 hole centres, on the cavity floor |

Each boss must land on the board-plane hole positions — use the `board plane`
sketch to transfer them, do not re-draw.

All four holes land at s = 10.0 and s = 87.0, both **outside** the module
zone (s 21.8 → 75.2), so no boss collides with the module.

### 2.5 The USB-C slot

Cut a slot in the **front wall** at the bottom of the slope, aligned to the
board's own USB-C receptacle: at s ≈ 0 → 8, centred transversely on the
receptacle position.

Keep the slot **Ø9.0 circular** (round is easiest to cut and matches a
USB-C cable gland). Center it so the cable clears the receptacle body.

## Hard constraints

1. Extrusion width is exactly **56.0**.
2. Slope stays exactly 45.000° and 96 long.
3. The cavity floor is **2.0** thick and the rear is fully open.
4. Bosses are **perpendicular to the slope**, OD 7.0, hole Ø3.8, height 9.0
   above the floor, at the 4 hole positions.
5. The display window is **45 × 59** in the slope plane with a 0.9 lip.

## What you must output

1. The feature list in build order with the exact tool used for each
   (Extrude / Shell / Extrude-cut / Hole / Revolve).
2. A plain list of the final dimension values, one per line.
3. A cross-section screenshot description (what would be visible at the
   cavity floor).
4. Confirm you stopped and did not start Part 3.
