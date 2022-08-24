from itertools import product, repeat
from collections import defaultdict

ACTIVE = 1
INACTIVE = 0

def main():
    global ACTIVE, INACTIVE
    data = open("17.txt", "r").read()

    # part1
    sol(data, 3)
    # part2
    sol(data, 4)

def find_no_neighboring_active_cubes(grid, cube, dim):
    active_n_cubes = 0
    for n_cube in product(*list([(cube[i]-1, cube[i], cube[i]+1) for i in range(dim)])):
        if n_cube != cube:
            active_n_cubes += grid[n_cube]
    
    return active_n_cubes

def next_state(cube_state, no_of_neighboring_active_cubes):
    global ACTIVE, INACTIVE
    # State change
    if cube_state == ACTIVE and (no_of_neighboring_active_cubes == 2 or no_of_neighboring_active_cubes == 3):
        return ACTIVE
    elif cube_state == INACTIVE and no_of_neighboring_active_cubes == 3:
        return ACTIVE

    return INACTIVE

def simulate(grid, cycles, dim):
    # Iterate through the 6 cycles
    for _ in range(cycles):
        cubes = list(grid.keys())
        next_grid = defaultdict(int)
        # Single cycle
        for cube in cubes:
            # Iterate through its neighbors

            active_n_cubes = find_no_neighboring_active_cubes(grid, cube, dim)

            next_grid[cube] = next_state(grid[cube], active_n_cubes)
            
            # Add the neighboring cells to the next_grid
            for n_cube in product(*list([(cube[i]-1, cube[i], cube[i]+1) for i in range(dim)])):
                if n_cube not in next_grid:
                    next_grid[n_cube] = INACTIVE
            
        grid = next_grid

    total_active = sum(grid.values())

    return total_active

    
def sol(data, dim):
    global ACTIVE, INACTIVE
    # (x,y,z) -> active/inactive
    grid = defaultdict(int)

    for y, line in enumerate(data.split('\n')):
        if line != "":
            for x, cube in enumerate(line):
                grid[(x,y,*[0 for _ in range(dim - 2)])] = ACTIVE if cube == "#" else INACTIVE
    
    max_x = max(grid, key=lambda t: t[0])[0]
    max_y = max(grid, key=lambda t: t[1])[1]

    # Add an outer layer
    for coord in product(range(-1, (max_x + 1) + 1), range(-1, (max_y + 1) + 1), *[range(-1, 2) for _ in range(dim - 2)]):
        if coord not in grid:
            grid[coord] = INACTIVE
    
    print(simulate(grid, 6, dim))

main()