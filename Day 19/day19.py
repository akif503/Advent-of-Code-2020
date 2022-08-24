import re
from collections import defaultdict
from itertools import product

def main():
    global rules, rule_set
    data = open("19.txt", "r").read()

    raw_rules, messages = data.split("\n\n")

    # Int -> a list of tuples
    rules = defaultdict(list)
    # Int -> string
    rule_set = defaultdict(list)
    enumerated_rules = []

    for rule in raw_rules.split('\n'):
        rule_no, rem = rule.split(': ')
        rule_no = rule_no.strip()

        if '|' in rem:
            parsed = [re.findall(r"(\d+)", x) for x in rem.split(" | ")]
            rules[rule_no].extend(map(tuple, parsed))

        else:
            if parsed := re.search(r"([a-z])", rem):
                rule_set[rule_no].append(parsed.group(1))
                enumerated_rules.append(rule_no)

            else:
                parsed = re.findall(r"(\d+)", rem)
                rules[rule_no].append(tuple(parsed))

    valid_messages = backtrack('0')

    result = 0
    for message in messages.rstrip('\n').split('\n'):
        if (message := message.strip()) in valid_messages:
            result += 1
    
    print(f"Part 1: {result}")

    result = 0
    for message in messages.split('\n'):

        l42 = len(rule_set['42'][0])
        l31 = len(rule_set['31'][0])

        i_31 = len(message)
        n_31 = 0
        while message[i_31 - l31 : i_31] in rule_set['31']:

            i_31 -= l31
            n_31 += 1
        
        idx = i_31
        n_42 = 0
        while message[idx - l42 : idx] in rule_set['42']:
            
            n_42 += 1
            idx -= l42
        
        if not (n_42 < n_31 or n_31 == 0 or idx != 0 or n_42 == n_31):
            result += 1
        
    print(f"Part 2: {result}")


def backtrack(rule):
    global rules, rule_set

    if rule in rule_set:
        return rule_set[rule]

    rule_strs = []
    for rule_option in rules[rule]:
        for sub_rule in rule_option:
            if sub_rule not in rule_set:
                rule_set[sub_rule] = backtrack(sub_rule)
                
        rule_strs.extend(["".join(x) for x in product(*[rule_set[sub_rule] for sub_rule in rule_option])])

    return rule_strs


main()