import re
from collections import defaultdict

data = open("input.txt", "r").read()

# Program: [..., (instruction, operator, operand), ...]
program = [(*(m := re.findall(r"^(\w+)\s(\+|\-)(\d+)$", line)[0])[0:-1], int(m[-1])) for line in data.split("\n") if line != ""]

# Equivalent to ^^^^^^^^!!!
# for line in data.split("\n"):
#     if line != "":
#         inst, operator, operand = re.findall(r"^(\w+)\s(\+|\-)(\d+)$", line)[0]
#         program.append((inst, operator, int(operand)))
        

def run(program):
    executed = defaultdict(bool)
    pc = 0
    acc = 0
    
    infinite_loop = False

    while True:
        if executed[pc] or pc >= len(program):
            if executed[pc]:
                infinite_loop = True
            break
        
        executed[pc] = True

        # Elements of an instruction
        inst, operator, operand = program[pc]

        # Change operand according to the operator
        operand = operand if operator == '+' else -operand

        if inst == 'jmp':
            pc += operand

        else:
            pc += 1
            if inst == 'acc':
                acc += operand

    return (acc, infinite_loop)
    
def part1():
    global program 

    print(run(program)[0])

def part2():
    global program

    for index, line in enumerate(program):
        if line[0] == 'jmp':
            # Change jmp to nop
            program[index] = ('nop', *line[1:])
            if not (m := run(program))[1]:
                print(m[0])
                break
            program[index] = line

        elif line[0] == 'nop':
            # Change nop to jmp
            program[index] = ('jmp', *line[1:])
            if not (m := run(program))[1]:
                print(m[0])
                break
            program[index] = line

part1()