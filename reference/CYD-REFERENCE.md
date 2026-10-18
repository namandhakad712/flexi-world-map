# CYD Desk Buddy — measured reference (from the exported STEP)

Source: `CYD Desk Buddy 45° Symmetrical.step` + `CYD Desk Buddy - Non-Symmetrical.step`
+ `CYD Desk Buddy Parametric v1.2.f3d` (all downloaded from MakerWorld into
`reference/`). Geometry measured directly from the STEP by
`tools/measure_cyd6.py`, not estimated.

The case is modelled tilted 45° about its X axis, so a feature lying in the
board plane appears as equal-magnitude Y and Z deltas: in-plane distance =
dy × √2.

## CYD geometry (what the model actually has)

| Feature | Measured value |
| --- | --- |
| Case overall X span (width across) | 102.8 (sym) / 99.2 (non-sym) |
| M3 mounting posts | **4 × Ø3.5** (r = 1.75) |
| Mount hole span along the long axis | **78.4 mm** (x = −36.30 → 42.10) |
| Mount hole span across the width | **42.0 mm** in-plane (dy = dz = 29.70) |
| Hole row offset | centred about x = +2.9 (not symmetric — the board is offset toward the display end) |
| Bezel clip holes | 8 × Ø3.2, two pairs at each end |
| Case side walls | Ø8.4 / Ø9.6 / Ø11.6 ventilating slots on the flanks |

## Our board (measured from the fabricated PCB)

| Feature | Measured value |
| --- | --- |
| Board outline | **85.0 × 40.0** |
| Mount drill | Ø3.2 (M3, non-plated) |
| Mount holes | (4,4) · (81,4) · (4,36) · (81,36) |
| Mount span long axis | **77.0 mm** (x = 4 → 81) |
| Mount span across width | **32.0 mm** (y = 4 → 36) |
| Hole row offset | centred about x = 42.5 (symmetric) |
| Module envelope | 72.3 × 44.2, pins 2.9 below, sits ~13 above carrier |
| Display module | Elecrow DLS23028B **50 × 86**, active 43.2 × 57.6 |
| Buttons | 3 × 6×6×5 tactile at (28,24) (42,24) (56,24) |
| USB-C | left edge at (0,0), opens toward −X |
| Chime | 3-pin horizontal header at (51.46, 3) |

## The deltas (this is the edit list)

| # | Feature | CYD | Ours | Change |
| --- | --- | --- | --- | --- |
| 1 | Mount span, long axis | 78.4 | **77.0** | −1.4 mm |
| 2 | Mount span, across width | 42.0 | **32.0** | **−10.0 mm** |
| 3 | Mount drill diameter | Ø3.5 | Ø3.2 drill, but use Ø3.5 clearance in the case | keep 3.5 |
| 4 | Mount row offset | x ≈ +2.9 off-centre | **0, symmetric** (x 4 → 81) | re-centre |
| 5 | Board width | ~52 | **40.0** | **−12 mm** — the whole case narrows |
| 6 | Board length | ~85–86 | **85.0** | ≈0 |
| 7 | Screen | 2.8" on-board | **2.8" on a 50 × 86 breakout, wire-mounted** | different mounting, same panel |
| 8 | Buttons | none (touchscreen) | **3 tactile at (28,24) (42,24) (56,24)** | **add 3 side/back cutouts** |
| 9 | USB entry | rear panel-mount pigtail | **board's own USB-C, left edge** | rear slot → side slot |
| 10 | Antenna | n/a | **keepout: no metal bosses in the module antenna zone** | new constraint |
| 11 | Chime | n/a | **3-pin header at (51.46, 3)** | reserve a small bay |

The single biggest change is #2/#5: our board is **10 mm narrower between
mount holes and 12 mm narrower overall** than the CYD, so the case's
cross-section and the boss pattern must narrow with it. The length is
essentially unchanged.

## What stays the same

- The overall wedge look, the 45° viewing angle, the front bezel + body split
- The 4 × M3 screws (Ø3.5 clearance)
- The rear-enclosed, panel-mount-style back
- Print orientation and the "no supports" slicability
- The 2.8" screen scale (same panel as the CYD)

> Designer's own note in the listing: *"A STEP file is included for anyone
> wishing to adapt the enclosure for their own projects."* This is the
> sanctioned adaptation path. Credit goes in the README as
> "adapted from annaglyph's CYD Desk Buddy (MakerWorld)".
