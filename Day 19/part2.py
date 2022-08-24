import re
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import pydot
import time

ll = 0
def main():
    global rules, ll, G

    inp_f = "19.txt"
    ex_f = "ex2.txt"

    data = open(ex_f, "r").read().rstrip()

    raw_rules, msgs = data.split('\n\n')

    rules = {}
    for line in raw_rules.split('\n'):
        rule, strt = line.split(': ')
        rules[rule] = strt
    
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    G = nx.DiGraph()

    result = 0
    for msg in msgs.split('\n')[1:2]:
        ll = len(msg)
        if (m := consume(msg, '0', 0)) == len(msg):
            result += 1
        
        print(m, len(msg))
    
    # same layout using matplotlib with no labels
    # pos=graphviz_layout(G, prog='dot')
    # nx.draw(G, pos, with_labels=True)
    # plt.show()
    print(result)

    
def consume(msg, rule, level):
    global rules,ll

    #print(rule)
    time.sleep(0.5)
    #print("-" * (len(msg)), '>', rule, level)
    if rules[rule][0] == '"':
        if msg[0] == rules[rule].strip('"'):
            return [1]
        else:
            return [-1]

    ret = []
    for opt in rules[rule].split(' | '):
        idx = 0
        for sub_rule in opt.split(' '):
            #G.add_edge((rule, level), (sub_rule, level+1))
                
            if idx >= len(msg) or set(w := consume(msg[idx:], sub_rule, level + 1)) == set([-1]):
                idx = -1
                break

            idx += [x for x in w if x != -1][0]
            print(rule, " -> ", w, idx)

        ret.append(idx)

    return ret

main()


# Length of strings that match [rule 8] is 5 and length of strings that match [rule 11] is 10.
# So, a message of length 30 could match 6 consecutive strings of [rule 8], which will leave no
# space for [rule 11] to check for its match.
# A good example to test is a string: [42 42 42 42 31 31]; now, try to reason why our method for 
# part 1 breaks, for refresher rule 0 is 0: 8 11