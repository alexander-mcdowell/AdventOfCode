import time

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
pos = None
i = 0
reading = True
for l in data:
    if (reading):
        if l == "":
            reading = False
            continue
        row = []
        j = 0
        for c in l:
            if (c == '@'):
                pos = (i, j)
                row.append('.')
            else: row.append(c)
            j += 1
        grid.append(row)
        i += 1
    else:
        for move in l:
            if (move == '<'): dir = 0
            elif (move == '^'): dir = 1
            elif (move == '>'): dir = 2
            else: dir = 3
            delta = [(0, -1), (-1, 0), (0, 1), (1, 0)][dir]
            pos2 = (pos[0] + delta[0], pos[1] + delta[1])
            if (0 <= pos2[0] < len(grid) and 0 <= pos2[1] < len(grid[0]) and grid[pos2[0]][pos2[1]] != '#'):
                if (grid[pos2[0]][pos2[1]] == '.'):
                    pos = pos2
                else:
                    start_block = (pos2[0], pos2[1])
                    k = 0
                    found_space = False
                    while True:
                        pos3 = (pos2[0] + delta[0], pos2[1] + delta[1])
                        if (not (0 <= pos3[0] < len(grid) and 0 <= pos3[1] < len(grid[0]))): break
                        if (grid[pos3[0]][pos3[1]] == '#'): break
                        if (grid[pos3[0]][pos3[1]] == '.'):
                            found_space = True
                            break
                        pos2 = pos3
                        k += 1
                    if (found_space):
                        for k2 in range(k, -1, -1):
                            grid[start_block[0] + delta[0] * (k2 + 1)][start_block[1] + delta[1] * (k2 + 1)] = 'O'
                        grid[start_block[0]][start_block[1]] = '.'
                        pos = start_block

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == 'O'): total += 100*i + j
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

def can_push(block_i, block_j, delta):
    global grid
    
    if (grid[block_i][block_j] == '.'): return True
    if (grid[block_i][block_j] == '#'): return False
    
    if (not (0 <= block_i + delta[0] < len(grid) and 0 <= block_j + delta[1] < len(grid[block_i]))): return False
    
    target_pos = (block_i + delta[0], block_j + delta[1])
    if (delta[0] == 0 and can_push(target_pos[0], target_pos[1], delta)): return True
    if (delta[1] == 0 and can_push(target_pos[0], target_pos[1], delta)):
        if (grid[block_i][block_j] == '[' and can_push(target_pos[0], target_pos[1] + 1, delta)): return True
        if (grid[block_i][block_j] == ']' and can_push(target_pos[0], target_pos[1] - 1, delta)): return True
        return False

    return False

pushed = set()
def push(block_i, block_j, delta):
    global grid
    
    if ((block_i, block_j) in pushed): return
    pushed.add((block_i, block_j))
    
    if (grid[block_i][block_j] in ['.', '#']): return
    
    # Push the block that's ahead of this one
    push(block_i + delta[0], block_j + delta[1], delta)
    
    # If pushing up/down
    if (delta[1] == 0):
        if (grid[block_i][block_j] == '['): push(block_i, block_j + 1, delta)
        else: push(block_i, block_j - 1, delta)
    grid[block_i + delta[0]][block_j + delta[1]] = grid[block_i][block_j]
    grid[block_i][block_j] = '.'

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
pos = None
i = 0
reading = True
grid = []
for l in data:
    if (reading):
        if l == "":
            reading = False
            continue
        j = 0
        row = []
        for c in l:
            if (c == '@'):
                row += ['.', '.']
                pos = (i, j)
            elif (c == 'O'): row += ['[', ']']
            else: row += [c, c]
            j += 2
        grid.append(row)
        i += 1
    else:
        for move in l:
            if (move == '<'): dir = 0
            elif (move == '^'): dir = 1
            elif (move == '>'): dir = 2
            else: dir = 3
            delta = [(0, -1), (-1, 0), (0, 1), (1, 0)][dir]
            pos2 = (pos[0] + delta[0], pos[1] + delta[1])
            if (0 <= pos2[0] < len(grid) and 0 <= pos2[1] < len(grid[0]) and grid[pos2[0]][pos2[1]] != '#'):
                if (grid[pos2[0]][pos2[1]] == '.'):
                    pos = pos2
                elif (can_push(pos2[0], pos2[1], delta)):
                    pushed = set()
                    push(pos2[0], pos2[1], delta)
                    pos = pos2

total = 0
for i in range(len(grid)):
    j = 0
    while j < len(grid[i]):
        if (grid[i][j] == '['):
            total += 100*i + j
            j += 1
        j += 1
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")