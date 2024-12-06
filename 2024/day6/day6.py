import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
pos = None
dir = 0
i = 0
for l in data:
    row = []
    j = 0
    for x in l:
        if (x == "^"): pos = (i, j)
        row.append(x)
        j += 1
    grid.append(row)
    i += 1
pos_list = set()
while True:
    pos_list.add(pos)
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
    if (not (0 <= pos[0] + delta[1] < len(grid)) or not (0 <= pos[1] + delta[0] < len(grid[0]))):
        break
    elif (grid[pos[0] + delta[1]][pos[1] + delta[0]] == "#"):
        dir = (dir + 1)%4
        delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
    else: pos = (pos[0] + delta[1], pos[1] + delta[0])
print(len(pos_list))
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
start_pos = None
i = 0
for l in data:
    row = []
    j = 0
    for x in l:
        if (x == "^"): start_pos = (i, j)
        row.append(x)
        j += 1
    grid.append(row)
    i += 1

used = set()
pos = start_pos
dir = 0
while True:
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
    if (not (0 <= pos[0] + delta[1] < len(grid)) or not (0 <= pos[1] + delta[0] < len(grid[0]))):
        break
    else:
        used.add((pos[0] + delta[1], pos[1] + delta[0]))
        if (grid[pos[0] + delta[1]][pos[1] + delta[0]] == "#"):
            dir = (dir + 1)%4
            delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
        else: pos = (pos[0] + delta[1], pos[1] + delta[0])

count = 0
for obstruct_pos in used:
    obstruct_i, obstruct_j = obstruct_pos
    if (grid[obstruct_i][obstruct_j] == '#'): continue
    if (grid[obstruct_i][obstruct_j] == '^'): continue
    grid[obstruct_i][obstruct_j] = '#'
    pos_list = set()
    pos = start_pos
    dir = 0
    looped = False
    while True:
        if ((pos, dir) in pos_list):
            looped = True
            break
        pos_list.add((pos, dir))
        delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
        if (not (0 <= pos[0] + delta[1] < len(grid)) or not (0 <= pos[1] + delta[0] < len(grid[0]))):
            break
        elif (grid[pos[0] + delta[1]][pos[1] + delta[0]] == "#"):
            dir = (dir + 1)%4
            delta = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]
        else: pos = (pos[0] + delta[1], pos[1] + delta[0])
    if (looped): count += 1
    grid[obstruct_i][obstruct_j] = '.'
print(count)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()