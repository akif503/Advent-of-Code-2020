# The logic of finding the ing_allg_map can be done with maximum bipartite matching
import re
from collections import deque, defaultdict
from pprint import pprint

data = open("21.txt", "r").read()

data1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

#data = data1

possible_allg_in_ings = {}
all_ings = []
for line in data.strip().splitlines():
    ing, allgs = re.search(r"(.+) \(contains (.+)\)", line).groups()

    ings = ing.split(' ')
    all_ings.extend(ings)
    for allg in allgs.split(', '):
        if possible_allg_in_ings.get(allg, None):
            possible_allg_in_ings[allg].intersection_update(ings)

        else:
            possible_allg_in_ings[allg] = set(ings)

times_occured = defaultdict(int)

for ing in all_ings:
    times_occured[ing] += 1

result = set(all_ings)

queue = deque([allg for allg in possible_allg_in_ings if len(possible_allg_in_ings[allg]) == 1])

ing_allg_map = {}

while len(queue) > 0:
    current_allg = queue.popleft()

    target_ing = possible_allg_in_ings.pop(current_allg).pop()

    ing_allg_map[target_ing] = current_allg

    result.remove(target_ing)

    for allg in possible_allg_in_ings:
        if target_ing in possible_allg_in_ings[allg]:
            possible_allg_in_ings[allg].remove(target_ing)

            if len(possible_allg_in_ings[allg]) == 1:
                if allg not in queue:
                    queue.append(allg)
    
print("Part 1: ", sum(map(lambda x: times_occured[x], result)))

cdl = sorted(ing_allg_map.items(), key = lambda x: x[1])
cdl = ",".join([x[0] for x in cdl])

print("Part 2: ", cdl)