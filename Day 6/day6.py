from collections import defaultdict

with open("input.txt", "r") as f:
    groups = [x for x in f.read().split("\n\n") if x != ""]


def part1():
    result = 0
    for group in groups:
        forms = [x for x in group.split('\n') if x != ""]

        # If anyone answered yes to one of question then it would be on the list
        answers = set()

        for answer in forms:
            for letter in answer:
                answers.add(letter)

        result += len(answers)

    with open("out1.txt", "w") as out:
        out.write(f"{result}\n")


def part2():
    result = 0
    for group in groups:
        forms = [x for x in group.split('\n') if x != ""]

        answers = defaultdict(int)

        for answer in forms:
            for letter in answer:
                answers[letter] += 1

        for answer in answers:
            if answers[answer] == len(forms):
                result += 1

    with open("out2.txt", "w") as out:
        out.write(f"{result}\n")

