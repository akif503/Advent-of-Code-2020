# Maximum bipartite matching (part 2)
import re

def main():
    data = open("16.txt", "r").read().split("\n\n")

    fields = {}
    for section in data:
        if re.search(r"your ticket", section):
            my_ticket = list(map(int,section.split("\n")[-1].split(',')))

        elif re.search(r"nearby tickets", section):
            nearby_tickets = [list(map(int, x.split(","))) for x in section.split("\n")[1:] if x != ""]

        else:
            for line in section.split("\n"):
                extract = re.findall(r"^(\w+\s*\w+): (\d+\-\d+) or (\d+\-\d+)$", line)

                field = extract[0][0]
                ranges = [tuple(map(int,x.split("-"))) for x in extract[0][1:]]
                
                fields[field] = ranges
                
    part1(fields, nearby_tickets)
    part2(fields, nearby_tickets, my_ticket)

def check_validity(fields, value):
    within_range = lambda r,c: r[0] <= c <= r[1]

    for field in fields:
        ranges = fields[field]
        
        for field_range in ranges:
            if within_range(field_range, value):
                return True
        
    return False

def part1(fields, nearby_tickets):
    error = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not check_validity(fields, value):
                error += value
            
    print(error)
    
def find_possible_fields(fields, value):
    within_range = lambda r,c: r[0] <= c <= r[1]

    possible_fields = []
    for field in fields:
        ranges = fields[field]
        
        for field_range in ranges:
            if within_range(field_range, value):
                possible_fields.append(field)
                break
                
    return possible_fields


def part2(fields, nearby_tickets, my_ticket):
    valid_tickets = []
    for ticket in nearby_tickets:
        for value in ticket:
            if not check_validity(fields, value):
                break
        else:
            valid_tickets.append(ticket)

    possible_fields_for_pos = []
    for index in range(len(valid_tickets[0])):
        fields_for_this_pos = set(fields.keys())
        for ticket in valid_tickets:
            possible_fields = find_possible_fields(fields, ticket[index])

            fields_for_this_pos.intersection_update(set(possible_fields))

        possible_fields_for_pos.append(fields_for_this_pos)

    selected = {}
    while not (len(selected) >= len(fields)):
        # Find the smallest length
        index, smallest = min(enumerate(possible_fields_for_pos), key=lambda t: m if (m := len(t[-1])) else 1000)
        
        selected_field = list(smallest)[0]
        selected[index] = selected_field

        for field in possible_fields_for_pos:
            field.discard(selected_field)

    result = 1
    for k, v in zip(selected, selected.values()):
        if 'departure' in v:
            result *= my_ticket[k]

    print(result)


main()