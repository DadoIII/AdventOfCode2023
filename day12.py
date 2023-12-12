inputFile = 'inputs/test12.txt'

# Part 1

def create_groupings(springs, groups):
    # Create groups of strings that are sepparated by at least one operational spring
    spring_groups = [group for group in springs.split(".") if group != ""]
    return spring_groups, groups

# Recursive function that tries all combinations of spring groups with the group numbers 
def all_combinations(spring_groups, numbers, pairing):
    current_spring_group = spring_groups[0]
    # Last spring group. Have to try to fit all the remaining numbers in it
    if len(spring_groups) == 1:
        if len(current_spring_group) >= sum(numbers) + len(numbers) - 1:
            pairing[current_spring_group] = numbers
            return valid_combinations(pairing)
        else:
            return 0
    else:
        total = 0
        # Try to put different amounts of group numbers into the current spring group
        for i in range(len(numbers)):
            numbers_slice = numbers[:i]
            if len(current_spring_group) >= sum(numbers_slice) + len(numbers_slice) - 1:
                pairing[current_spring_group] = numbers_slice
                total += all_combinations(spring_groups[1:], numbers[i:], pairing)
            else:
                break
        return total


def valid_combinations(pairing):
    prod = 1
    for (springs, numbers) in zip(pairing, pairing.values()):
        if numbers != []:
            prod *= all_valid_combinations(springs, numbers, sum(numbers) - springs.count('#'), [], 0)
                
    return prod

def all_valid_combinations(springs: str, numbers: [int], springs_to_place: int, placed_indexes: [int], index: int) -> int:
    # All springs placed, check if the placement is valid
    if springs_to_place == 0:
        return 1 if is_valid(springs, numbers, placed_indexes) else 0
    # Not enough unkown spaces to place the springs
    elif springs_to_place > springs.count('?') - index:
        return 0
    else:
        total = 0
        total += all_valid_combinations(springs, numbers, springs_to_place, placed_indexes, index + 1)  # Continue without placing a spring on this index
        total += all_valid_combinations(springs, numbers, springs_to_place - 1, placed_indexes + [index], index + 1)  # Continue with placing a spring on this index
        return total

   
def is_valid(springs, numbers, placed_indexes):
    q_index = 0
    for i in range(len(springs)):
        if springs[i] == '?':
            if q_index in placed_indexes:
                springs = springs[:i] + '#' + springs[i+1:]
            q_index += 1
    if [len(group) for group in springs.split('?') if '#' in group] == numbers:
        print("Returning 1", springs, numbers)
        return 1
    else:
        print("Returning 0", springs, numbers)
        return 0
        

total = 0
with open(inputFile, 'r') as file:
    i = 0
    for line in file.readlines():
        springs, groups = line.strip().split(" ")
        spring_groups, groups = create_groupings(springs, [int(x) for x in groups.split(",")])
        print(spring_groups, groups)
        temp = all_combinations(spring_groups, groups, [{group: []} for group in spring_groups])
        print(temp)
        total += temp
        #if i > 5:
        #    break
        i += 1

print('Part 1:', total)