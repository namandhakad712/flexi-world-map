# Shell model — the corrected Wedge A structure

`tools/check_pocket.py` caught a real flaw in the first geometry draft:
a wedge with a **closed back wall** cannot hold a 30.6 mm pocket cut into a
45° slope. With a 71 mm-deep base, the back wall intrudes into the pocket
by about 4 mm in the module zone, which would have been a broken print.

The corrected model is the one the reference stand actually uses: an
**open-rear shell**.

## Structure

```
        slope face (45deg)
       /
      /   display panel beds into a 3mm pocket here
     /
    +-------------------------+
    |  front wall, 8mm tall   |   <- USB-C slot cut here (s 0..8)
    +-------------------------+   floor: 2mm, closed
    |                         |
    |   cavity, open at rear  |   module sits here on 4 bosses,
    |   (no back wall)        |   antenna end points up and out
    |                         |
    +-------------------------+   rear: fully open
```

- **Closed surfaces:** floor (2 mm), two side walls (2 mm), front wall (8 mm)
  with the USB-C slot, and the sloped face around the display pocket.
- **Open surface:** the whole rear. The module's component side faces it.
- **Rear cover** (part 3): a separate panel parallel to the board, 17 mm
  behind the board plane, screwing into 2 small posts on the rim. This is
  what closes the box. It carries the button holes and the antenna window.

## Why open-rear is right (three reasons)

1. **It fits.** A closed back wall would have to be ≥ 30.6 mm deep
   perpendicular to a 45° slope at the module span; the geometry simply does
   not close in a 71 mm-deep wedge.
2. **It is what the reference does.** The CYD stand and nearly every small
   display stand is a front shell plus a rear cover panel.
3. **It is honest about the antenna.** The module's component side faces the
   removable cover, so the antenna region sits behind a thin, single-wall
   panel with a window — not buried inside a solid wedge.

## Pocket depths (perpendicular to the slope face)

| Zone | Slope span (s) | Depth | Contents |
| --- | --- | --- | --- |
| Display lip | 4 → 6 | 3.0 | panel + 0.9 lip recess |
| Board + panel | 6 → 21.8 | 12.6 | 3 + 8 gap + 1.6 board |
| Module | 21.8 → 75.2 | **30.6** | + module envelope 13 + slack |
| Board top | 75.2 → 91 | 12.6 | rest of the board |

Verified by `tools/check_pocket.py`: the pocket floor stays ≥ 3.33 mm above
the outer bottom everywhere, above the 2.0 mm minimum wall.
