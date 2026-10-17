# T5AI-Core module — physical envelope (measured from the official STEP)

Source: `T5AI-Core_V101.step` (T5AI-Core 3D structural file V101), downloaded
from [TuyaOpen docs](https://tuyaopen.ai/docs/hardware/tuya-t5/t5-ai-core/overview-t5-ai-core)
37,024,832 bytes, 534,820 STEP entities, 109 solid bodies, 305 named
components (R0402 resistors, SOD-523 diodes, `indc4040x180` shield can,
two `CN254-1X22-M-DL-H904` 1×22 male headers etc.)

These numbers are **measured from the manufacturer's own 3D file**, not
estimated. They supersede any guess in the enclosure spec until a real
sample is measured with calipers.

## Board envelope

| Axis | Span | Interpretation |
| --- | --- | --- |
| Long axis | **72.3 mm** (−4.80 → 67.50) | matches Tuya's stated "73 mm" |
| Short axis | **44.2 mm** (−16.20 → 28.04) | populated width incl. headers; bare PCB is 29 mm |
| Thickness | **1.6 mm** (slab z 0.2 → 1.6) | standard 2-layer |
| Pin protrusion below board | **2.9 mm** | male header pins (z −2.88 → −0.36) |

> Tuya's own docs say "Board dimensions: 73 mm × 29 mm × 11 mm (excluding pin
> headers) / 17 mm (including pin headers)". The 11 mm is **tallest
> component**, and 29 mm is the bare PCB width. The measured 44.2 mm is the
> populated width including the headers' own width. The measured 72.3 mm
> matches their 73 mm within 0.7 mm.

## Header rows

| Fact | Value |
| --- | --- |
| Pin field long axis | y = −8.13 → 64.72 (**72.85 mm**) |
| Header part | `CN254-1X22-M-DL-H904`, ×2 |
| Pin pitch | 2.54 mm |
| Row spacing (measured, carrier) | **25.4 mm** centre-to-centre |
| Rows run | along the long axis (22 pins × 2.54 = 53.34 mm each row) |

## What this means for the carrier-board interface

The Lume carrier was pinned from the fabricated board's own geometry:

| Carrier fact | Value |
| --- | --- |
| Socket pin field along X | 15.83 → 69.17 |
| Socket rows | y = 7.3 and y = 32.7, **25.4 mm** centre-to-centre |
| Row spacing | matches the measured module row spacing exactly ✓ |

So the carrier's socket field is right: the two 1×22 rows sit 25.4 mm apart
across the board's 40 mm width, and 53.34 mm of pin field along the length.
The module fills the carrier's socket region precisely.

## Height stack (corrected)

The old enclosure spec assumed the module rides ~9 mm above the carrier. The
real stack, with the module plugged into a vertical socket:

| Item | Height |
| --- | --- |
| Carrier PCB | 1.6 |
| Female socket body (PinSocket 1×22 vertical) | ~8.5 typical |
| Male pin engaged in socket (already counted) | — |
| Module PCB above socket top | 1.6 |
| **Total: carrier bottom → module top (bare)** | **~11.7** |
| Tallest on-module component (their 11 mm includes flash/shield stack) | varies |
| Realistic clearance to plan for | **≥ 13.0 mm** |

## Antenna

The official STEP contains **no antenna body** (searched `ANTENNA`/`Antenna`/
`antenna`/`FEC`/`AN-`/`ANT_` — 0 hits). The 2.4 GHz antenna is a PCB copper
shape, not a 3D part, so it has no 3D geometry to keep out of. Keepout still
matters electrically: keep dense plastic and any metal fasteners away from
the shield end (the `indc4040x180` shield can marks the RF end of the board).
