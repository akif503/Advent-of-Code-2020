from collections import defaultdict

# Take input
data = open("input.txt", "r").read()

jolts = []
exists = defaultdict(bool)

for jolt in data.split("\n"):
    if jolt != "":
        jolts.append(int(jolt))
        exists[int(jolt)] = True


def part1():
    global jolts
    jolts = sorted(jolts)

    differences = defaultdict(int)

    for index in range(1, len(jolts)):
        prev_jolt = jolts[index-1]
        cur_jolt = jolts[index]

        differences[cur_jolt - prev_jolt] += 1

    print((differences[1] + 1) * (differences[3] + 1))

def backtrack(jolt):
    global exists, default_jolt, memoize
    
    if jolt == default_jolt:
        return (True, 1)

    else:
        connectable = False
        distinct_arg = 0
        for next_jolt in range(jolt + 1, jolt + 4):
            if exists[next_jolt]:
                if memoize[next_jolt][0] == None:
                    memoize[next_jolt] = backtrack(next_jolt)

                flag, sub_solvable_branches = memoize[next_jolt]
                connectable = connectable or flag
                distinct_arg += sub_solvable_branches

        return (connectable, distinct_arg)

def part2():
    global jolts, memoize, default_jolt

    default_jolt = max(jolts) + 3
    exists[default_jolt] = True

    memoize = defaultdict(lambda : (None, 0))
    _, distinct_args = backtrack(0)

    print(distinct_args)

part1()
part2()