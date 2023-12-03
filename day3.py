import numpy as np

inputFile = "inputs/input3.txt"

#part 1

def symbol_nearby(top, middle, bottom, left, right):
    #to not go out of bounds
    if left - 1 < 0:
        left = 1
    if right + 1 == len(middle):
        right -= 1

    #check the top row
    if top != None:
        if any([not x.isdigit() and not x == "." for x in top[left-1:right+2]]):
            return True
    #check the bottom row
    if bottom != None:
        if any([not x.isdigit() and not x == "." for x in bottom[left-1:right+2]]):
            return True
    #check to the left
    if not middle[left-1].isdigit() and not middle[left-1] == ".":
        return True
    #check to the right
    if not middle[right+1].isdigit() and not middle[right+1] == ".":
        return True
    
    return False


def find_numbers(top, middle, bottom):
    numbers = []

    index = 0
    while index < len(middle):
        #found a start of a number
        if middle[index].isdigit():
            end = index
            #find the end of the number
            while end + 1 < len(middle) and middle[end+1].isdigit():
                end += 1
            if symbol_nearby(top, middle, bottom, index, end):
                numbers.append(int(middle[index:end+1]))
            index = end

        index += 1
    return numbers

total = 0
with open(inputFile, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    total += sum(find_numbers(None, lines[0], lines[1]))
    for i in range(1, len(lines) - 1):
        top = lines[i-1]
        middle = lines[i]
        bottom = lines[i+1]
        total += sum(find_numbers(top, middle, bottom))
    total += sum(find_numbers(lines[-2], lines[-1], None))

print("Part 1:", total)


#part 2
def find_adjecent_numbers(top, middle, bottom, index):
    numbers = []
    rows = [top, middle, bottom]
    for row in rows:
        left = index - 1 if index > 0 else index
        right = index + 1 if index + 1 < len(middle) else index
        #expand left as long as there are digits
        while left > 0 and row[left].isdigit():
            left -= 1
        #expand right as long as there are digits
        while right + 1 < len(middle) and row[right].isdigit():
            right += 1
        #only take numbers from the slice
        numbers += [int(x) for x in row[left:right+1].replace("*", ".").split(".") if x.isdigit()]

    return numbers



def find_gears(top, middle, bottom):
    gears = []
    for i, symbol in enumerate(middle):
        if symbol == "*": #find gear
            numbers = find_adjecent_numbers(top, middle, bottom, i)
            if len(numbers) == 2:
                gears.append(np.prod(numbers))
    return gears

gear_ratio = 0
with open(inputFile, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    for i in range(1, len(lines) - 1):
        top = lines[i-1]
        middle = lines[i]
        bottom = lines[i+1]
        gear_ratio += sum(find_gears(top, middle, bottom))

print("Part 2:", gear_ratio)