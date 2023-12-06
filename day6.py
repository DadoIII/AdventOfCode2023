import numpy as np
import math

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


print("Part 1:", np.prod(ways_to_win))

#part2
def find_lower_bound(low, high, time, distance):
    current = math.floor((low + high) / 2)
    last = (current == low or current == high)
    #good time and no more numbers to search
    if current * (time - current) > distance and last:
        return current
    #good time and more numbers to search (go lower)
    elif current * (time - current) > distance and not last:
        next = find_lower_bound(low, current, time, distance)
        return current if next == None else next
    #bad time and more numbers to search (go higher)
    elif current * (time - current) <= distance and not last:
        return find_lower_bound(current, high, time, distance)
    #bad time and no more numbers to search
    else:
        return None
    

def find_upper_bound(low, high, time, distance):
    current = math.ceil((low + high) / 2)
    last = (current == low or current == high)
    #good time and no more numbers to search
    if current * (time - current) > distance and last:
        return current
    #good time and more numbers to search (go higher)
    elif current * (time - current) > distance and not last:
        next = find_upper_bound(current, high, time, distance)
        return current if next == None else next
    #bad time and more numbers to search (go lower)
    elif current * (time - current) <= distance and not last:
        return find_upper_bound(low, current, time, distance)
    #bad time and no more numbers to search
    else:
        return None

with open(inputFile, "r") as file:

    time = int(''.join([x for x in file.readline().strip().split(":")[-1].strip().split(" ") if x.isdigit()]))
    distance = int(''.join([x for x in file.readline().strip().split(":")[-1].strip().split(" ") if x.isdigit()]))
    
    middle = time // 2
    #logarithmic search for upper and lower bound
    lower = find_lower_bound(0, middle, time, distance)
    upper = find_upper_bound(middle, time, time, distance)

    print("Part 2:", upper - lower + 1)
