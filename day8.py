import numpy as np

inputFile = 'inputs/input8.txt'

#part 1

sequence = []
network = {}

with open(inputFile, "r") as file:
    sequence = file.readline().strip()
    file.readline()
    for line in file.readlines():
        source, destinations = line.strip().split('=')
        destinations = [destinations[2:5], destinations[7:10]]
        network[source.strip()] = destinations

node = 'AAA'
steps = 0
while node != 'ZZZ':
    for instruction in sequence:
        if instruction == 'L':
            node = network[node][0]
        else:
            node = network[node][1]
        steps += 1
        if node == 'ZZZ':
            break
        
print('Part 1:', steps)


#part 2

#only way to get to all of the finishing points is to go right 4 times
#the only 4+ R's (RRRR) are at the end of the sequence
#does not feel like the intended solution as it only works by inspecting the data
#therefore only working for this specific input and fails on other ones

sequence = []
network = {}
sequence_network = {}
nodes = []

with open(inputFile, "r") as file:
    sequence = file.readline().strip()
    file.readline()
    for line in file.readlines():
        source, destinations = line.strip().split('=')
        destinations = [destinations[2:5], destinations[7:10]]
        network[source.strip()] = destinations
        if source.strip()[-1] == 'A':
            nodes.append(source.strip())

print('Starting nodes:', nodes)
for starting_node in network:
    node = starting_node
    for instruction in sequence:
        if instruction == 'L':
            node = network[node][0]
        else:
            node = network[node][1]
    sequence_network[starting_node] = node


starting_node_results = {}
for starting_node in nodes:
    steps = 0
    node = starting_node
    while node[-1] != 'Z':
        node = sequence_network[node]
        steps += len(sequence)
    starting_node_results[starting_node] = (node, steps, steps / len(sequence))

print('The final node, number of steps and sequences to get to a final node from the starting nodes:\n', starting_node_results)

ending_nodes = [node for (node,_,_) in starting_node_results.values()]
ending_node_results = {}

for starting_node in ending_nodes:
    steps = 0
    node = starting_node
    while node[-1] != 'Z' or steps == 0:
        node = sequence_network[node]
        steps += len(sequence)
    ending_node_results[starting_node] = (node, steps, steps / len(sequence))

print('The final node, number of steps and sequences to get to a final node from the starting nodes:\n', ending_node_results)
        
print('Part 2:', 281 * int(np.prod([x for (_,_,x) in ending_node_results.values()])))