# TODO: Convert it to the binary solution


from functools import reduce

def find_seat(boarding_pass):

    row = find(boarding_pass[:7], ('F', 'B'), (0, 127))
    col = find(boarding_pass[7:], ('L', 'R'), (0, 7))

    return (row, col)


def find(match_string, salt, interval):
    # salt[0] - take lower half
    # salt[1] - take upper half

    lower, upper = interval
    for letter in match_string:
        if letter == salt[0]:
            upper = (lower + upper) // 2
        
        else:
            lower = (lower + upper + 1) // 2

    # At this point both lower and upper should be same
    return lower
    

def calculate_seat_id(row, col):
    return row * 8 + col


def main():
    data = open("input.txt", "r")

    boarding_passes = [bp for bp in data.read().split("\n") if bp != ""]

    #part1(boarding_passes)
    part2(boarding_passes)
    
    
def part1(boarding_passes):

    result = -1
    for bp in boarding_passes:
        row, col = find_seat(bp)

        result = max(calculate_seat_id(row, col), result)

    print(result)

    # One-liner version of the above code segmant
    # result = reduce(lambda acc, bp: max(acc, calculate_seat_id(*find_seat(bp))), boarding_passes, -1)
    

def part2(boarding_passes):

    id_list = [calculate_seat_id(*find_seat(bp)) for bp in boarding_passes]

    for possible_bp_id in range(min(id_list) + 1, max(id_list) - 1):
        if possible_bp_id not in id_list:
            print(possible_bp_id)

    # One-liner version of the above loop (-1 means no such id found) [This is valid when there's only one such id, as is our case]
    # result = reduce(lambda acc, x: x if x not in id_list else acc, range(min(id_list) + 1, max(id_list) - 1), -1)

    
main()