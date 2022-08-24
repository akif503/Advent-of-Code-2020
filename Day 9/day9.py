from itertools import combinations

data = open("input.txt", "r").read()

preamble_length = 25

numbers = [int(x) for x in data.split("\n") if x != ""]

def check_validity(numbers, target):
    for n1, n2 in combinations(numbers, 2):
        if n1 != n2 and n1 + n2 == target:
            return True 

    return False

invalid_number = 0
for i in range(preamble_length, len(numbers)):
    if not check_validity(numbers[i-preamble_length:i], numbers[i]):
        invalid_number = numbers[i]
        break

print(invalid_number)

result = 0
low, acc = 0, numbers[0]

for high in range(1, len(numbers)):
    while acc > invalid_number and low < high: 
        acc -= numbers[low]
        low += 1
    
    if acc == invalid_number:
        result = (max(numbers[low:high]) + min(numbers[low:high]))
        break
    
    else:
        acc += numbers[high]

print(result)