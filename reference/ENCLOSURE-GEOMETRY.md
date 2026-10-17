# Enclosure geometry — settled parameters + the design fork

Every dimension that is *decided* goes here. Anything still open is labelled
`OPEN`. When Gemini proposes a part, its numbers are checked against this
file.

## Confirmed by measurement or vendor datasheet

### Board (measured from fabricated PCB, commit 1a13f18)

| Property | Value |
| --- | --- |
| Outline | 85.0 (X) × 40.0 (Y) × 1.6 |
| M3 holes (drill 3.2) | (4,4) · (81,4) · (4,36) · (81,36) |
| Under-board pin protrusion | ~3.0 mm (J1 socket + J2 header tails) |
| Module above carrier top | ~9 mm → component envelope ≈ 10.6 mm |

### Display module (Elecrow DLS23028B, from BOM)

| Property | Value |
| --- | --- |
| Module PCB | **50 × 86 mm** |
| Active area | 43.2 × 57.6 mm |
| Interface | 9-pin SPI header (VCC GND CS RST DC SDI SCK LED SDO) |
| Extra | SD card slot on the back side — needs ~2.5 mm relief behind module |
| Consequence | Display is **wider than the board** (50 > 40) and almost as long (86 ≈ 85) |

### Fixed case parameters (decided)

| Parameter | Value | Why |
| --- | --- | --- |
| Wall thickness | 2.0 mm |.printable, stiff |
| Floor thickness | 2.0 mm | flat base |
| Boss OD | 7.0 mm | M3 heat-set insert (4.0 mm OD) needs ≥1.5 mm wall |
| Boss hole | 3.8 mm | press/melt fit for 4.0 mm OD insert |
| Boss height | 4.0 mm | clears 3.0 mm of under-board pin tails |
| Screw | M3 × 10 SHCS | through PCB into insert |
| Display angle | 45 deg | user choice |
| Board-to-display gap | ≥ 14 mm | module envelope 10.6 + cable + slack |
| Layer height | 0.20 mm, PLA | |

## The design fork

The display being 86 mm — the same length as the board — is what forces a
choice. Two architectures both work, both are printable, and the display
numbers are identical in both. What differs is where everything else ends up.

### Fork A — "the CYD look": whole board tilted back at 45 deg

```
                 ╱ display (in bezel, screen faces you)
                ╱   86 x 50, tilted 45
               ╱
              ╱ ← 14 mm gap, module + J2 cable live here
             ╱
            ╱ ← carrier board 85 x 40, also tilted 45
           ╱
   _______╱_________________________________
   │            wedge base                  │
   └──── USB-C cutout in left wall ─────────┘
```

- Board tilted 45° with the **x=85 (display-header) end UP**.
- Component side faces the **back**, which is open — so the module antenna
  radiates into free air, nothing above it.
- Footprint ≈ 70 deep × 56 wide × 63 tall.
- Buttons, module and chime all end up on the open back — speaker grill
  on the back or the left wall.
- Mounting: M3 screws from the back, through PCB into inserts held by the
  bezel side rails.
- Matches the reference stand's proportions.

### Fork B — "tray + leaning screen": board flat, display leaning above it

```
        display 86x50 leaning forward at 45°
        ╱‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╲
       ╱    screen faces you    ╲
      ╱__________________________╲
      │  o module + antenna       │
      │  o o o ← buttons, face up │
      │        (board lies flat)  │
      │__________________________ │
```

- Board lies horizontal in a shallow open tray — easiest to drop in,
  easiest screws (straight down into base bosses).
- Display leans at 45° above/behind the board, either rising from the rear
  edge or overhanging forward.
- Nothing is above the module antenna at all — best possible RF.
- Footprint ≈ 90+ deep × 56 wide × 75 tall (bigger, taller than A).
- Buttons accessed from the top, speaker grill in a tray wall.

## Still open

- **`OPEN` Fork A vs Fork B** — user's call, it changes the whole build order.
- **`OPEN` Chime module physical size** — the J3 3-pin header feeds a separate
  active chime/buzzer that has to live somewhere in the case. Need its mm.
- **`OPEN` Display cable length/type** — J2 is 9-pin 2.54 male header; the
  Display side needs matching female-to-female jumpers or a cut ribbn. Fix
  the routing only after the fork is chosen.
