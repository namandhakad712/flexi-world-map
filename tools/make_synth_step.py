#!/usr/bin/env python3
"""Build a synthetic STEP file that models the Lume Wedge spec exactly,
so verify_step.py can be proven to pass on good geometry."""

import math, sys

def pt(name, xyz):
    return f"CARTESIAN_POINT('{name}',({xyz[0]},{xyz[1]},{xyz[2]}))"

# Wedge corners: width 56 (x), depth 71 (y), front wall 8 tall, slope 96 long
# at 45deg rising from (0,0,8) to (0,67.9,75.9).
corners = [
    (0,0,0),(56,0,0),(56,71,0),(0,71,0),
    (0,0,8),(56,0,8),
    (0,67.9,75.9),(56,67.9,75.9),
]
pts = [f"#{i+1}=CARTESIAN_POINT('v{i}',({c[0]},{c[1]},{c[2]}))" for i, c in enumerate(corners)]

# 4 mount holes on the tilted board plane. Board XY (4,4),(81,4),(4,36),(81,36),
# s = 6 + bx along the slope. 8mm perpendicular offset at 45deg -> dy=-5.657, dz=+5.657.
# Emitted in real STEP form: #N=CARTESIAN_POINT(...); #M=CIRCLE('',#N,r);
lines = []
pid = 100
for n,(bx,by) in enumerate([(4,4),(81,4),(4,36),(81,36)]):
    s = 6.0 + bx
    y = s*math.cos(math.radians(45)) - 5.657
    z = 8.0 + s*math.sin(math.radians(45)) + 5.657
    pid += 1
    pts.append(f"#{pid}=CARTESIAN_POINT('h{n}',({by},{y},{z}))")
    lines.append(f"#{pid+50}=CIRCLE('h{n}',#{pid},1.6)")   # r = D/2

body = ";\n".join(pts) + ";\n" + ";\n".join(lines) + ";"
sys.stdout.write("ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\n" + body + "\nENDSEC;\nEND-ISO-10303-21;\n")
