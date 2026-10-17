# Board measurements — source of truth for every CAD dimension

Every number below is extracted from the fabricated
`lume-coaster.kicad_pcb` (commit `1a13f18`, gerbers verified). Do not
re-derive from photos or from memory. If the model disagrees with this file,
this file wins.

## Coordinate system

Origin = lower-left corner of the board. +X to the right, +Y "up" the board
(toward the far edge from the USB-C). All values in millimetres.

```
  (0,40) o──────────────────────────────o (85,40)
         │  antenna keepout (x > 68)    │
         │   ┌ ─ ─ ─ ─ ─ ─ ─┐          │
         │   module zone     │   DISP  │
         │   x 15.8 → 69.2  │  J2 x76 │
         │   └ ─ ─ ─ ─ ─ ─ ─┘          │
         │                            │
         │  o  o  o    buttons y=24   │
         │                            │
   USB-C │  o                     o    │
  (0,0)  o──────────────────────────────o (85,0)
```

## Board

| Property | Value |
| --- | --- |
| Outline | 85.0 × 40.0 (rectangle, 4 edge cuts) |
| Thickness | 1.6 |
| Layer count | 2 (F.Cu / B.Cu) |

## Mounting — 4× M3

Drill 3.2 mm, non-plated. Best fastener: M3 × 10 mm SHCS into heat-set
inserts in the base bosses.

| Ref | X | Y |
| --- | --- | --- |
| H1 | 4 | 4 |
| H2 | 81 | 4 |
| H3 | 4 | 36 |
| H4 | 81 | 36 |

Boss centre = hole centre. Recommend boss OD 6.0 mm (for a 4.0 mm OD
heat-set insert you want ≥0.5 mm wall all round).

## Populated envelope (top side)

| Component | X | Y | Footprint |
| --- | --- | --- | --- |
| J1_TOP socket | 15.83 → 69.17 | 7.3 | 1×22 vertical 2.54 |
| J1_BOT socket | 15.83 → 69.17 | 32.7 | 1×22 vertical 2.54 |
| Module above carrier | — | — | ~9 mm higher than carrier top face |
| J2 display header | 76 | 8.5 → 31.4 | 1×9 vertical 2.54 |
| J3 chime header | 51.46 | 3 | 1×3 horizontal 2.54 |
| BT1 LiPo JST-PH | 8 | 32 | 1×2 horizontal 2.0 |
| J5 USB-C | 0 | 0 | SMD receptacle, left edge |
| SW1 MODE | 28 | 24 | 6×6×5 SMD tactile |
| SW2 UP | 42 | 24 | 6×6×5 SMD tactile |
| SW3 DOWN | 56 | 24 | 6×6×5 SMD tactile |
| Q1 / R_BL1 | 71 / 67 | 26.58 | — |

## Antenna keepout

The module's on-board antenna is over the right third of the board.
Keep **all** screw bosses, threaded inserts and dense material away from
**x > 68 mm**. This is why only H2 (81, 4) sits on that side and gets a
minimal boss.

> Geometry note: the module is elevated ~9 mm above the carrier on male
> pins, so the antenna is physically away from the carrier copper. That's
> why the board-level pour is full-width. The *case* is a different story —
> a solid wedge of plastic directly under the module still loads the
> antenna. Keep the plastic thin and the bosses far away.

## Stand geometry (case, not board)

| Property | Target |
| --- | --- |
| Viewing angle | 45° |
| Wall thickness | 1.8–2.0 mm |
| Board-to-lid clearance | ≥ 11 mm (module 9 mm + 2 mm slack) |
| Print | PLA, 0.20 mm, no supports |
