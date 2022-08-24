import re 

data = open("14.txt", "r").read()

data1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

data2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

# data = data2
# data = data1

# u/sophiebits
# The function when thought without the replace part, implants the bit (where bit != X) of mask on arg
# And the replace part where X is present will keep the bit of the arg variable
def domask(arg, mask):
    arg |= int(mask.replace('X', 0), 2)
    arg &= int(mask.replace('X', 1), 2)
    

def part1(data):
    # Address -> Byte code
    memory = {}

    mask = ""
    for line in data.split("\n"):
        if m := re.search(r"mask.*=\s([\w\d]+)", line):
            mask = m.groups(0)[0]
            continue
        
        if line != "":
            addr, value = [int(x) for x in re.findall(r"(\d+)", line)]

            value = list(bin(value))[2:]
            value = ['0' for _ in range(36 - len(value))] + value

            for i, m in enumerate(mask):
                if mask[i] != 'X':
                    value[i] = mask[i]

            value = int("".join(value), 2)
            memory[addr] = value

    result = sum(memory.values())

    print(result)

def part2(data):

    memory = {}
    mask = ""
    for line in data.split("\n"):
        if m := re.search(r"mask.*=\s([\w\d]+)", line):
            mask = m.groups(0)[0]
            continue
        
        if line != "":
            addr, value = [int(x) for x in re.findall(r"(\d+)", line)]

            addr = list(bin(addr))[2:]
            addr = ['0' for _ in range(36 - len(addr))] + addr

            for i, m in enumerate(mask):
                if mask[i] != '0':
                    addr[i] = mask[i]

            floating_bit_locs = [i for i, b in enumerate(addr) if b == 'X']

            part_addrs = []
            elaborate("", len(floating_bit_locs), 0, part_addrs)

            for part_addr in part_addrs:
                floating_address = list(addr)
                for floating_bit, loc in zip(part_addr, floating_bit_locs):
                    floating_address[loc] = floating_bit

                memory["".join(floating_address)] = value
            
    print(sum(memory.values()))

def elaborate(part_addr, n, i, part_addrs):
    if i >= n:
        part_addrs.append(part_addr)
        return 
    
    elaborate(part_addr + '0', n, i + 1, part_addrs)
    elaborate(part_addr + '1', n, i + 1, part_addrs)

part2(data)