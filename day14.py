import pprint
import math

inputFile = 'inputs/input14.txt'

# Part 1

def count_load(unmovable_indexes, num_of_rocks, length):
    if len(unmovable_indexes) != len(num_of_rocks) - 1:
        raise Exception('Wrong amount of indexes and num_of_rocks!')
    
    load = 0
    unmovable_indexes = unmovable_indexes[::-1]
    num_of_rocks = num_of_rocks[::-1]
    unmovable_rock = unmovable_indexes.pop()
    rocks = num_of_rocks.pop()
    for i in range(length):
        #print(unmovable_indexes, num_of_rocks)
        if i == unmovable_rock:
            if unmovable_indexes != []:
                unmovable_rock = unmovable_indexes.pop()
            rocks = num_of_rocks.pop()
        elif rocks > 0:
            load += length - i
            rocks -= 1
    return load



grid = []
total_load = 0

with open(inputFile, 'r') as file:
    for line in file:
        grid.append(line.strip())

for i in range(len(grid[0])):
    unmovable_indexes = []
    num_of_rocks = [0]
    for j in range(len(grid)):
        current = grid[j][i]
        if current == 'O':
            num_of_rocks[-1] += 1
        elif current == '#':
            unmovable_indexes.append(j)
            num_of_rocks.append(0)
    total_load += count_load(unmovable_indexes, num_of_rocks, len(grid))

print('Part 1:', total_load)