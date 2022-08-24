# How many passwords are valid
with open("input.txt", "r") as data:
    sample_points = [x for x in data.read().split("\n") if x != ""]


def part1():
    valid_password = 0

    for sample in sample_points:
        split = sample.split()

        policy = split[:-1]
        password = split[-1]

        lower, upper = tuple([int(x) for x in policy[0].split("-")])
        policy_letter = policy[-1][0]

        policy_letter_count = 0
        for letter in password:
            if letter == policy_letter:
                policy_letter_count += 1
                
        if lower <= policy_letter_count <= upper:
            valid_password += 1

    with open("out1.txt", "w") as out:
        out.write(f"{valid_password}\n")


def part2():
    valid_password = 0

    for sample in sample_points:
        split = sample.split()

        policy = split[:-1]
        password = split[-1]

        lower, upper = tuple([int(x) for x in policy[0].split("-")])
        policy_letter = policy[-1][0]

        if (password[lower - 1] == policy_letter or password[upper - 1] == policy_letter) and (password[lower-1] != password[upper-1]):
            valid_password += 1
    
    with open("out2.txt", "w") as out:
        out.write(f"{valid_password}\n")
