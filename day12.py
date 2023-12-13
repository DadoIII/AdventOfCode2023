inputFile = 'inputs/input12.txt'

# Part 1

def create_groupings(springs, groups):
    # Create groups of strings that are sepparated by at least one operational spring
    spring_groups = [group for group in springs.split(".") if group != ""]
    return spring_groups, groups

# Recursive function that tries all combinations of spring groups with the group numbers 
def all_combinations(spring_groups: [str], numbers: [int], placed_numbers: [[int]], index: [int]) -> int:
    current_spring_group = spring_groups[index]
    # Last spring group. Have to try to fit all the remaining numbers in it
    if index == len(spring_groups) - 1:
        if len(current_spring_group) >= sum(numbers) + len(numbers) - 1:
            return valid_combinations(spring_groups, placed_numbers[:-1] + [placed_numbers[-1] + numbers])
        else:
            return 0
    else:
        total = 0

        # Move to the next group without placing more numbers into the current group 
        total += all_combinations(spring_groups, numbers, placed_numbers + [[]], index + 1)
        # If there is space in the current group place the next number in
        if numbers != [] and len(current_spring_group) >= sum(placed_numbers[-1] + [numbers[0]])+ len(placed_numbers[-1]):
            total += all_combinations(spring_groups, numbers[1:], placed_numbers[:-1] + [placed_numbers[-1] + [numbers[0]]], index)

        return total


def valid_combinations(spring_groups, number_groups):
    prod = 1
    for (springs, numbers) in zip(spring_groups, number_groups):
        # Trying to place less springs than the number of operational springs already there
        if sum(numbers) < springs.count('#'):
            prod = 0
            break
        else:
            prod *= all_valid_combinations(springs, numbers, sum(numbers) - springs.count('#'), [], 0)
                
    return prod

def all_valid_combinations(springs: str, numbers: [int], springs_to_place: int, placed_indexes: [int], index: int) -> int:
    # All springs placed, check if the placement is valid
    if springs_to_place == 0:
        return is_valid(springs, numbers, placed_indexes)
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
        return 1
    else:
        return 0
        
        
total = 0
with open(inputFile, 'r') as file:
    for line in file.readlines():
        springs, groups = line.strip().split(" ")
        spring_groups, groups = create_groupings(springs, [int(x) for x in groups.split(",")])
        total += all_combinations(spring_groups, groups, [[]], 0)

print('Part 1:', total)