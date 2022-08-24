import re 

data = open("input.txt", "r")

# List of dicts
passports = []
current_passport = {}

# change to data.read()
for line in data.read().split("\n"):
    if line == "":
        passports.append(current_passport)
        current_passport = {}

    else:
        for kv in line.split(' '):
            key, value = tuple(kv.split(":"))

            current_passport[key] = value

def part1():
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid_passport = 0

    for passport in passports:
        valid = True
        for field in fields:
            if passport.get(field) == None:
                valid = False

        valid_passport = valid_passport + 1 if valid else valid_passport

    with open("out1.txt", "w") as out:
        out.write(f"{valid_passport}\n")

    
def valid_date(str_val, no_of_digits, lower, upper):
    # Returns if the date is not valid, based on if it is numeric and it has certain 
    # number of digits and is insider the range [lower, upper]
    #   - val: str
    #   - no_of_digits, lower, upper: int
    
    return (str_val.isnumeric() and len(str_val) == no_of_digits and lower <= int(str_val) <= upper)


def valid_height(hgt):
    # Returns if the height satisfies the condition

    scale_ranges = {
        "cm": [150, 193],
        "in": [59, 76]
    }
    
    valid = False
    if hgt[-2:] in scale_ranges.keys() and hgt[:-2].isnumeric():
        scale = hgt[-2:]
        val = int(hgt[:-2])
        lower, upper = scale_ranges[scale]

        valid = lower <= val <= upper

    return valid


def part2():
    valid_passport = 0

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for passport in passports:
        valid = True

        for field in fields:
            if passport.get(field) == None:
                valid = False
            
        if valid:
            # byr - 4 digits; 1920 <= 2002
            byr, iyr, eyr, hgt, hcl, ecl, pid = tuple([passport[field] for field in fields])
            # print(tuple([passport[field] for field in fields]))

            # Check byr, iyr, and eyr
            if not (valid_date(byr, 4, 1920, 2002) and valid_date(iyr, 4, 2010, 2020) and valid_date(eyr, 4, 2020, 2030)):
                valid = False
                
            # hgt
            if not valid_height(hgt):
                valid = False

            # hcl
            if not (hcl[0] == "#" and len(hcl[1:]) == 6):
                valid = False 

            for char in hcl[1:]:
                # In range a - f
                inalpha = char in [chr(ord('a') + x) for x in range(6)]
                if not (char.isnumeric() or inalpha):
                    valid = False
            
            # ecl 
            if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False

            # pid
            if not (pid.isnumeric() and len(pid) == 9):
                valid = False
        
        valid_passport = valid_passport + 1 if valid else valid_passport

    with open("out2.txt", "w") as out:
        out.write(f"{valid_passport}\n")


def alternate_solution():
    # Solution to both part 1 and part 2
    global passports

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # Validities
    valid_height = lambda hgt: 1 == len(re.findall(r"^(1[5-9][0-9]cm|[5-7][0-9]in)$", hgt))
    valid_haircolor = lambda hcl: 1 == len(re.findall(r"^(#[a-f0-9]{6})$", hcl))
    valid_eyecolor = lambda ecl: 1 == len(re.findall(r"^(amb|blu|brn|gry|grn|hzl|oth)$", ecl))
    valid_pid = lambda pid: 1 == len(re.findall(r"^([0-9]{9})$", pid))

    result1, result2 = 0, 0
    for passport in passports:
        valid = True

        for field in fields:
            if passport.get(field) == None:
                valid = False
            
        result1 = result1 + 1 if valid else result1

        if valid:
            byr, iyr, eyr, hgt, hcl, ecl, pid = tuple([passport[field] for field in fields])
            
            valid = all([
                valid_date(byr, 4, 1920, 2002),
                valid_date(iyr, 4, 2010, 2020),
                valid_date(eyr, 4, 2020, 2030),
                valid_height(hgt),
                valid_haircolor(hcl),
                valid_eyecolor(ecl),
                valid_pid(pid)
            ])

        result2 = result2 + 1 if valid else result2

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


alternate_solution()