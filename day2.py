import numpy as np

inputFile = "inputs/input2.txt"

#part 1
colours = {"red": 12, "green": 13, "blue": 14}

sum = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        game, values = line.strip().split(":")
        possible = True
        for value in values.replace(";", ",").split(","):
            number, colour = value.strip().split(" ")
            if int(number) > colours[colour]:
                possible = False
                break
        if possible:
            sum += int(game.split(" ")[-1])


print("Part 1:", sum)


#part 2
sum = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        colours = {"red": 0, "green": 0, "blue": 0}
        _, values = line.strip().split(":")
        for value in values.replace(";", ",").split(","):
            number, colour = value.strip().split(" ")
            if int(number) > colours[colour]:
                colours[colour] = int(number)

        sum += np.prod(list(colours.values()))

print("Part 2:", sum)

