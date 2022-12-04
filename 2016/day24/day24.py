##########
# PART 1 #
##########

"""
data = open("day24in.txt").read().split("\n")
targets = {}
grid = []
y = 0
for line in data:
    grid.append([])
    x = 0
    for c in line:
        if (ord('0') <= ord(c) <= ord('9')):
            targets[int(c)] = (x, y)
            grid[-1].append(0)
        else: grid[-1].append(int(c == '#'))
        x += 1
    y += 1

def a_star(start, target, grid):
    n, m = len(grid), len(grid[0])
    cost_grid = [[1000000000 for _ in range(m)] for _ in range(n)]
    cost_grid[start[1]][start[0]] = 0
    step_grid = [[-1 for _ in range(m)] for _ in range(n)]
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
            if (v[0] < 0 or v[0] >= m or v[1] < 0 or v[1] >= n or grid[v[1]][v[0]] == 1): continue

            if (cost_grid[u[1]][u[0]] + heuristic < cost_grid[v[1]][v[0]]):
                cost_grid[v[1]][v[0]] = cost_grid[u[1]][u[0]] + heuristic
                step_grid[v[1]][v[0]] = 1 + step_grid[u[1]][u[0]]
                if (v not in visited): queue.append(v)
    return step_grid[target[1]][target[0]]

cost_map = {}
for i in range(len(targets)):
    for j in range(i + 1, len(targets)):
        if (i not in cost_map): cost_map[i] = []
        if (j not in cost_map): cost_map[j] = []
        cost = a_star(targets[i], targets[j], grid)
        cost_map[i].append((j, cost))
        cost_map[j].append((i, cost))

def find_min_cost(u, cost_map, visited = []):
    min_cost = 0
    for x in cost_map[u]:
        v, c = x
        if (v not in visited):
            new_cost = c + find_min_cost(v, cost_map, visited + [u])
            if (min_cost == 0 or new_cost < min_cost): min_cost = new_cost
    return min_cost

print(find_min_cost(0, cost_map))
"""

##########
# PART 2 #
##########

data = open("day24in.txt").read().split("\n")
targets = {}
grid = []
y = 0
for line in data:
    grid.append([])
    x = 0
    for c in line:
        if (ord('0') <= ord(c) <= ord('9')):
            targets[int(c)] = (x, y)
            grid[-1].append(0)
        else: grid[-1].append(int(c == '#'))
        x += 1
    y += 1

def a_star(start, target, grid):
    n, m = len(grid), len(grid[0])
    cost_grid, step_grid, visited = [], [], []
    
    for _ in range(n):
        cost_grid.append([])
        step_grid.append([])
        visited.append([])
        for _ in range(m):
            cost_grid[-1].append(1000000000)
            step_grid[-1].append(-1)
            visited[-1].append(False)
    cost_grid[start[1]][start[0]] = 0
    step_grid[start[1]][start[0]] = 0

    queue = [start]
    while (len(queue) != 0):
        best_cost, u = 10000000000000, None
        for x in queue:
            if (cost_grid[x[1]][x[0]] < best_cost):
                u = x
                best_cost = cost_grid[x[1]][x[0]]
        if (u == None): break
        if (u == target): break
        queue.remove(u)
        visited[u[1]][u[0]] = True
        
        for v in [(u[0], u[1] - 1), (u[0], u[1] + 1), (u[0] - 1, u[1]), (u[0] + 1, u[1])]:
            heuristic = abs(target[1] - v[1]) + abs(target[0] - v[0])
            if (v[0] < 0 or v[0] >= m or v[1] < 0 or v[1] >= n or grid[v[1]][v[0]] == 1): continue

            if (cost_grid[u[1]][u[0]] + heuristic < cost_grid[v[1]][v[0]]):
                cost_grid[v[1]][v[0]] = cost_grid[u[1]][u[0]] + heuristic
                step_grid[v[1]][v[0]] = 1 + step_grid[u[1]][u[0]]
                if (not visited[v[1]][v[0]]): queue.append(v)
    return step_grid[target[1]][target[0]]

cost_map = {}
for i in range(len(targets)):
    for j in range(i + 1, len(targets)):
        if (i not in cost_map): cost_map[i] = []
        if (j not in cost_map): cost_map[j] = []
        cost = a_star(targets[i], targets[j], grid)
        cost_map[i].append((j, cost))
        cost_map[j].append((i, cost))

def find_min_cost(u, cost_map, n, visited = []):
    if (len(visited) == (n - 1)):
        for x in cost_map[u]:
            if (x[0] == 0): return x[1]

    min_cost = 0
    for x in cost_map[u]:
        v, c = x
        if (v not in visited):
            new_cost = c + find_min_cost(v, cost_map, n, visited + [u])
            if (min_cost == 0 or new_cost < min_cost): min_cost = new_cost
    return min_cost

print(find_min_cost(0, cost_map, len(targets)))