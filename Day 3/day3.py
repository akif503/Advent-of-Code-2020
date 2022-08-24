import time 

# Input
data = open("input.txt", "r")
grid = []

for row in data.read().split("\n"):
    if row != "":
        grid.append(row)


def part1():

    no_of_cols = len(grid[0])
    no_of_rows = len(grid)

    x, y = 0, 0

    trees = 0
    while y < no_of_rows:
        if grid[y][x] == "#":
            trees += 1

        x = (x + 3) % no_of_cols
        y = y + 1

    with open("out1.txt", "w") as out:
        out.write(f"{trees}\n")


def part2():
    global grid

    # Slopes
    # Right 1, down 1.
    # Right 3, down 1.
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    no_of_cols = len(grid[0])
    no_of_rows = len(grid)

    result = 1

    for slope in slopes:
        x, y = 0, 0

        trees = 0
        while y < no_of_rows:
            if grid[y][x] == "#":
                trees += 1

            x = (x + slope[0]) % no_of_cols
            y = y + slope[1]

        result *= trees

    with open("out2.txt", "w") as out:
        out.write(f"{result}\n")

