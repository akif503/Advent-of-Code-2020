import re
from collections import defaultdict


# - - bags contain (N - - bags? |no\sother\sbags)+

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data = open("input.txt", "r").read()
data = [x for x in data.split("\n") if x != ""]

types_of_bag = []
bag_to_node = {}
bag_to_bags = {}

for line in data:
    containing_bag = re.findall(r"(\w+\s\w+)\sbags?\s*c", line)[0]
    types_of_bag.append(containing_bag)
    bag_to_node[containing_bag] = len(types_of_bag) - 1

    # inner bags
    inner_bags = re.findall(r"(?:(\d+)\s(\w+\s\w+))\sbags?", line)

    bag_to_bags[containing_bag] = inner_bags

# directed_edges[containing bag node][inner bag node] = (bool, number of that inner bags)
directed_edges = [[(False, 0) for x in range(len(types_of_bag))] for y in range(len(types_of_bag))]
node_to_nodes = defaultdict(list)

for bag in types_of_bag: 
    con_node = bag_to_node[bag]
    for inner_bag in bag_to_bags[bag]:
        no_of_bags = int(inner_bag[0])
        inner_node = bag_to_node[inner_bag[1]]
        directed_edges[con_node][inner_node] = (True, inner_node)
        node_to_nodes[con_node].append((no_of_bags, inner_node))


# DFS with memoization
reachable = [None for _ in range(len(types_of_bag))]
def backtrack(container_bag, target_bag):
    global directed_edges, node_to_nodes

    if len(node_to_nodes[container_bag]) == 0:
        return False
    
    for _, bag in node_to_nodes[container_bag]:
        if bag == target_bag:
            return True
        
        if reachable[bag] == None:
            reachable[bag] = backtrack(bag, target_bag)

        # If not reachable check the next node
        if reachable[bag]:
            return True

# Now repeatedly use dfs to see if you can reach the shiny bag
result = 0
for bag in types_of_bag:
    if reachable[bag_to_node[bag]] == None:
        reachable[bag_to_node[bag]] = backtrack(bag_to_node[bag], bag_to_node['shiny gold'])
    
    result = (result + 1) if reachable[bag_to_node[bag]] == True else result

print(result)
    