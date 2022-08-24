# Adopted from user u/Strilanc and u/sciyoshi's solution 
# Very hacky but yet a very smart solution
# The idea is to replace every number in the string with a class object of that number.
# That is: "5 * 6 + 12" -> "A(5) * A(6) + A(12)". 

# And then we can define the operators to be anything we want, using the underscore class methods.
# And to keep the precedence relation, we just convert the operators according to the precedence
# relation that match our case, we can do this because we can define our operators to do anything we
# want as discussed above.

import re

def main():
    data = open("18.txt").read()
    lines = [line for line in data.split("\n") if line != ""]

    part1 = 0
    part2 = 0

    for line in lines: 
        line = re.sub(r"(\d+)", r"A(\1)", line)

        # For part1 both operators have equal precedence, so we change multiplication (*) to subtraction (-)
        line = line.replace('*', '-')
        part1 += eval(line, {'A': A}).value

        # For part2 addition has higher precedence, so we change it to multiplication (*) and keep the
        # subtraction from the previous case, as it is lower in precedence than multiplication.
        line = line.replace('+', '*')
        part2 += eval(line, {'A': A}).value

    print(part1)
    print(part2)


class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value + other.value)
    
    def __sub__(self, other):
        return A(self.value * other.value)
    
    def __mul__(self, other):
        return A(self.value + other.value)


main()