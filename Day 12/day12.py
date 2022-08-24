import re
from math import cos, sin, pi
import numpy as np
from functools import reduce

data = open("12.txt", "r").read()

moves = []
for line in data.split('\n'):
    if line != "":
        direction, val = re.findall(r"^(\w)(\d+)$", line)[0]

        moves.append((direction, int(val)))

direction = {
    'N': [0, 1],
    'S': [0, -1],
    'E': [1, 0],
    'W': [-1, 0]
}


def convert_to_rad(degree):
    return degree * pi / 180

def part1():
    # In polar coords
    heading = 0
    # [East, North]
    position = [0, 0]

    for move in moves:
        move_dir, move_val = move

        if move_dir in 'NEWS':
            position = [position[x] + move_val * direction[move_dir][x] for x in range(2)]

        if move_dir in 'FLR':
            if move_dir == 'F':
                position = [position[0] + move_val * cos(heading * pi / 180), position[1] + move_val * sin(heading * pi / 180)]

            if move_dir == 'L':
                heading = (heading + move_val) % 360
            
            if move_dir == 'R':
                heading = (heading - move_val) % 360

    print(sum([abs(p) for p in position]))

def part2():

    ship = Ship()
    for move in moves:
        ship.move(*move)

    print(ship.manhattan_dist())

# Wanted to refactor the code to use class for the second part; Now, it's trivial to refactor the 1st part using 
# this class as well by just adding another method moving in the class
class Ship:
    # Dependencies math -> cos, sin, pi
    #              functools -> reduce

    def __init__(self):
        self.heading = 0
        self.waypoint = [10, 1]

        self.position = [0, 0]

        self.dir_map = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        
        self.convert_to_rad = lambda degree: degree * pi / 180

    def move(self, direction, magnitude):
        if direction in 'NEWS':
            # waypoint = waypoint + magnitude * dir_map[direction] // Could've done it better with numpy
            self.waypoint = list(map(sum, zip(self.waypoint, map(lambda m: magnitude * m, self.dir_map[direction]))))
        
        elif direction in 'FLR':
            if direction == 'F':
                # position = position + magnitude * waypoint
                self.position = list(map(sum, zip(self.position, map(lambda v: v * magnitude, self.waypoint))))

            else:
                self.heading = magnitude if direction == 'L' else (-1) * magnitude
                self.heading = self.convert_to_rad(self.heading)

                # The maps are for rounding the values to 10 decimal places to shave of precision error
                # Conversely you could also use int because all the rotation are multiple of 90
                rotation_matrix = np.array(list(map(lambda r: list(map(lambda v: round(v, 10), r)), 
                                  [[cos(self.heading), -sin(self.heading)], [sin(self.heading), cos(self.heading)]])), 
                                  dtype=np.float32)

                # If the rotation of waypoint wasn't multiples of 90 then use float to map
                self.waypoint = list(map(int, np.matmul(rotation_matrix, np.asarray(self.waypoint).reshape(2,1))))

    def manhattan_dist(self):
        return reduce(lambda acc, p: acc + abs(p), self.position, 0)


part2()