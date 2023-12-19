from enum import Enum
from collections import deque
import math

# Input file
inputFile = 'inputs/test17-2.txt'

class Direction(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


# Part 1
# Looks like bfs that is looking for a optimal path is not even close to being fast enough


class Space():
    def __init__(self, heat_loss, min_heat_loss):
        self.heat_loss = heat_loss
        self.min_heat_loss_horizontal = min_heat_loss  # Minimum heat loss to get to this space so far with an ending horizontal move
        self.min_heat_loss_vertical = min_heat_loss  # Minimum heat loss to get to this space so far with an ending vertical move

map_height, map_width = 0, 0
best_heat_loss = 0

# def closest_heat_loss(x: int, y: int) -> int:
#     # Returns the worst possible heat loss to get to the end given a position
#     x_distance = map_width - x
#     y_distance = map_height - y
#     # Can use a most efficient path
#     if x_distance * 3 >= y_distance and y_distance * 3 >= x_distance:
#         return (x_distance + y_distance) * 9
    
#     # Y distance is a lot greater, has to make some inefficient moves along the x axis
#     elif x_distance * 3 < y_distance:
#         efficient_distance = (x_distance) * 3
#         extra_moves = math.ceil((y_distance - efficient_distance) / 3)
#         return (x_distance + y_distance) * 9 + extra_moves
    
#     # X distance is a lot greater, has to make some inefficient moves along the y axis
#     elif y_distance * 3 < x_distance:
#         efficient_distance = (y_distance) * 3
#         extra_moves = math.ceil((x_distance - efficient_distance) / 3)
#         return (x_distance + y_distance) * 9 + extra_moves

#info is x, y, heat loss so far, Direction
def bfs(info: (int, int, int, Direction)) -> int:

    queue = deque([info])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node from the queue
        #print(node)
        x, y = node[0], node[1]
        space = heat_map[y][x]
        heat_loss_so_far = node[2]
        direction = node[3]
        

        if direction == Direction.VERTICAL:

            if space.min_heat_loss_vertical >= heat_loss_so_far:
                space.min_heat_loss_vertical = heat_loss_so_far

            cumulative_loss_left = 0
            cumulative_loss_right = 0
            for i in [1, 2, 3]:
                if x - i >= 0:
                    cumulative_loss_left += heat_map[y][x-i].heat_loss
                    if heat_map[y][x-i].min_heat_loss_horizontal >= heat_loss_so_far + cumulative_loss_left:
                        queue.append((x-i, y, heat_loss_so_far + cumulative_loss_left, Direction.HORIZONTAL))
                if x + i < map_width:
                    cumulative_loss_right += heat_map[y][x+i].heat_loss
                    if heat_map[y][x+i].min_heat_loss_horizontal >= heat_loss_so_far + cumulative_loss_right:
                        queue.append((x+i, y, heat_loss_so_far + cumulative_loss_right, Direction.HORIZONTAL))
  
        if direction == Direction.HORIZONTAL:

            if space.min_heat_loss_horizontal >= heat_loss_so_far:
                space.min_heat_loss_horizontal = heat_loss_so_far

            cumulative_loss_up = 0
            cumulative_loss_down = 0
            for i in [1, 2, 3]:
                if y - i >= 0:
                    cumulative_loss_up += heat_map[y-i][x].heat_loss
                    if heat_map[y-i][x].min_heat_loss_vertical >= heat_loss_so_far + cumulative_loss_up:
                        queue.append((x, y-i, heat_loss_so_far + cumulative_loss_up, Direction.VERTICAL))

                if y + i < map_height:
                    cumulative_loss_down += heat_map[y+i][x].heat_loss
                    if heat_map[y+i][x].min_heat_loss_vertical >= heat_loss_so_far + cumulative_loss_down:
                        queue.append((x, y+i, heat_loss_so_far + cumulative_loss_down, Direction.VERTICAL))

heat_map = []

with open(inputFile, 'r') as file:
    for line in file:
        heat_map.append([Space(int(x), 1_000_000) for x in line.strip()])
    map_height = len(heat_map)
    map_width = len(heat_map[0])

    bfs((0, 0, 0, Direction.HORIZONTAL))
    print('-------------')
    bfs((0, 0, 0, Direction.VERTICAL))

result = heat_map[map_height - 1][map_width - 1].min_heat_loss_vertical
result2 = heat_map[map_height - 1][map_width - 1].min_heat_loss_horizontal
print(f'Part 1: {min(result, result2)}')

