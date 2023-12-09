inputFile = 'inputs/input9.txt'

#part 1 and 2

next_number_total = 0
previous_number_total = 0

def find_numbers(numbers):
    next_number = numbers[-1] #just add the last numbers of each row
    previous_numbers = [numbers[0]] #collect the first numbers of each row
    while any([number != 0 for number in numbers]):
        next_row = []
        for i in range(len(numbers) - 1):
            next_row.append(numbers[i+1] - numbers[i])
        numbers = next_row
        next_number += numbers[-1]
        previous_numbers.append(numbers[0])
    
    #loop backwards and figure out the numbers in front of each row
    previous_numbers = previous_numbers[::-1]
    previous_number = 0
    for i in range(1, len(previous_numbers)):
        previous_number = (previous_numbers[i] - previous_number)

    return next_number, previous_number

with open(inputFile, 'r') as file:
    for line in file.readlines():
        next_number, previous_number = find_numbers([int(x) for x in line.strip().split(" ")])
        next_number_total += next_number
        previous_number_total += previous_number

print('Part 1:', next_number_total)
print('Part 2:', previous_number_total)



