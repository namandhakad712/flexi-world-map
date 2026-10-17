# Week 2 Submission checklist

Theme: **CAD** — "Model something in CAD, then print or machine it."
Design week (Week 2). Build week is Week 7.

Deliverables per the Blueprint submission requirements.

## Hard requirements (missing any = auto-return)

- [ ] `README.md` contains:
  - [ ] description of what the project is
  - [ ] a couple sentences on **how to use** it
  - [ ] a couple sentences on **why** you made it
  - [ ] screenshot of the full 3D model
  - [ ] wiring diagram (N/A — everything is on the PCB)
  - [ ] BOM in a table with links
- [ ] `.STEP` file of the full assembly, in the repo
- [ ] Onshape **public link** in the README (source file requirement for OnShape)
- [ ] Source CAD files (Onshape document link)
- [ ] `bom.csv` in the **root directory**, CSV format, **with links**
- [ ] Original design — not a copy of the CYD desk buddy or any guide
- [ ] Sanity-checked with someone else
- [ ] No AI-generated README text (write in your own voice)
- [ ] Repository organized into folders

## BOM CSV note

The dashboard BOM is `BOM.md` (mirrored from Half Life). The submission also
needs `bom.csv` at the repo root — plan:

```
Part,Qty,Unit,Total,Link
PLA filament (black),1,3.00,3.00,
M3x10 SHCS,4,0.10,0.40,https://www.amazon.com/
M3 heat-set insert 5mm OD,4,0.15,0.60,https://www.amazon.com/
USB-C panel mount pigtail,1,2.00,2.00,https://amzn.eu/d/01LBdiyW
```

## Hours

Tier 1 = $30 grant for 10 hours. Filament + fasteners ≈ $6, so there's plenty
of headroom. Log the session hours on the dashboard — modeling + measuring +
verification count.

## Where things go

```
exports/
  lume-wedge-assembly.step     <- the STEP the reviewers want
  lume-wedge-base.stl
  lume-wedge-bezel.stl
  screenshots/
    full-assembly.png
    base.png
    bezel.png
cad/
  (Onshape export of the studio document, if any)
```
