import re

PART = 2

def main():
    data = open("18.txt", "r").read()
    lines = [line for line in data.split("\n") if line != ""]

    result = 0
    for line in lines:
        result += do_eval(line)

    print(result)

def do_eval(expression):
    # Evaluate the bracketted expression firsts
    while '(' in expression:
        expression = re.sub(r"\(([^()]+)\)", lambda e: inner(e.group(1)), expression)
    
    return int(inner(expression))


def inner(expression):
    global PART
    # Evaluate expression that do not have any brackets
    # Part 1   
    if PART == 1:
        # We don't do addition or multiplication first or second because both have same precedence
        # and that's why we can evaluate from left to right as the operators come by.
        while '+' in expression or '*' in expression:
            # e is a non-overlapping sub group matching the pattern of the form d1 + d2
            # We do a count=1 because otherwise it will convert all the possible non-overlapping groups
            # However, we want to convert each one from left to right, and count=1 will ensure that
            expression = re.sub(r"(\d+)\s*[+*]\s*(\d+)", lambda e: str(eval(e.group(0))), expression, count=1)
    
    if PART == 2:
        # We do all the addition first because + has higher precedence than * in the part 2.
        while '+' in expression:
            expression = re.sub(r"(\d+)\s*[+]\s*(\d+)", lambda e: str(eval(e.group(0))), expression)

        while '*' in expression:
            expression = re.sub(r"(\d+)\s*[*]\s*(\d+)", lambda e: str(eval(e.group(0))), expression)

    return expression

main()