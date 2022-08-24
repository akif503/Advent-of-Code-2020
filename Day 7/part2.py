import re
from collections import defaultdict


# - - bags contain (N - - bags? |no\sother\sbags)+


data1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

data = open("input.txt", "r").read()

data = [x for x in data.split("\n") if x != ""]

types_of_bag = []
bag_to_bags = {}
root_bags = []

# Map the strings to integers
bag_to_node = {}

# Parse the data
for line in data:
    containing_bag = re.findall(r"(\w+\s\w+)\sbags?\s*c", line)[0]
    types_of_bag.append(containing_bag)

    # Convert it to integer node 
    bag_to_node[containing_bag] = len(types_of_bag) - 1

    # inner bags
    inner_bags = re.findall(r"(?:(\d+)\s(\w+\s\w+))\sbags?", line)

    # Containers -> inner bags
    bag_to_bags[containing_bag] = inner_bags

    # The bags that doesn't contain other bags
    if len(inner_bags) == 0:
        root_bags.append(containing_bag)

        
node_to_nodes = defaultdict(list)

# Convert bags_to_bags to nodes_to_node
for bag in types_of_bag: 
    for inner_bag in bag_to_bags[bag]:
        node_to_nodes[bag_to_node[bag]].append((int(inner_bag[0]), bag_to_node[inner_bag[1]]))

# No of inner nodes
no_of_inner_nodes = defaultdict(int)

# Known nodes
known_nodes = [bag_to_node[x] for x in root_bags]

while len(known_nodes) < len(types_of_bag):

    # Loops through all the bags
    for bag in types_of_bag:
        # Convert the bag to node 
        con_node = bag_to_node[bag]

        # If we don't know the result for that node (bag)
        if con_node not in known_nodes:
            inner_nodes = node_to_nodes[con_node]

            add = 0
            # Loop through all the inner_nodes and see if they are known or not
            for no_of_nodes, node in inner_nodes:
                if node not in known_nodes:
                    add = 0
                    break
                
                add += (no_of_nodes * (no_of_inner_nodes[node] + 1))
            
            no_of_inner_nodes[con_node] += add

            # This means we didn't know all the inner_nodes of that container
            if add != 0:
                known_nodes.append(con_node)
        
print(no_of_inner_nodes[bag_to_node['shiny gold']])
