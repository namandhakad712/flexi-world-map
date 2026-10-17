# Enclosure geometry — Fork A final design (commit-ready numbers)

Architecture picked: **A — the CYD look.** Board tilted 45° with the
display-header end up, display panel parallel in front, component side and
module facing the open back. This file is the single source of truth; when
Gemini proposes a part, its numbers get checked against here.

## Global coordinate system

Wedge sits on the desk, screen facing the user (−Y direction).

```
   Z (up)
   │            user looks from this side (−Y)
   │             ╱ display panel, screen faces −Y
   │            ╱  86 long, tilted 45°
   │           ╱
   │          ╱  board plane, 8mm behind display back face
   │         ╱   component side faces +Y (open)
   │        ╱
   │_______╱________________________ → Y (depth, 0 at front face)
  front wall 8mm
```

`x` in the tables below = distance along the slope from the wedge's
front-bottom corner (s = 0). The slope rises at 45°, so ΔY = ΔZ = Δx × 0.707.

## Settled dimensions

### Envelope

| Dimension | Value | Derivation |
| --- | --- | --- |
| Outer width | **56.0** | display 50 + 2×1.0 clearance + 2×2.0 wall |
| Front wall height | **8.0** | from desk to where the slope starts |
| Slope length (s) | **96.0** | display 86 + 4 lip at front + 6 margin at top |
| Slope run / rise | **67.9 / 67.9** | 45° over 96 |
| Total depth | **71.0** | 67.9 + 3 back rim |
| Total height | **76.0** | 67.9 rise + 8 front wall |
| Slope angle | **45°** | |

### Display pocket (in the wedge's sloped face)

| Dimension | Value |
| --- | --- |
| Panel used | Elecrow DLS23028B, 50 × 86, active 43.2 × 57.6 |
| Window opening (screen reveal) | 45.0 × 59.0 — 0.9 mm lip over active area all round |
| Pocket depth (panel beds into slope) | 3.0 |
| Panel position along slope | s = 4 → 90 |
| Position across width | centred in 56 |
| SD card slot relief | pocket floor stays clear, no bosses within 25 × 25 of panel centre |

### Board mounting

The board plane sits **8 mm behind the display panel's back face**
(perpendicular), so its along-position is s = 6 → 91 (85 long).

> **Module height corrected** — see [MODULE-DIMENSIONS.md](MODULE-DIMENSIONS.md).
> The official T5AI-Core STEP shows the module is 72.3 × 44.2 mm with pins
> protruding only 2.9 mm below it, and Tuya's own spec is 73 × 29 × 11 mm
> (17 mm with headers). Realistic module clearance to plan for is
> **≥ 13.0 mm**, not the 9 mm assumed in the first draft. The board-to-cover
> figure below reflects the corrected stack.

| Item | Value | Note |
| --- | --- | --- |
| Perp. gap, display-back to board-solder-side | 8.0 | clears display connector + SD bump |
| Mount holes (board XY) | (4,4) · (81,4) · (4,36) · (81,36) | measured |
| Hole → s coordinate | s = 6 + board_x | |
| Boss | OD 7.0, Ø3.8 hole, M3 heat-set insert 4.0 OD × 4.0 L | printed in the posts |
| Post | from pocket floor up to board, 6.4 tall | 8 gap − 1.6 board |
| Screws | 4× M3 × 10 SHCS, **from the back**, through PCB into inserts | component side is accessible — open back |

Screw access from the back is fine at all four holes: the module socket span
is x 15.8–69.2, so the x=4 and x=81 hole columns sit clear of the module.
Crowded-but-ok: BT1 JST-PH at (8,32) vs H3 at (4,36) = 5.7 mm — verify no
connector body overhangs the hole before printing.

### Rear cover (part 3)

Parallel to the board, **17 mm behind the board plane** — clears the real
module envelope (measured 11 mm tall + pins, see
[MODULE-DIMENSIONS.md](MODULE-DIMENSIONS.md)) plus the button caps (5.0 mm).

> Pocket depth for the module zone is **30.6 mm** perpendicular to the slope
> (gap 8 + board 1.6 + module 13 + cover 2.0 + slack 6). The first draft
> budgeted 26.6 and assumed a closed back wall — that did **not** fit:
> `tools/check_pocket.py` proved the back wall would breach the floor by
> ~4 mm. The corrected model is an open-rear shell; see
> [SHELL-MODEL.md](SHELL-MODEL.md).


| Feature | Value |
| --- | --- |
| Button holes | 3 × Ø6.2 at board (28,24) (42,24) (56,24) mapped onto the cover plane |
| Antenna window | 22 × 35 cutout over the x > 68 zone — no plastic in front of the module antenna |
| Chime bay | reserved 32 × 16 × 6 near board (51,3) — generic, module not bought yet |
| Fastening | 2× self-tap into small printed posts on the wedge rim (no extra hardware) |

### Cable routing

- **J2 → display**: 9-pin female-to-female jumpers fold over the board's top
  edge (s = 91) and drop into the pocket. Path is in the 8 mm gap.
- **USB-C**: uses the board's own receptacle — J5 is at board (0,0), its
  opening points along −X = down the slope toward the front-bottom corner.
  Cut a slot in the front wall at s ≈ 0–8. **No panel-mount pigtail needed.**
  `VERIFY`: confirm J5 receptacle overhangs the x=0 edge (not the y edge)
  before the slot is cut — re-check the footprint pads.

## Part manufacturing order (this drives the Gemini prompts)

1. **Master sketch** — board outline + 4 holes at 1:1 on one sketch, and the
   wedge side-profile on another (front view). Nothing extruded yet.
2. **Wedge base** — extrude side profile across 56, cut display pocket with
   the screen window, add the 4 posts + inserts.
3. **Rear cover** — flat panel with button holes, antenna window, chime bay.
4. **Assembly + interference check** — board + display + base + cover.
5. **Export** — assembly STEP, base STL, cover STL, 3 screenshots.

## Print orientation

- Base prints **flat on its underside**; the slope is a 45° overhang, exactly
  at the no-support limit. Use 0.16–0.20 mm layers and it steps cleanly.
- Rear cover prints face-down, flat, no supports.
- PLA or PETG, 3 perimeters, 15% infill.

## Still open

- **`VERIFY`** J5 USB-C overhang direction (x=0 edge vs y edge) — re-read the
  J5 footprint pads in `lume-coaster.kicad_pcb`. *(pads at x 1.5–6.2 confirm
  the receptacle opens toward the x=0 edge — done in commit b13106f)*
- **`OPEN`** Chime module physical size — bay is generic 32×16 until bought.
- **`OPEN`** Colour choice for the rear cover (cosmetic, pick later).

## Corrected by measurement (supersedes first draft)

| Was | Now | Evidence |
| --- | --- | --- |
| module rides ~9 mm above carrier | **≥ 13.0 mm clearance** | official STEP: 73×29×11 mm, 17 mm with headers; pins 2.9 mm |
| module socket zone x 15.8–69.2 unchanged | confirmed ✓ | measured from both carrier PCB and official module STEP |
| rear cover 14 mm behind component side | now **17 mm** behind board plane | module stack corrected |
| pocket depth 26.6 (module zone) | **30.6** | gap 8 + board 1.6 + module 13 + cover 2.0 + slack 6 |

