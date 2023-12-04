inputFile = "inputs/input4.txt"

#part 1
total = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        #formatting the lines
        _, numbers = line.strip().split(":")
        winning_numbers, my_numbers = numbers.strip().split("|")
        winning_numbers = [int(x) for x in winning_numbers.strip().split(" ") if x.isdigit()]
        my_numbers = [int(x) for x in my_numbers.strip().split(" ") if x.isdigit()]
        #collect matching numbers
        matching_numbers = [x for x in my_numbers if x in winning_numbers]

        if len(matching_numbers) > 0:
            total += 2**(len(matching_numbers) - 1)

print("Part 1:", total)

#part 2
total = 0
with open(inputFile, "r") as file:
    lines = file.readlines()
    cards = [1]*len(lines) #keep track of card counts
    for i, line in enumerate(lines):
        #formatting lines
        _, numbers = line.strip().split(":")
        winning_numbers, my_numbers = numbers.strip().split("|")
        winning_numbers = [int(x) for x in winning_numbers.strip().split(" ") if x.isdigit()]
        my_numbers = [int(x) for x in my_numbers.strip().split(" ") if x.isdigit()]
        #collect matching numbers
        matching_numbers = [x for x in my_numbers if x in winning_numbers]
        points = len(matching_numbers)
        #add new cards
        for j in range(i + 1, i + points + 1):
            cards[j] += cards[i]


print("Part 2:", sum(cards))

