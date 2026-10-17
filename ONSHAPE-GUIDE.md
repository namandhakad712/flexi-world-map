# Modeling a Part — the noob guide

How this project is being modeled in Onshape, block by block, the way a
person who has never opened a CAD program would actually do it: one
feature at a time, in an order that shows up on a timelapse as real work.

## Order of work

The reason for this order: every part below builds on the one before it,
and nothing gets modeled twice.

1. **Master sketch** — the board outline, the 4 M3 hole centres, drawn at
   1:1 in a single sketch. Everything later is dimensioned *to* this.
2. **Base** — extrude the block, cut the board cavity, cut the cable
   channel, add the 4 bosses.
3. **Bezel** — frame around the display, with the window cut and a
   thin lip the display beds onto.
4. **Assembly** — board + base + bezel mated. Interference check.
5. **Export** — STEP for the submission, STL for slicing.

## Good habits (learned the hard way in Week 1 with KiCad)

- **Dimension everything off the master sketch.** No typing a number into
  a dialog that was already in the sketch. Ref is the source of truth.
- **Name your features.** "Base cavity" not "Extrude 4". Six months from
  now you will not remember what Extrude 4 was.
- **One feature, one purpose.** If you find yourself wanting to sketch
  three separate things in one sketch, stop and split it.
- **Roll the timeline back** when something looks wrong instead of
  deleting forward.
- After each part: screenshot the part and the assembly. The submission
  needs screenshots of the full 3D model.
