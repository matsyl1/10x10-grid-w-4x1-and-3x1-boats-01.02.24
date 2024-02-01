# 10x10 grid with two non-intersecting boats (4x1 and 3x1)

# import
import random
import numpy as np

# original grid
grid = np.full([10,10], ".", dtype=str)

# 4x1 boat - first random coord.
x1 = random.randint(0,9)
y1 = random.randint(0,9)
grid[y1, x1] = "1"

    # Same axis test
def same_axis (coord1, coord2, coord3, coord4):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    x4, y4 = coord4
    return (x1==x2==x3==x4) or (y1==y2==y3==y4)

    # adjacent condition for coord1 and coord2
def adjacent_12 (coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2) == 1

    # adjacent condition for coord1 and coord3
def adjacent_13 (coord1, coord3):
    x1, y1 = coord1
    x3, y3 = coord3
    return abs(x1-x3) + abs(y1-y3) == 2

    # adjacent condition for coord2 and coord3
def adjacent_23 (coord2, coord3):
    x2, y2 = coord2
    x3, y3 = coord3
    return abs(x2-x3) + abs(y2-y3) == 1

    # adjacent condition for coord1 and coord4
def adjacent_14 (coord1, coord4):
    x1, y1 = coord1
    x4, y4 = coord4
    return abs(x1-x4) + abs(y1-y4) == 3

    # adjacent condition for coord2 and coord4
def adjacent_24 (coord2, coord4):
    x2, y2 = coord2
    x4, y4 = coord4
    return abs(x2-x4) + abs(y2-y4) == 2

while True:
    x2 = random.randint(0,9)
    y2 = random.randint(0,9)
    x3 = random.randint(0, 9)
    y3 = random.randint(0, 9)
    x4 = random.randint(0, 9)
    y4 = random.randint(0, 9)
    if adjacent_12((x1,y1),(x2,y2)) and adjacent_13((x1,y1),(x3,y3)) and adjacent_23((x2,y2),(x3,y3)) and adjacent_14((x1,y1),(x4,y4)) and adjacent_24((x2,y2), (x4, y4)) and ((x1==x2==x3==x4) or (y1==y2==y3==y4)):
        grid[y2, x2] = "2"
        grid[y3, x3] = "3"
        grid[y4, x4] = "4"
        print(grid)
        break

print(f"Start: ({x1}, {y1}) and trying: ({x2}, {y2}), ({x3}, {y3}), ({x4}, {y4})")