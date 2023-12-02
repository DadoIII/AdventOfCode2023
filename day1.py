inputFile = "inputs/input1.txt"

#part 1
def get_digits(text):
    return [x for x in text if x.isdigit()]

sum = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        digits = get_digits(line.strip())
        sum += int(digits[0] + digits[-1])

print("Part 1:", sum)

#part 2
words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def has_digit(text):
    value = -1
    for word in words.keys():
        if word in text:
            value = words[word]
    return value

def get_first_last_digits(text):
    first, last = -1, -1

    index = 0 
    while first < 0: #look for first digit
        if text[index].isdigit(): #its in digit form
            first = int(text[index])
        else: #its in text form
            first = has_digit(text[:index+1])
        index += 1

    index = -1
    while last < 0: #look for last digit
        if text[index].isdigit(): #its in digit form
            last = int(text[index])
        else: #its in text form
            last = has_digit(text[index:])
        index -= 1

    return first, last

sum = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        first, last = get_first_last_digits(line.strip())
        sum += int(str(first) + str(last))

print("Part 2:", sum)