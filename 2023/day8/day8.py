import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
instruction = data[0]
nodes = {}
for line in data[2:]:
    node, maps = line.split(" = ")
    maps = maps.split(", ")
    nodes[node] = (maps[0][1:], maps[1][:-1])
i = 0
steps = 1
curr = 'AAA'
while True:
    inst = instruction[i]
    curr = nodes[curr][['L', 'R'].index(inst)]
    if (curr == 'ZZZ'):
        print(steps)
        break
    i += 1
    if (i == len(instruction)): i = 0
    steps += 1
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

import math

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
instruction = data[0]
nodes = {}
for line in data[2:]:
    node, maps = line.split(" = ")
    maps = maps.split(", ")
    nodes[node] = (maps[0][1:], maps[1][:-1])
i = 0
steps = 0
currents = [x for x in nodes if x[-1] == 'A']
cycle_lengths = [None for _ in range(len(currents))]
end = False
while not end:
    inst = instruction[i]
    for j in range(len(currents)):
        currents[j] = nodes[currents[j]][['L', 'R'].index(inst)]
    steps += 1
    for j in range(len(currents)):
        x = currents[j]
        if (x[-1] == 'Z' and cycle_lengths[j] == None):
            cycle_lengths[j] = steps
            if (all([y!=None for y in cycle_lengths])):
                lcm = 1
                for y in cycle_lengths: lcm *= y // math.gcd(y, lcm)
                print(lcm)
                end = True
                break
    i += 1
    if (i == len(instruction)): i = 0
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")