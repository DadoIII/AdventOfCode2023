inputFile = "inputs/input5.txt"

#part 1

seeds = []
maps = [] #keep track of the mappings 

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

maps = [] #keep track of the mappings

def get_seed_ranges(input):
    seed_ranges = []
    for i in range(0, len(input), 2):
        seed_ranges.append([input[i], input[i+1]])
    return seed_ranges


def convert_ranges(seed_ranges):
    new_ranges = []
    #destination and source start are the starting points of these ranges
    # map_range is the length of both of these ranges
    for destination_start, source_start, map_range in maps:
        source_end = source_start + map_range
        #seed start is the start of the seed range and seed_range is the length of the range
        for (i, [seed_start, seed_range]) in enumerate(seed_ranges):
            seed_end = seed_start + seed_range
            #seed range is fully inside the map range
            if seed_start >= source_start and seed_end <= source_end:
                new_ranges.append([destination_start + (seed_start - source_start), seed_range]) #create the mapping
                seed_ranges[i] = [0, 0] #delete the old range

            #the end of the seed range is outside of the map range
            elif seed_start >= source_start and seed_start <= source_end:
                new_ranges.append([destination_start + (seed_start - source_start), source_end - seed_start]) #create the mapping
                seed_ranges[i] = [source_end, seed_end - source_end] #keep the rest of the range that is outside of the mapping range

            #the start of the seed range is outside of the map range
            elif seed_end >= source_start and seed_end <= source_end:
                new_ranges.append([destination_start, seed_end - source_start]) #create the mapping
                seed_ranges[i] = [seed_start, source_start - seed_start] #keep the rest of the range that is outside of the mapping range
            
            #a middle part of the seed range is inside the map range
            elif seed_start < source_start and seed_end > source_end:
                new_ranges.append([destination_start, map_range]) #create the mapping
                seed_ranges[i] = [seed_start, source_start - seed_start] #keep the rest of the range that is outside of the mapping range
                seed_ranges.append([source_end, seed_end - source_end]) #keep the rest of the range that is outside of the mapping range
            #not in the map range at all
            else:
                pass

    #keep the ranges that were not mapped 
    return new_ranges + [x for x in seed_ranges if x != [0, 0]]


with open(inputFile, "r") as file:
    line = file.readline().strip()
    seed_ranges = get_seed_ranges([int(x) for x in line.split(":")[-1].strip().split(" ")])
    line = file.readline()
    while line:
        maps = []
        #add all of the mappings for a single step
        while line != "\n" and line:
            if line.strip()[-1] != ":":
                maps.append([int(x) for x in line.strip().split(" ")])
            line = file.readline()
        #convert the ranges
        seed_ranges = convert_ranges(seed_ranges)
        line = file.readline()

    print(min([x for x,_ in seed_ranges]))