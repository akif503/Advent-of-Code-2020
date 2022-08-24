import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

dir_map = {
    #       x   y
    'ne': (-1, -2),
    'nw': (1, -2),
    'e': (-2, 0),
    'w': (2, 0),
    'se': (-1, 2),
    'sw': (1, 2)
}

def main():
    global dir_map

    filename = '24.txt'
    #filename = 'ex.txt'
    data = open(filename, "r").read().strip('\n')

    state = defaultdict(bool)

    for line in data.split('\n'):

        tile = (0, 0)

        idx = 0
        while idx < len(line):
            if line[idx] == 'e' or line[idx] == 'w':
                d = line[idx]
                idx += 1
            
            else:
                d = line[idx: idx+2]
                idx += 2

            tile = tuple(map(sum, zip(tile, dir_map[d])))
        
        state[tile] = not state[tile]

    result = sum(state.values())
    print("Part 1:", result)

    for tile in list(state.keys()):
        for d in dir_map:
            adj_tile = tuple(map(sum, zip(tile, dir_map[d])))

            _ = state[adj_tile]
    
    for _ in range(100):
        new_state = defaultdict(bool)

        for tile in list(state.keys()):
            blcks = 0

            for d in dir_map:
                adj_tile = tuple(map(sum, zip(tile, dir_map[d])))

                if state[adj_tile]:
                    blcks += 1
                
                _ = new_state[adj_tile]
            
            if state[tile] and (blcks == 0 or blcks > 2):
                new_state[tile] = False
            
            elif not state[tile] and blcks == 2:
                new_state[tile] = True

            else:
                new_state[tile] = state[tile]
        
        state = new_state

    print("Part 2:", sum(state.values()))


def draw_graph(state):
    global dir_map
    
    G = nx.Graph()

    for tile in list(state.keys()):
        G.add_node(tile)
        G.nodes[tile]['color'] = 'blue' if state[tile] else 'red'

        for d in dir_map:
            adj_tile = tuple(map(sum, zip(tile, dir_map[d])))

            G.add_edge(tile, adj_tile)
            G.nodes[adj_tile]['color'] = 'blue' if state[adj_tile] else 'red'

    color_map = [x[1]['color'] for x in G.nodes(data=True)]

    nx.draw(G, node_color=color_map)
    plt.show()


main()