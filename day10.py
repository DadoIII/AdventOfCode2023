from enum import Enum

inputFile = 'inputs/input10.txt'

#part 1

#y, x
class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

DIRECTIONS_OPPOSITE = {Directions.UP: Directions.DOWN,
                       Directions.DOWN: Directions.UP,
                       Directions.RIGHT: Directions.LEFT,
                       Directions.LEFT: Directions.RIGHT}

class Pipes(Enum):
    HORIZONTAL = '-'
    VERTICAL = '|'
    TOPLEFT = 'J'
    TOPRIGHT = 'L'
    BOTTOMLEFT = '7'
    BOTTOMRIGHT = 'F'
    START = 'S'

PIPE_DIRECTIONS = {Pipes.HORIZONTAL:  [Directions.LEFT, Directions.RIGHT],
                   Pipes.VERTICAL:    [Directions.UP, Directions.DOWN],
                   Pipes.TOPLEFT:     [Directions.UP, Directions.LEFT],
                   Pipes.TOPRIGHT:    [Directions.UP, Directions.RIGHT],
                   Pipes.BOTTOMLEFT:  [Directions.DOWN, Directions.LEFT],
                   Pipes.BOTTOMRIGHT: [Directions.DOWN, Directions.RIGHT],
                   Pipes.START:       [Directions.DOWN, Directions.UP, Directions.LEFT, Directions.RIGHT]
                   }

directions = (Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT)

#add 2d vectors
def add(pos: (int, int), direction: Directions) -> (int, int):
    return (pos[0] + direction.value[0], pos[1] + direction.value[1])

#find one of the 2 starting directions
def find_connection(pos: (int, int)) -> (int, int):
    for direction in directions:
        adjecent_pos = add(pos, direction)
        #not out of bounds
        if adjecent_pos[0] >= 0 and adjecent_pos[1] >= 0 and adjecent_pos[0] < 140 and adjecent_pos[1] < 140:
            adjecent = ground[adjecent_pos[0]][adjecent_pos[1]]
            match direction:
                case Directions.UP:
                    if adjecent == Pipes.VERTICAL.value or adjecent == Pipes.BOTTOMLEFT.value or adjecent == Pipes.BOTTOMRIGHT.value:
                        return Directions.UP
                case Directions.DOWN:
                    if adjecent == Pipes.VERTICAL.value or adjecent == Pipes.TOPLEFT.value or adjecent == Pipes.TOPRIGHT.value:
                        return Directions.DOWN 
                case Directions.LEFT:
                    if adjecent == Pipes.HORIZONTAL.value or adjecent == Pipes.BOTTOMRIGHT.value or adjecent == Pipes.TOPRIGHT.value:
                        return Directions.LEFT
                case Directions.RIGHT:
                    if adjecent == Pipes.HORIZONTAL.value or adjecent == Pipes.BOTTOMLEFT.value or adjecent == Pipes.TOPLEFT.value:
                        return Directions.RIGHT
        return None

#find the next position and direction based on the direction of entry
def next_step(pos: (int, int), direction: Directions) -> ((int, int), Directions):
    next_pos = add(pos, direction)
    next_pipe = ground[next_pos[0]][next_pos[1]]

    #get the next direction of the pipe
    pipe_directions = PIPE_DIRECTIONS[Pipes(next_pipe)]
    next_direction = [x for x in pipe_directions if x != DIRECTIONS_OPPOSITE[direction]][0]

    return next_pos, next_direction


#y, x
start = (0,0)
ground = []
loop = []   #u2d list of bools indicating whether the spot is part of the pipe loop or not, used in part 2

with open(inputFile, 'r') as file:
    for i, line in enumerate(file.readlines()):
        row = [x for x in line.strip()]
        row2 = [False for _ in line.strip()]    #used in part 2
        if 'S' in row:
            start = (i, row.index('S'))
        ground.append(row)
        loop.append(row2)


direction = find_connection(start)  #find a connecting pipe from the start
current_pos, direction = next_step(start, direction)
loop[current_pos[0]][current_pos[1]] = True    #used for part 2
length = 1

#find the length of the pipe loop and divide by 2 to get the answer
while ground[current_pos[0]][current_pos[1]] != 'S':
    current_pos, direction = next_step(current_pos, direction)
    loop[current_pos[0]][current_pos[1]] = True    #used for part 2
    length += 1


print('Part 1:', length // 2)

#part 2


#search each row, count as inside when the number of horizontal pipes before it is odd
#|.| is inside
#||.|| is outside
#there can be a complex horizontal pipe such as F-J, but F-7 is not as it goes back down
#F-J.| is inside
#L--J. is outside
#these can be combined
#L7F7.| is inside
#|F7F-J.|F-J is outside
total = 0
for y in range(len(ground)):
    pipe_count = 0
    pipe = None
    for x in range(len(ground[y])):
        place = ground[y][x]
        part_of_loop = loop[y][x]

        if not part_of_loop and pipe_count % 2 == 1:
            total += 1
        
        if part_of_loop:
            if place in ['|', 'S']:
                pipe_count += 1
            elif place == 'F':
                pipe = 'down'
            elif place == 'L':
                pipe = 'up'
            elif place == 'J':
                if pipe == 'down':
                    pipe_count += 1
                pipe = None
            elif place == "7":
                if pipe == 'up':
                    pipe_count += 1
                pipe = None



print('Part 2:', total)