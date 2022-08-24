# Van Eck's Sequence
import time

init_numbers = [0,1,4,13,15,12,16]

def sol(init_numbers, total_turns):
    age = {n: i for i, n in enumerate(init_numbers[:-1])}
    last_number = init_numbers[-1]

    for turn in range(len(init_numbers), total_turns):
        cur_number = 0 if last_number not in age else (turn - 1) - age[last_number]
        
        age[last_number] = turn - 1
        last_number = cur_number

    # Result
    print(last_number)

n1 = 2021
n2 = 30000000
t1 = time.time()
sol(init_numbers, n2)
print(time.time() - t1)