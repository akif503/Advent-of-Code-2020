# Inspired from geohotz's solution
# This is a much better way to solve this problem, and keeps up with the essence of the problem as well.
# Here, from our dp solution one fact can be discerned that a string matching a rule has always the same 
# length regardless. This fact could also probably be shown mathematically. 
# Here, we solve this problem by using this fact recursively. 
# Firstly, we try to match certain length of a string with the sub-rule of a rule; if the sub-rule matches
# then then it will have to consume some length of the string. So, it returns the length that it consumes.
# We use that length to increment the offset index and recur for the adjoining sub rule with the rest of the message
# starting from that offset index - msg[idx:]. If any of the sub rule does not match it will return -1 and we will
# break out of the loop. If there is another option for a that rule to match we do the same steps for the 
# sub rule of the option by starting the offset from 0.

import re

def main():
    global rules
    inp_f = "19.txt"

    data = open(inp_f, "r").read().rstrip()

    raw_rules, msgs = data.split('\n\n')

    rules = {}
    for line in raw_rules.split('\n'):
        rule, strt = line.split(': ')
        rules[rule] = strt

    result = 0
    for msg in msgs.split('\n'):
        if consume(msg, str(0)) == len(msg):
            result += 1
    
    print(result)

def consume(msg, rule):
    global rules

    if rules[rule][0] == '"':
        if msg[0] == rules[rule].strip('"'):
            return 1
        else:
            return -1

    for opt in rules[rule].split(' | '):
        idx = 0
        for sub_rule in opt.split(' '):
            if (w := consume(msg[idx:], sub_rule)) == -1:
                idx = -1
                break

            idx += w

        if idx != -1:
            return idx

    return -1

main()
