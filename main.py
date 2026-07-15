import numpy as np

# Rectangle geometry bounds
x_min, x_max = 0.0, 10.0
y_min, y_max = 10.0, 20.0

# Resolution
nx, ny = 10, 20   # nodes along x and y

# Node coordinates stored as 2D arrays, indexed [i][j]
X = np.zeros((nx, ny))
Y = np.zeros((nx, ny))

for i in range(nx):
    for j in range(ny):
        X[i, j] = x_min + (x_max - x_min) * i / (nx - 1)
        Y[i, j] = y_min + (y_max - y_min) * j / (ny - 1)

# Cell connectivity: each cell defined by 4 node index-pairs (i,j)
# cell(i,j) uses nodes (i,j), (i+1,j), (i+1,j+1), (i,j+1)
cells = []
for i in range(nx - 1):
    for j in range(ny - 1):
        cell = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
        cells.append(cell)

print("Grid shape (X):", X.shape)
print("Grid shape (Y):", Y.shape)
print("Number of cells:", len(cells))
print("Sample node (0,0):", (X[0, 0], Y[0, 0]))
print("Sample cell (0,0):", cells[0])
