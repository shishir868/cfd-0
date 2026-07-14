import numpy, scipy, random

# Rectangle geometry: defined by 4 corner nodes
x_min, x_max = 0.0, 10.0
y_min, y_max = 10.0, 20.0

nodes = [
    (x_min, y_min),  # bottom-left
    (x_max, y_min),  # bottom-right
    (x_max, y_max),  # top-right
    (x_min, y_max),  # top-left
]

cells = [0, 1, 2, 3]  # single cell/loop referencing the 4 corner nodes, in order

print(nodes, cells)