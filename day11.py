inputFile = 'inputs/input11.txt'

# Part 1 and 2
MILLION = 1_000_000
galaxies1 = []  # Positions of the galaxies [y,x]
galaxies2 = []  # Positions of galaxies for part 2
empty_columns = [i for i in range(141)]  # Track the possible empty columns

with open(inputFile, 'r') as file:
    empty_rows = 0  # Keep track of empty rows so far
    for y, line in enumerate(file.readlines()):
        empty_row = True
        for x, space in enumerate(line):    
            if space == '#':  # Found galaxy
                galaxies1.append([y + empty_rows, x])
                galaxies2.append([y + empty_rows * (MILLION - 1), x])
                empty_row = False
                if x in empty_columns:  # Remove column as possibly empty
                    empty_columns.remove(x)
        if empty_row:
            empty_rows += 1

# ----- Expand distances between columns -----
for i, [y, x] in enumerate(galaxies1):
    expansions = len([column for column in empty_columns if column < x])
    galaxies1[i] = [y, x + expansions]

for i, [y, x] in enumerate(galaxies2):
    expansions = len([column for column in empty_columns if column < x])
    galaxies2[i] = [y, x + expansions * (MILLION - 1)]
# --------------------------------------------

# ------ Calculate the total distances -------
total_distance1 = 0
for i, [y1, x1] in enumerate(galaxies1[:-1]):
    for [y2, x2] in galaxies1[i+1:]:
        total_distance1 += abs(y1-y2) + abs(x1-x2)

total_distance2 = 0
for i, [y1, x1] in enumerate(galaxies2[:-1]):
    for [y2, x2] in galaxies2[i+1:]:
        total_distance2 += abs(y1-y2) + abs(x1-x2)
# --------------------------------------------

print('Part 1:', total_distance1)
print('Part 1:', total_distance2)