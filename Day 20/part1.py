import re 
from collections import deque

class Tile:
    def __init__(self, tile_id, rows):
        self.id = tile_id
        self.rotation = 0 # -3,-2,-1, 0, 1, 2, 3
        self.flipped = False 

        self.rows = [row for row in rows]
        right = "".join([self.rows[i][-1] for i in range(len(rows))])
        left = "".join([self.rows[i][0] for i in range(len(rows))])

        # top, right, bottom, left
        # self.borders = [self.rows[0], right, self.rows[-1],  left]
        self.open_borders = {
            'T': self.rows[0],
            'B': self.rows[-1],
            'L': left,
            'R': right
        }
    
    def rotate(self, angle):
        pass
    
    def flip(self, axis):
        pass


def main():
    # filename = '20.txt'
    filename = 'ex.txt'
    data = open(filename, "r").read()

    raw_tiles = data.split("\n\n")

    tiles = {}
    for tile in raw_tiles:
        if tile:
            lines = [line for line in tile.split("\n") if line]

            tile_id = int(re.findall(r"(\d+)", lines[0])[0])

            tiles[tile_id] = Tile(tile_id, lines[1:])
    
    grid = {
        (0, 0): tiles[tile_id]
    }

    queue = deque(tiles.values())

    while len(queue) > 0:
        tile = queue.popleft()

        for loc, fixed_tile in grid.values():
            if (m := match_borders(fixed_tile, tile)):
                label1, label2, flipped = m

                joined = f"{label1}{label2}"

                if joined in ['TR', 'RB', 'LT', 'BL']:
                    # Rotate right
                    tile.rotation = 1
                    pass

                elif joined in ['TL', 'RT', 'LB', 'BR']:
                    # Rotate left
                    tile.rotation = -1
                    pass

                elif joined in ['TT', 'RR', 'LL', 'BB']:
                    # Rotate twice
                    tile.rotation = 2
                    pass


def match_borders(fixed_tile, tile):
    for label1, border1 in fixed_tile.open_borders.values():
        if border1:
            for label2, border2 in tile.open_borders.values():
                if border1 == border2:
                    # Which side of fixed tile, tile, and if flipped 
                    return (label1, label2, False)
                
                # Check for flipped match
                for idx in range(len(border1)):
                    if border1[idx] != border2[-idx-1]:
                        break
                else:
                    return (label1, label2, True)

    return None

main()