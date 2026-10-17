# Lume Wedge — desk stand for a T5AI-Core carrier board

A 3D-printable **wedge stand** for the Lume carrier board — an 85 × 40 mm
carrier for the Tuya **T5AI-Core** (T5-E1) module with a 2.8" ILI9341 SPI
display, three tactile buttons and a USB-C power input.

The carrier is a flat slab. On a desk, a flat slab means you look *down* at
the screen at a bad angle and the display's own header holds the panel at zero
degrees. This is the layer that turns the slab into something that faces you:
a low wedge base with a bezel that carries the display at a comfortable
viewing angle, keeping the board, the display, and the USB-C cable path in one
assembly.

```
            display (45deg, facing user)
              \  _________________________
               \  o                    o   <- bezel frame + heat-set inserts
                \  ......... screen .......
                 \  o                    o
                  \_________________________
                   |        wedge base       |
                   |   board cavity + bosses |
                   |__________   ____________|
                              | |
                             USB-C panel mount
```

## Parts

- **Base** — the wedge body. Carries the board on four bosses at the M3
  mounting holes, has a cable channel for the display's FFC to reach the J2
  header without kinking, and a rear panel-mount hole for USB-C.
- **Bezel** — front frame that clamps the display between itself and the base.
  Four M3 heat-set inserts on the base, four M3x10 screws from the bezel.
- **Optional foot** — friction-fit pad so the wedge does not slide.

## Why this shape

The board's display header sits at the far end from the antenna, and the
module's own PCB antenna needs metal *kept away* from it. The wedge puts all
the plastic under the board's display half and keeps the antenna-end boss
field empty — no screw bosses near the antenna, no dense mass of material
under it.

Nothing here is a remix of any existing model. The reference I looked at
(MakerWorld "CYD desk buddy") was for a totally different board with an
on-board display; this is drawn from my own board's measurements so the
cavity, bosses and bezel all come from the real footprint.

## Board measurements (these drive every dimension)

Source: measured from the fabricated `lume-coaster.kicad_pcb`, not guessed.

| Thing | Value |
| --- | --- |
| Board outline | 85 × 40 mm, 1.6 mm thick |
| M3 mounting holes (drill 3.2 mm) | (4,4) · (81,4) · (4,36) · (81,36) |
| USB-C receptacle (J5) | left edge, centred at (0,0) on the left side |
| Display header (J2) | 9-pin 2.54 mm male header, x=76, y 8.5–31.4 |
| Module sockets (J1_TOP / J1_BOT) | two 1×22 vertical, x 15.83–69.17, y=7.3 & 32.7 |
| Module height above carrier | ~9 mm (socket + male pins) |
| Antenna keepout | right third of the board (x > 68 mm) |
| Tactile buttons SW1–SW3 | 6×6×5 mm, y=24, x = 28 / 42 / 56 |
| Chime header (J3) | 3-pin horizontal, (51.46, 3) |
| LiPo connector (BT1) | JST-PH, (8, 32) — top side |

The display is mounted by wire (not plugged directly onto J2), so the bezel
positions it freely and a small FFC channel runs around the board edge.

## Printing

- 0.20 mm layer height, PLA or PETG
- Base prints flat on its underside, no supports
- Bezel prints face-down, no supports
- 3 perimeters / 15% infill

## BOM

See [BOM.md](BOM.md) — approx $3.50 in filament and 4× M3x10 screws plus 4×
M3 heat-set inserts.

## Repo layout

```
cad/            Onshape model source (this folder gets the exported studio file)
exports/        STEP + STL exports for the submission
reference/      board measurements and the reference photos used while modeling
BOM.md          parts list
JOURNAL.md      work log (mirrored from the Half Life platform)
```

## Status

Modeling in Onshape. See [JOURNAL.md](JOURNAL.md) for the session log.
