import numpy as np

inputFile = "inputs/input6.txt"

#part 1
ways_to_win = []

with open(inputFile, "r") as file:

    times = [int(x) for x in file.readline().strip().split(":")[-1].strip().split(" ") if x.isdigit()]
    distances = [int(x) for x in file.readline().strip().split(":")[-1].strip().split(" ") if x.isdigit()]

    for time, distance in zip(times, distances):
        wins = 0
        for i in range(time):
            if i * (time - i) > distance:
                wins += 1
        ways_to_win.append(wins)


print(np.prod(ways_to_win))
