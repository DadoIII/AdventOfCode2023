import pprint
import math

inputFile = 'inputs/input15.txt'

# Part 1

instructions = []

with open(inputFile, 'r') as file:
    ending_instruction = ''
    for line in file:
        new_instructions = line.strip().split(',')
        instructions.append(ending_instruction + new_instructions[0])
        instructions += new_instructions[1:-1]
        ending_instruction = new_instructions[-1]
    
    instructions.append(new_instructions[-1])

total_value = 0

for instruction in instructions:
    current_value = 0
    for character in instruction:
        current_value += ord(character)
        current_value = (current_value * 17) % 256
    total_value += current_value

print('Part 1:', total_value)