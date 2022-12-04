##########
# PART 1 #
##########

"""
# A* algorithm

num = int(open("day13in.txt").read().split("\n")[0])
N = 75
grid = []
for y in range(N):
    grid.append([])
    for x in range(N):
        k = num + x * (x + 3 + 2 * y) + y * (1 + y)
        count = bin(k)[2:].count('1')
        if (count % 2 == 0): grid[-1].append(' ')
        else: grid[-1].append('#')

start = (1, 1)
target = (31, 39)
cost_grid = [[1000000000 for _ in range(N)] for _ in range(N)]
cost_grid[start[1]][start[0]] = 0
step_grid = [[-1 for _ in range(N)] for _ in range(N)]
step_grid[start[1]][start[0]] = 0

queue = [start]
visited = []
while (len(queue) != 0):
    best_cost, u = 10000000000000, None
    for x in queue:
        if (cost_grid[x[1]][x[0]] < best_cost):
            u = x
            best_cost = cost_grid[x[1]][x[0]]
    if (u == None): break
    if (u == target): break
    queue.remove(u)
    visited.append(u)
    
    for v in [(u[0], u[1] - 1), (u[0], u[1] + 1), (u[0] - 1, u[1]), (u[0] + 1, u[1])]:
        heuristic = abs(target[1] - v[1]) + abs(target[0] - v[0])
        if (v[0] < 0 or v[0] >= N or v[1] < 0 or v[1] >= N or grid[v[1]][v[0]] == '#'): continue

        if (cost_grid[u[1]][u[0]] + heuristic < cost_grid[v[1]][v[0]]):
            cost_grid[v[1]][v[0]] = cost_grid[u[1]][u[0]] + heuristic
            step_grid[v[1]][v[0]] = 1 + step_grid[u[1]][u[0]]
            if (v not in visited): queue.append(v)

print(step_grid[target[1]][target[0]])
"""

##########
# PART 2 #
##########

# Dijkstra's algorithm

num = int(open("day13in.txt").read().split("\n")[0])
N = 100
grid = []
for y in range(N):
    grid.append([])
    for x in range(N):
        k = num + x * (x + 3 + 2 * y) + y * (1 + y)
        count = bin(k)[2:].count('1')
        if (count % 2 == 0): grid[-1].append(' ')
        else: grid[-1].append('#')

start = (1, 1)
step_grid = [[10000000000 for _ in range(N)] for _ in range(N)]
step_grid[start[1]][start[0]] = 0

queue = [start]
visited = []
while (len(queue) != 0):
    best_cost, u = 10000000000000, None
    for x in queue:
        if (step_grid[x[1]][x[0]] < best_cost):
            u = x
            best_cost = step_grid[x[1]][x[0]]
    if (u == None): break
    queue.remove(u)
    visited.append(u)
    
    for v in [(u[0], u[1] - 1), (u[0], u[1] + 1), (u[0] - 1, u[1]), (u[0] + 1, u[1])]:
        if (v[0] < 0 or v[0] >= N or v[1] < 0 or v[1] >= N or grid[v[1]][v[0]] == '#'): continue

        if (step_grid[u[1]][u[0]] + 1 < step_grid[v[1]][v[0]]):
            step_grid[v[1]][v[0]] = 1 + step_grid[u[1]][u[0]]
            if (v not in visited and step_grid[v[1]][v[0]] < 50): queue.append(v)

count = 0
for i in range(N):
    for j in range(N):
        if (step_grid[i][j] <= 50): count += 1
print(count)