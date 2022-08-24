import re 
from collections import defaultdict, deque
import time

class Tile:
    def __init__(self, tile_id, rows):
        self.id = tile_id
        self.rows = [list(row) for row in rows]
        self.cols = self.create_transpose(self.rows)

        self.no_rows = len(self.rows)
        self.no_cols = len(self.cols)

        # top, left, bottom, right
        self.borders = [self.rows[0], self.cols[0], self.rows[-1], self.cols[-1]]


    def create_transpose(self, axis):
        t_axis = [[] for _ in range(len(axis[0]))]
        for vector in axis:
            for j, pixel in enumerate(vector):
                t_axis[j].append(pixel)
        
        return t_axis
    
    def show(self):
        for r, row in enumerate(self.rows):
            for i in range(10, len(row)+1, 10):
                print("".join(row[i-10:i]), end="    ")
                    
            if r % 10 == 9 and r != 0:
                print('')
            print()
    
    def rotate(self, side=1):

        # right rotation
        if side == 1:
            for i, _ in enumerate(self.rows):
                self.rows[i] = self.cols[i][::-1]
            
            self.cols = self.create_transpose(self.rows)

        # left rotation 
        else:
            for i, _ in enumerate(self.cols):
                self.cols[i] = self.rows[i][::-1]
            
            self.rows = self.create_transpose(self.cols)

    def flip(self, side=0):
        # 0 -> Horizontal
        # 1 -> Vertical

        if side == 0:
            for i in range(self.no_cols // 2):
                self.cols[i], self.cols[-i-1] = self.cols[-i-1], self.cols[i]
    
            self.rows = self.create_transpose(self.cols)

        if side == 1:
            for i in range(self.no_rows // 2):
                self.rows[i], self.rows[-i-1] = self.rows[-i-1], self.rows[i]
            
            self.cols = self.create_transpose(self.rows)
        
    def get_id(self):
        return self.id

    def get_borders(self):
        return [self.rows[0], self.cols[0], self.rows[-1], self.cols[-1]]


def main():
    filename = '20.txt'
    # filename = 'ex.txt'
    data = open(filename, "r").read()

    raw_tiles = data.split("\n\n")

    tiles = []
    id_to_tile = {}
    for tile in raw_tiles:
        if tile:
            lines = [line for line in tile.split("\n") if line]

            tile_id = int(re.findall(r"(\d+)", lines[0])[0])

            tile_obj = Tile(tile_id, lines[1:])
            tiles.append(tile_obj)
            id_to_tile[tile_id] = tile_obj
    
    mp = {
        0: 'T',
        1: 'L',
        2: 'B',
        3: 'R'
    }

    result = 1
    neighbors = defaultdict(list)


    for tile1 in tiles:
        matched = []
        for tile2 in tiles:
            if tile1.get_id() != tile2.get_id():
                for border1 in tile1.get_borders():
                    border1 = "".join(border1)

                    for border2 in tile2.get_borders():
                        border2 = "".join(border2)
                        if border1 == border2 or border1 == border2[::-1]:

                            neighbors[tile1.get_id()].append(tile2.get_id())

                            matched.append(tile2.get_id())

        if len(matched) == 2:
            result *= tile1.get_id()
    
    # print(result)

    # (r,c) -> tile_id
    # init_tile = tiles[0]
    init_tile = id_to_tile[1171]
    grid = {(0, 0): init_tile.get_id()}
    opposite_grid = {
        init_tile.get_id(): (0, 0)
    }

    selected = defaultdict(bool)
    selected[init_tile.get_id()] = True

    queue = deque()
    queue.append(init_tile)

    while len(queue) > 0:
        tile1 = queue.popleft()

        tile1_id = tile1.get_id()
        print(tile1_id)

        for tile2_id in neighbors[tile1_id]:

            r, c = opposite_grid[tile1_id]
            if not selected[tile2_id]:
                tile2 = id_to_tile[tile2_id]

                matched = False
                for side in mp.values():
                    if matched:
                        print('Ok', tile2_id)
                        break 

                    if side == 'T':
                        for _ in range(4):
                            tile2.rotate()

                            if (m := tile1.rows[0] == tile2.rows[-1][::-1]) or tile1.rows[0] == tile2.rows[-1]:
                                if m:
                                    tile2.flip()

                                r -= 1
                                matched = True
                                break
                    
                    elif side == 'B':
                        for _ in range(4):
                            tile2.rotate()

                            if (m := tile1.rows[-1] == tile2.rows[0][::-1]) or tile1.rows[-1] == tile2.rows[0]:
                                if m:
                                    tile2.flip()

                                r += 1

                                matched = True
                                break

                    
                    elif side == 'L':
                        for _ in range(4):
                            tile2.rotate()

                            if (m := tile1.cols[0] == tile2.cols[-1][::-1]) or tile1.cols[0] == tile2.cols[-1]:
                                if m:
                                    tile2.flip()
                                    
                                c -= 1

                                matched = True
                                break
                    
                    elif side == 'R':
                        for _ in range(4):
                            tile2.rotate()
                            
                            if (m := tile1.cols[-1] == tile2.cols[0][::-1]) or tile1.cols[-1] == tile2.cols[0]:
                                if m:
                                    tile2.flip()
                    
                                c += 1
                                
                                matched = True
                                break
                    
                grid[(r,c)] = tile2_id
                opposite_grid[tile2_id] = (r,c)
                queue.append(tile2)
                selected[tile2_id] = True
                # time.sleep(5)


    create_picture(grid, id_to_tile)
    

def create_picture(grid, id_to_tile):
    top = min([r for r, _ in grid.keys()])
    bottom = max([r for r, _ in grid.keys()])

    left = min([c for _, c in grid.keys()])
    right = max([c for _, c in grid.keys()])
    
    picture_ids = []
    for r in range(top, bottom + 1):
        row = []
        for c in range(left, right + 1):
            pos = (r, c)
            row.append(grid[pos])
        
        picture_ids.append(row)
        
    picture = [['' for _ in range(10 * len(picture_ids[0]))] for _ in range(10 * len(picture_ids))]
    
    for Tr, row in enumerate(picture_ids):
        for Tc, tile_id in enumerate(row):
            tile_grid = id_to_tile[tile_id].rows
            pp = ""
            for row in tile_grid:
                pp += "".join(row) + '\n'
                
            # print(tile_id, '\n', pp)

            for Sr, tile_row in enumerate(tile_grid):
                for Sc, pixel in enumerate(tile_row):
                    picture[10*Tr+Sr][10*Tc+Sc] = pixel

                    
    actual_picture = []

    for row in picture[1:-1]:
        actual_picture.append(row[1:-1])

    picture = Tile(None, picture)
    #picture.flip(1)
    picture.show()

    print(picture_ids)


    
main()
