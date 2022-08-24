def main():
    data = open("25.txt").read().rstrip('\n')

    data1 = """5764801
    17807724"""

    public_card, public_door = map(int,data.split('\n'))

    public_key_subject_number = 7

    print(public_card, public_door)
    ls_card, ls_door = find_loop_size(public_card), find_loop_size(public_door)
    print(ls_card, ls_door)

    # Find encryption key
    print(transform(public_door, ls_card))
    print(transform(public_card, ls_door))


def find_loop_size(desired):
    loop_size = 0
    value = 1
    while True:
        if value == desired:
            return loop_size

        value = next_value(value, 7)
        loop_size += 1
        
    return loop_size


def next_value(value, subject_number):
    return value * subject_number % 20201227 


def transform(subject_number, loop_size):
    value = 1

    for _ in range(loop_size):
        value = next_value(value, subject_number)

    return value


main()