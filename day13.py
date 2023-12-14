import pprint
import math

inputFile = 'inputs/input13.txt'

# Part 1

def flip_diagonally(table):
    flipped_table = [''] * len(table[0])
    for i in range(len(table[0])):
        column = ''
        for row in table:
            column += row[i]
        flipped_table[i] = column
    return flipped_table

def find_horizontal_line(table):
    result = 0
    at_least_one = set()
    more_than_two = set()
    for row in table:
        if row not in at_least_one:
            at_least_one.add(row)
        else:
            more_than_two.add(row)
    for row in more_than_two:
        result = is_valid(row, table)
        if result > 0:
            break
    return result

def is_valid(row, table):
    result = 0
    indexes = [i for i, x in enumerate(table) if x == row]
    for i, index1 in enumerate(indexes[:-1]):
        indexes2 = indexes.copy()[i+1:]
        for index2 in indexes2:
            middle = (index1 + index2) / 2
            if middle % 1 != 0:
                result += valid_horizontal_line(middle, table)
    return result

def valid_horizontal_line(line, table):
    lower, top = math.floor(line), math.ceil(line)
    while lower >= 0 and top < len(table):
        if table[lower] != table[top]:
            return 0
        lower -= 1
        top += 1
    return math.ceil(line)

table = []

total = 0
with open(inputFile) as file:
    for line in file:
        line = line.strip()
        if line:
            table.append(line)
        elif table:
            temp = 0
            temp += 100 * find_horizontal_line(table)
            temp += find_horizontal_line(flip_diagonally(table))
            #pprint.pprint(table)
            #rint(temp)
            total += temp
            table = []

    # Process the last group  
    if table:
        total += 100 * find_horizontal_line(table)
        total += find_horizontal_line(flip_diagonally(table))

print('Part 1:', total)


