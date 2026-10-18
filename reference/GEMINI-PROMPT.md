# The Gemini prompt — adapt the CYD Desk Buddy to our board

Paste this whole block to Gemini. It is self-contained: it has the reference
geometry (measured from the CYD STEP), our board's real measurements, the
exact edit list, and the constraints.

---

I imported the "CYD Desk Buddy 45° Symmetrical" STEP into Onshape. I need it
adapted to MY carrier board. The designer published this STEP specifically
for adaptation ("A STEP file is included for anyone wishing to adapt the
enclosure for their own projects"), so this is a sanctioned adaptation, not a
copy — I will credit annaglyph's CYD Desk Buddy in my README.

**Work part-by-part, one feature group per message, and wait for me between
parts.** I am screen-recording, so the model has to build up in visible
steps, not one generated lump.

## The reference geometry (what the imported model actually has)

Measured from the STEP, not guessed. The case is modelled tilted 45° about
its X axis, so a feature in the board plane appears as equal-magnitude Y and
Z deltas — in-plane distance = dy × √2.

- Case overall X span: 102.8 mm
- 4 × M3 mounting posts, Ø3.5 clearance
- Mount holes along the long axis: x = −36.30 → 42.10 (span **78.4**), offset
  +2.9 mm toward the display end
- Mount holes across the width: in-plane span **42.0** (dy = dz = 29.70)
- 8 × Ø3.2 bezel clip holes, two pairs per end
- Vent slots Ø8.4 / Ø9.6 / Ø11.6 on the flanks
- Front bezel + body split, fully enclosed rear, 45° wedge

## MY board (measured from the fabricated PCB)

- Board outline: **85.0 × 40.0**, thickness 1.6
- Mount holes: Ø3.2 drill (M3), at **(4,4), (81,4), (4,36), (81,36)**
- Mount span long axis: **77.0** (x = 4 → 81), centred, symmetric
- Mount span across width: **32.0** (y = 4 → 36)
- Module: T5AI-Core, 72.3 × 44.2, rides ~13 mm above the carrier on two
  1×22 sockets, pins 2.9 mm long. **Antenna zone: keep metal bosses out of
  the module's right third (x > 68).**
- Display: Elecrow DLS23028B breakout, **50 × 86**, active area 43.2 × 57.6,
  9-pin SPI, **wire-mounted** (it does NOT plug into the board). SD card slot
  on the back of the module.
- 3 tactile buttons, 6×6×5, at **(28,24), (42,24), (56,24)** — but they sit
  under the module, so they must be reached from the side, not the top
- USB-C receptacle: left edge at (0,0), opens toward −X (points out the left
  side of the board). Uses the board's own connector, no panel-mount pigtail.
- Chime: 3-pin header at (51.46, 3), generic active buzzer, not bought yet

## The edit list

| # | What | Change |
|---|---|---|
| 1 | Mount span, long axis | 78.4 → 77.0 (−1.4) |
| 2 | Mount span, across width | 42.0 → 32.0 (**−10**) |
| 3 | Mount row offset | re-centre to symmetric x 4 → 81 |
| 4 | Cross-section | the case narrows by ~12 overall (52 → 40 board) |
| 5 | Board length | unchanged (≈85) |
| 6 | Mount drill | keep Ø3.5 clearance in the case |
| 7 | Screen | same 2.8" panel, but the pocket now beds a 50 × 86 breakout, wire-mounted, with ~2.5 SD relief behind it |
| 8 | Buttons | add 3 side-reachable cutouts for the tactiles at (28,24) (42,24) (56,24) |
| 9 | USB-C | replace the rear panel-mount with a side cutout at the left edge, (0,0) |
| 10 | Antenna | no bosses or dense plastic in x > 68 |
| 11 | Chime | reserve a generic 32 × 16 bay near (51.46, 3) |

## Keep unchanged

The wedge look, the 45° angle, the front bezel + body split, the rear-enclosed
style, print orientation (case flat on base, bezel face-down), and "no
supports needed" slicability.

## Constraints

- 4 × M3 × 12 screws, bosses Ø7.0 outer / Ø3.8 hole for heat-set inserts
  (the screw spans board 1.6 + boss 9.0 = 10.6 of travel)
- Wall thickness 2.0
- The module needs ≥13 mm clearance above the carrier
- Output: keep the whole thing an assembly of case + bezel, as in the import

## Part order (one per message, STOP after each)

1. Report the imported model's actual tree: parts, names, and the coordinate
   system. Confirm nothing is broken on import.
2. Re-dimension the mounting bosses to my hole pattern (+1, +2, +3, +4).
3. Narrow the cross-section (+4) — case width follows the board.
4. Re-cut the display pocket for the 50 × 86 breakout (+7).
5. Button cutouts (+8) and USB-C side slot (+9).
6. Antenna zone and chime bay (+10, +11).
7. Final check: interference, wall thickness, prints-without-supports.

After every part, list the exact feature names and dimensions you changed,
one per line, so I can verify them.
