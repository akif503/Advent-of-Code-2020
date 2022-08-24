# TODO: Making sense of Chinese remainder theorem
# Also do an iterative search through pairwise progression
import math
import re
import numpy as np
from itertools import count
from functools import reduce


data = open("13.txt", "r").read()

earliest_time, bus_ids = data.split("\n")

def part1(earliest_time, bus_ids):

    earliest_time = int(earliest_time)
    bus_ids = [int(x) for x in re.findall(r"(\d+)", bus_ids)]

    # Smallest multiple of x that is greater than n
    smgn = lambda x, n: (n // x + 1) * x

    # earliest_bus = smallest multiple of bus_id[0] which is greater than earliest_time
    earliest_bus = smgn(bus_ids[0], earliest_time)
    result = 0

    for bus_id in bus_ids[1:]:
        earliest_bus = min(cur_smallest := smgn(bus_id, earliest_time), earliest_bus)
        if cur_smallest == earliest_bus:
            result = (earliest_bus - earliest_time) * bus_id

    print(result)

# Extended euclidean alogrithm, using matrix operation
# There's another method of finding modular inverse, by using fermat's little theorem -
# It is applicable here because a and b are co-prime
def eea_M(a, b, state):
    if b == 0:
        return state[0]

    q = a // b
    transform_matrix = np.array([[0, 1],
                                 [1, -q]], dtype=np.int32)

    state = np.matmul(transform_matrix, state)
    return eea_M(b, a % b, state)

# Naive solution to a congurence equation of the form
# Ni[i] * x = 1 (mod p)
def naive_sol(Ni, ps):
    xi = []
    i = 0
    for p in ps:
        # Find the solution to the congruence equation
        #       Ni[i] * x = 1 (mod p)
        x = 1
        xn = Ni[i] * x
        while True:
            if xn % p == 1:
                break

            x += 1
            xn = Ni[i] * x

        xi.append(x)
        i += 1


# Chinese Remainder Theorem
def crt(ps, bs):
    # ps: List of co-primes
    # bs: remainders corresponding to each prime numbers

    # N = p1*p2*...*pn
    N = reduce(lambda prod, p: prod * p, ps)
    
    Ni = [N // p for p in ps]

    # Initial State for Extended Euclidean Algorithm
    init_state = np.array([[1, 0], [0,1]])
    # xi[i] is the modular multiplicative inverse of Ni[i] under (mod p)
    xi = [eea_M(n, p, init_state)[0] for n, p in zip(Ni, ps)]

    # result = SUM(bi*Ni*xi)
    result = reduce(lambda acc, t: acc + reduce(lambda prod, a: prod * a, t), zip(bs, Ni, xi), 0)

    return result % N

    
def part2():
    global bus_ids
    bus_ids = bus_ids.split(",")
    bus_ids = "17,x,13,19".split(",")

    ps, rems = list(zip(*[(int(x), -i) for i, x in enumerate(bus_ids) if x != 'x']))

    result = crt(ps, rems)

    print(result)


# Iterative product summation solution
def part2_alternative():
    global bus_ids
    # bus_ids = bus_ids.split(",")
    # bus_ids = ['17','x','13','19']

    running_product = 1
    # The first bus that's available
    result = int(bus_ids[0])

    for i, bus_id in enumerate(bus_ids):
        if bus_id.isnumeric():
            bus_id = int(bus_id)
            while True:
                if (result + i) % bus_id == 0:
                    break

                result += running_product
            
            running_product *= bus_id

    print(result)

# part1(earliest_time, bus_ids)
part2()
# part2_alternative()