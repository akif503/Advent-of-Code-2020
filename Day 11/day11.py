import pprint
from collections import defaultdict
import re

data = open("input.txt", "r").read()

data1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

# data = data1 

grid = []

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

for row in data.split("\n"):
    if row != "":
        grid.append(list(row))

def count_occupied_seats():
    global grid
    occupied_seats, unoccupied_seats = 0, 0
    for row in grid:
        occupied_seats += len(re.findall(r"#", "".join(row)))
        unoccupied_seats += len(re.findall(r"L", "".join(row)))

    return occupied_seats, unoccupied_seats

def update():
    global grid
    new_grid = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell is not FLOOR:
                # Count the number of occupied seats
                curr_occ = 0
                left = 8
                for xc in [-1, 0, 1]:
                    for yc in [-1, 0, 1]:
                        # If in range
                        nx = x + xc
                        ny = y + yc

                        if 0 <= nx < len(row) and 0 <= ny < len(grid) and not (xc == 0 and yc == 0):
                            if grid[ny][nx] == OCCUPIED:
                                curr_occ += 1

                        left -= 1

                if cell == EMPTY and curr_occ == 0:
                    new_grid[y][x] = OCCUPIED

                elif cell == OCCUPIED and curr_occ >= 4:
                    new_grid[y][x] = EMPTY

                else:
                    new_grid[y][x] = grid[y][x]

    grid = new_grid


def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def part1():
    prev_occ, _ = count_occupied_seats()
    while True:
        update()
        cur_occ, _ = count_occupied_seats()

        if prev_occ == cur_occ:
            break

        prev_occ = cur_occ

    print(prev_occ)

    
def find_offset(diag_id, r, c):
    # diag_id: PDiag -> 1
    #        : SDiag -> -1

    return r - (diag_id * c)


def update2():
    global grid

    # Reformulation
    s_rows = defaultdict(list)
    s_cols = defaultdict(list)

    sp_diags = defaultdict(list)
    ss_diags = defaultdict(list)

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == OCCUPIED:
                # Rows
                s_rows[r].append(c)
                # Cols
                s_cols[c].append(r)
                # Primary Diags
                offset = find_offset(1, r, c)
                sp_diags[offset].append((r,c))
                # Secondary Diags 
                offset = find_offset(-1, r, c)
                ss_diags[offset].append((r,c))
                
                
    new_grid = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]

    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell is not FLOOR:
                # Count the number of occupied seats
                curr_occ = 0

                # New update rule
                # Is there an element which is less than c (for row)
                for c in s_rows[y]:
                    if c > x:
                        break

                    if c < x:
                        curr_occ += 1
                        break

                for c in reversed(s_rows[y]):
                    if c < x:
                        break 

                    if c > x:
                        curr_occ += 1
                        break
                    
                for r in s_cols[x]:
                    if r > y:
                        break 

                    if r < y:
                        curr_occ += 1
                        break
                
                for r in reversed(s_cols[x]):
                    if r < y:
                        break 

                    if r > y:
                        curr_occ += 1
                        break


                for pd in sp_diags[find_offset(1, y, x)]:
                    if pd[0] > y and pd[1] > x:
                        break 

                    if pd[0] < y and pd[1] < x:
                        curr_occ += 1
                        break


                for pd in reversed(sp_diags[find_offset(1, y, x)]):
                    if pd[0] < y and pd[1] < x:
                        break

                    if pd[0] > y and pd[1] > x:
                        curr_occ += 1
                        break

                    
                # Left of the cell
                for pd in ss_diags[find_offset(-1, y, x)]:
                    # if (y,x) == (2,7):
                    #    print(pd, "OK")

                    if pd[0] > y and pd[1] < x:
                        curr_occ += 1
                        break

                
                # Right of the cell
                for pd in reversed(ss_diags[find_offset(-1, y, x)]):
                    if pd[0] < y and pd[1] > x:
                        curr_occ += 1
                        break

                if (y,x) == (0,3):
                    # print(ss_diags[find_offset(-1, y, x)])
                    print((y,x), curr_occ)

                
                if cell == EMPTY and curr_occ == 0:
                    new_grid[y][x] = OCCUPIED

                elif cell == OCCUPIED and curr_occ >= 5:
                    new_grid[y][x] = EMPTY

                else:
                    new_grid[y][x] = grid[y][x]

    grid = new_grid

def update3():
    global grid
    new_grid = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell is not FLOOR:
                # Count the number of occupied seats
                curr_occ = 0
                left = 8
                for xc in [-1, 0, 1]:
                    for yc in [-1, 0, 1]:
                        # If in range
                        nx = x + xc
                        ny = y + yc

                        if not (xc == 0 and yc == 0):
                            while 0 <= nx < len(row) and 0 <= ny < len(grid):
                                if grid[ny][nx] == OCCUPIED:
                                    curr_occ += 1
                                    break

                                if grid[ny][nx] == EMPTY:
                                    break

                                nx = nx + xc
                                ny = ny + yc
                        
                        left -= 1

                if cell == EMPTY and curr_occ == 0:
                    new_grid[y][x] = OCCUPIED

                elif cell == OCCUPIED and curr_occ >= 5:
                    new_grid[y][x] = EMPTY

                else:
                    new_grid[y][x] = grid[y][x]

    grid = new_grid

    
def part():

    update3()
    print_grid(grid)
    print("NEXT")
    update3()
    print_grid(grid)
    print("NEXT")
    update3()
    print_grid(grid)

def part2():
    prev_occ, _ = count_occupied_seats()
    while True:
        update3()
        cur_occ, _ = count_occupied_seats()

        if prev_occ == cur_occ:
            break

        prev_occ = cur_occ

    print(prev_occ)
    
part2()