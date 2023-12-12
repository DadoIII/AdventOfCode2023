inputFile = 'inputs/input12.txt'

# Part 1

def create_groupings(springs, groups):
    # Create groups of strings that are sepparated by at least one operational spring
    spring_groups = [group for group in springs.split(".") if group != ""]
    return spring_groups, groups

# Recursive function that tries all combinations of spring groups with the group numbers 
def all_combinations(spring_groups, numbers, pairing):
    current_spring_group = spring_groups[0]
    # Last spring group. Have to try to fit all the remaining groups in
    if len(spring_groups) == 1:
        if len(current_spring_group) >= sum(numbers) + len(numbers) - 1:
            pairing[current_spring_group] = numbers
            return valid_combinations(pairing)
        else:
            return 0
    else:
        total = 0
        # Try to put different amounts of group numbers into the latest spring group
        for i in range(len(numbers)):
            numbers_slice = numbers[:i]
            if len(current_spring_group) >= sum(numbers_slice) + len(numbers_slice) - 1:
                pairing[current_spring_group] = numbers_slice
                total += all_combinations(spring_groups[1:], numbers[i:], pairing)
            else:
                break
        return total


def valid_combinations(pairing):
    for (springs, numbers) in pairing:
        pass
    return 0


total = 0
with open(inputFile, 'r') as file:
    i = 0
    for line in file.readlines():
        springs, groups = line.strip().split(" ")
        spring_groups, groups = create_groupings(springs, [int(x) for x in groups.split(",")])
        print({group: [] for group in spring_groups})
        total += all_combinations(spring_groups, groups, {group: [] for group in spring_groups})
        if i > 5:
            break
        i += 1

print('Part 1:', total)