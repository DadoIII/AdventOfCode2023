inputFile = "inputs/input5.txt"

#part 1

seeds = []
maps = []

def convert():
    global seeds
    for i, seed in enumerate(seeds):
        for destination, source, range in maps:
            if seed >= source and seed < source + range:
                seeds[i] = destination + (seed - source)
                break


with open(inputFile, "r") as file:
    line = file.readline().strip()
    seeds = [int(x) for x in line.split(":")[-1].strip().split(" ")]
    line = file.readline()
    while line:
        maps = []
        while line != "\n" and line:
            if line.strip()[-1] != ":":
                maps.append([int(x) for x in line.strip().split(" ")])
            line = file.readline()

        convert()
        line = file.readline()


    print(min(seeds))

#part 2
