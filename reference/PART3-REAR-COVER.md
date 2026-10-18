# Part 3 of 5 — Rear cover

> **For Gemini.** Part 1 (master sketches) and Part 2 (wedge base) should
> already exist. This step builds the rear cover as a separate part. Do not
> start Part 4.

## What this part does

It closes the open rear of the wedge base. The module's component side faces
it, so it carries everything you touch from behind: the three buttons, the
chime bay, and the antenna window.

## Orientation

The cover is a **flat panel parallel to the board plane**, **17.0 mm behind
the board's component-side face**. That clears the module envelope (13.0 from
the board plane) with 4.0 mm to spare for the button caps.

| Item | Value |
| --- | --- |
| Cover thickness | 2.0 |
| Standoff from board component face | **17.0** |
| Panel footprint | same 85 × 40 outline as the board, + 6.0 mm on the two long edges for the fixing flanges → 91 × 52 |

## The four features

### 3.1 Button holes

Three **Ø6.2** holes, at the SW1–SW3 positions mapped onto the cover plane.

Board coordinates → cover coordinates: the cover is parallel to the board, so
the map is a straight translate of the 3 button centres:

| Ref | Board (x, y) | Hole Ø |
| --- | --- | --- |
| SW1 MODE | (28, 24) | 6.2 |
| SW2 UP | (42, 24) | 6.2 |
| SW3 DOWN | (56, 24) | 6.2 |

Buttons are 6×6 mm tactile switches. Ø6.2 gives a finger clearance ring
without the hole being sloppy.

### 3.2 Antenna window

A **22 × 35** rectangular cutout, positioned over the module's antenna end.

| Item | Value |
| --- | --- |
| Window size | 22 across × 35 along the board |
| Position | covers board x > 68 (the antenna end) |
| Why | no plastic sits between the module antenna and the air |

The module's official STEP contains no antenna *body* (verified: 0 hits for
ANTENNA/antenna/FEC), because the 2.4 GHz antenna is a copper shape on the
module PCB. The window is still there so the plastic is thin where the radio
is, and it is the one feature that would be a reprint if forgotten.

### 3.3 Chime bay

A shallow bay for an active chime/buzzer on the J3 header (5 V / GND / TRIG,
3-pin, at (51.46, 3) on the board). The module is not bought yet, so this is
a **reserved generic pocket**:

| Item | Value |
| --- | --- |
| Bay size | 32 × 16 × 6 deep |
| Position | near board (51, 3),component side |
| Note | do not drill through — leave 1.0 mm floor until the buzzer dims are known |

### 3.4 Fixing flanges

Two small flanges, one on each long edge, that reach past the wedge base's
side walls and take a self-tapping screw into a printed post.

| Item | Value |
| --- | --- |
| Flange width | 6.0 beyond the 85-long edge |
| Screw | 2× M2.5 × 6 self-tap (not in the M3 BOM) |
| Post | printed into the base, Ø4.0, at the flange centres |

Do **not** put a flange at the display end — that is where the wedge base is
already closed.

## Hard constraints

1. Cover is **2.0** thick, **17.0** behind the board plane, footprint 91 × 52.
2. Exactly **3** button holes, Ø6.2, at (28,24) (42,24) (56,24).
3. Antenna window **22 × 35** over the board x > 68 region.
4. Chime bay 32 × 16 × **6**, floor 1.0 mm — blind, not through.
5. Cover must not touch the module: ≥ 4.0 mm clearance from the board plane
   to the bay floor.

## What you must output

1. Feature list in build order with the tool for each.
2. One-per-line list of final dimension values.
3. Confirm the bay is blind (floor left) and the window is through.
4. Confirm you stopped and did not start Part 4.
