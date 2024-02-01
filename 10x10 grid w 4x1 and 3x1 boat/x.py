# 10x10 grid with two randomly placed non-intersecting boats (4x1 and 3x1)

# import
import random
import numpy as np

# original grid
grid = np.full([10,10], ".", dtype=str)

# 4x1: first random coord.
x1 = random.randint(0,9)
y1 = random.randint(0,9)
grid[y1, x1] = "4"

# same axis test
def same_axis (coord1, coord2, coord3, coord4):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    x4, y4 = coord4
    return (x1==x2==x3==x4) or (y1==y2==y3==y4)
# adjacent test for coord1 and coord2
def adjacent_12 (coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2) == 1
# adjacent test for coord1 and coord3
def adjacent_13 (coord1, coord3):
    x1, y1 = coord1
    x3, y3 = coord3
    return abs(x1-x3) + abs(y1-y3) == 2
# adjacent test for coord2 and coord3
def adjacent_23 (coord2, coord3):
    x2, y2 = coord2
    x3, y3 = coord3
    return abs(x2-x3) + abs(y2-y3) == 1
# adjacent test for coord1 and coord4
def adjacent_14 (coord1, coord4):
    x1, y1 = coord1
    x4, y4 = coord4
    return abs(x1-x4) + abs(y1-y4) == 3
# adjacent test for coord2 and coord4
def adjacent_24 (coord2, coord4):
    x2, y2 = coord2
    x4, y4 = coord4
    return abs(x2-x4) + abs(y2-y4) == 2
# loop to place random coords to satisfy tests
while True:
    x2 = random.randint(0,9)
    y2 = random.randint(0,9)
    x3 = random.randint(0, 9)
    y3 = random.randint(0, 9)
    x4 = random.randint(0, 9)
    y4 = random.randint(0, 9)
    if adjacent_12((x1,y1),(x2,y2)) and adjacent_13((x1,y1),(x3,y3)) and adjacent_23((x2,y2),(x3,y3)) and adjacent_14((x1,y1),(x4,y4)) and adjacent_24((x2,y2), (x4, y4)) and ((x1==x2==x3==x4) or (y1==y2==y3==y4)):
        grid[y2, x2] = "4"
        grid[y3, x3] = "4"
        grid[y4, x4] = "4"
        # print(grid)
        break

# set to keep track of already used up coords by 4x1 boat
used_coord = {(x1,y1), (x2, y2), (x3, y3), (x4,y4)}

# 3x1: first random coord.
x1 = random.randint(0,4)
y1 = random.randint(0,4)
grid[y1, x1] = "3"

# check for non-intersection between 4x1 and 3x1
def non_intersect (coord1, coord2, coord3, used_coord):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    return (x1,y1) not in used_coord and (x2,y2) not in used_coord and (x3,y3) not in used_coord
# same axis test
def same_axis (coord1, coord2, coord3):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    return (x1==x2==x3) or (y1==y2==y3)
# adjacent test for coord1 and coord2
def adjacent_12 (coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2) == 1
# adjacent test for coord1 and coord3
def adjacent_13 (coord1, coord3):
    x1, y1 = coord1
    x3, y3 = coord3
    return abs(x1-x3) + abs(y1-y3) == 2
# adjacent test for coord2 and coord2
def adjacent_23 (coord2, coord3):
    x2, y2 = coord2
    x3, y3 = coord3
    return abs(x2-x3) + abs(y2-y3) == 1
# loop to place random coords to satisfy tests
while True:
    x2 = random.randint(0,9)
    y2 = random.randint(0,9)
    x3 = random.randint(0, 9)
    y3 = random.randint(0, 9)
    if adjacent_12((x1,y1),(x2,y2)) and adjacent_13((x1,y1),(x3,y3)) and adjacent_23((x2,y2),(x3,y3)) and non_intersect((x1,y1), (x2, y2), (x3, y3), used_coord) and same_axis((x1, y1), (x2, y2), (x3, y3)):
        grid[y2, x2] = "3"
        grid[y3, x3] = "3"
        print(grid)
        break
