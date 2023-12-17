from enum import Enum
inputFile = 'inputs/input16.txt'

class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

# Part 1

class Tile():
    energised_total = 0
    tiles = []

    def __init__(self):
        self.energised = False
        Tile.tiles.append(self)

    def isEnergised(self):
        return self.energised
    
    def energise(self):
        if not self.energised:
            self.energised = True
            Tile.energised_total += 1

    def next_move(self, direction):
        self.energise()
        return direction
    
    def get_energised_total(self):
        return self.energised_total
    
    def discharge(self):
        self.energised = False

    @classmethod
    def reset(cls):
        for tile in cls.tiles:
            tile.discharge()
        cls.energised_total = 0

class LeftDownMirror(Tile):
    def __init__(self):
        super().__init__()

    def next_move(self, direction):
        self.energise()
        if direction == Direction.UP:
            return Direction.LEFT
        elif direction == Direction.RIGHT:
            return Direction.DOWN
        elif direction == Direction.DOWN:
            return Direction.RIGHT
        elif direction == Direction.LEFT:
            return Direction.UP
        
class LeftUpMirror(Tile):
    def __init__(self):
        super().__init__()

    def next_move(self, direction):
        self.energise()
        if direction == Direction.UP:
            return Direction.RIGHT
        elif direction == Direction.RIGHT:
            return Direction.UP
        elif direction == Direction.DOWN:
            return Direction.LEFT
        elif direction == Direction.LEFT:
            return Direction.DOWN
    

class HorizontalSplitter(Tile):
    def __init__(self, x ,y):
        super().__init__()
        self.usedSplit = False
        self.x = x
        self.y = y

    def next_move(self, direction):
        self.energise()

        if direction == Direction.LEFT or direction == Direction.RIGHT:
            return direction
        elif self.usedSplit:
            return None
        elif direction == Direction.UP or direction == Direction.DOWN:
            self.usedSplit = True
            beam = Beam(self.x, self.y, Direction.RIGHT)
            beam.move()
            return Direction.LEFT
        
    def discharge(self):
        self.energised = False
        self.usedSplit = False

class VerticalSplitter(Tile):
    def __init__(self, x, y):
        super().__init__()
        self.usedSplit = False
        self.x = x
        self.y = y

    def next_move(self, direction):
        self.energise()

        if direction == Direction.UP or direction == Direction.DOWN:
            return direction
        elif self.usedSplit:
            return None
        elif direction == Direction.LEFT or direction == Direction.RIGHT:
            self.usedSplit = True
            beam = Beam(self.x, self.y, Direction.DOWN)
            beam.move()
            return Direction.UP
        
    def discharge(self):
        self.energised = False
        self.usedSplit = False

        
class Beam():
    all_beams = []

    def __init__(self, x, y, direction):
        self.all_beams.append(self)
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == Direction.UP and self.y > 0:
            self.y -= 1
        elif self.direction == Direction.DOWN and self.y < len(board) - 1:
            self.y += 1
        elif self.direction == Direction.LEFT and self.x > 0:
            self.x -= 1
        elif self.direction == Direction.RIGHT and self.x < len(board[0]) - 1:
            self.x += 1
        else:
            self.destroy()

    def next_move(self):
        tile = board[self.y][self.x]
        self.direction = tile.next_move(self.direction)
        self.move()


    def destroy(self):
        self.all_beams.remove(self)


board = []

with open(inputFile, 'r') as file:
    for y, line in enumerate(file):
        row = []
        for x, character in enumerate(line):
            if character == '.':
                row.append(Tile())
            elif character == '\\':
                row.append(LeftDownMirror())
            elif character == '/':
                row.append(LeftUpMirror())
            elif character == '-':
                row.append(HorizontalSplitter(x, y))
            elif character == '|':
                row.append(VerticalSplitter(x, y))
        board.append(row)

left_max = 0
for i in range(len(board)):
    Beam(0,i, Direction.RIGHT)

    while Beam.all_beams:
        for beam in Beam.all_beams[:]:  # Iterate over a copy of the list to avoid modifying it during iteration
            beam.next_move()

    if left_max < Tile.energised_total:
        left_max = Tile.energised_total 

    print(f'Part 1-{i}:', Tile.energised_total)

    Tile.reset()


up_max = 0
for i in range(len(board)):
    Beam(i,0, Direction.DOWN)

    while Beam.all_beams:
        for beam in Beam.all_beams[:]:  # Iterate over a copy of the list to avoid modifying it during iteration
            beam.next_move()

    if up_max < Tile.energised_total:
        up_max = Tile.energised_total 

    print(f'Part 1-{i}:', Tile.energised_total)

    Tile.reset()


right_max = 0
for i in range(len(board)):
    Beam(109,i, Direction.LEFT)

    while Beam.all_beams:
        for beam in Beam.all_beams[:]:  # Iterate over a copy of the list to avoid modifying it during iteration
            beam.next_move()

    if right_max < Tile.energised_total:
        right_max = Tile.energised_total 

    print(f'Part 1-{i}:', Tile.energised_total)

    Tile.reset()



down_max = 0
for i in range(len(board)):
    Beam(i,109, Direction.UP)

    while Beam.all_beams:
        for beam in Beam.all_beams[:]:  # Iterate over a copy of the list to avoid modifying it during iteration
            beam.next_move()

    if down_max < Tile.energised_total:
        down_max = Tile.energised_total 

    print(f'Part 1-{i}:', Tile.energised_total)

    Tile.reset()

print(f'Left max: {left_max}')
print(f'Up max: {up_max}')
print(f'Right max: {right_max}')
print(f'Down max: {down_max}')