import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
start_poses = []
i = 0
for l in data:
    row = []
    j = 0
    for x in l:
        if (x == '.'): y = -1
        else: y = int(x)
        if (y == 0): start_poses.append((i, j))
        row.append(y)
        j += 1
    grid.append(row)
    i += 1

# DFS
N, M = len(grid), len(grid[0])
score = 0
for start_pos in start_poses:
    stack = [start_pos]
    seen = set()
    while len(stack) != 0:
        i, j = stack.pop(-1)
        if ((i, j) in seen): continue
        seen.add((i, j))
        for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i2, j2 = i + delta[0], j + delta[1]
            if (0 <= i2 < N and 0 <= j2 < M and (grid[i2][j2] - grid[i][j]) == 1 and (i2, j2) not in seen):
                if (grid[i2][j2] == 9):
                    score += 1
                stack.append((i2, j2))
print(score)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
start_poses = []
i = 0
for l in data:
    row = []
    j = 0
    for x in l:
        if (x == '.'): y = -1
        else: y = int(x)
        if (y == 0): start_poses.append((i, j))
        row.append(y)
        j += 1
    grid.append(row)
    i += 1

# DFS
N, M = len(grid), len(grid[0])
score = 0
total_rating = 0
for start_pos in start_poses:
    stack = [start_pos]
    paths = [[0 for _ in range(M)] for _ in range(N)]
    while len(stack) != 0:
        i, j = stack.pop(-1)
        paths[i][j] += 1
        seen.add((i, j))
        for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i2, j2 = i + delta[0], j + delta[1]
            if (0 <= i2 < N and 0 <= j2 < M and (grid[i2][j2] - grid[i][j]) == 1):
                stack.append((i2, j2))
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 9: total_rating += paths[i][j]
print(total_rating)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")