import time
import heapq
import math

##########
# PART 1 #
##########

# def explore(u, target, grid, Blizzards):
#     n, m = len(grid), len(grid[0])
#     T = n * m // math.gcd(n, m)
#     queue = []
#     heapq.heappush(queue, (0, u))
#     visited = set()
#     while len(queue) != 0:
#         t, u = heapq.heappop(queue)
#         if (u == target): return t
#         t2 = t % T
#         if ((u, t2) not in visited):
#             visited.add((u, t2))
#             blizzard_poses = Blizzards[t2]
        
#             # Choose next
#             for k in [(1, 0), (0, -1), (-1, 0), (0, 1), (0, 0)]:
#                 v = (u[0] + k[0], u[1] + k[1])
#                 if (0 <= v[0] < n and 0 <= v[1] < m and grid[v[0]][v[1]] == '.'):
#                     if (v not in blizzard_poses): heapq.heappush(queue, (t + 1, v))

#     return None

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# grid = []
# blizzard_poses, blizzard_dirs = [], []
# i = 0
# for line in lines:
#     j = 0
#     row = []
#     for c in line:
#         if (c != '#'): row.append('.')
#         else: row.append("#")
#         if (c == '>'):
#             blizzard_dirs.append(0)
#             blizzard_poses.append((i, j))
#         elif (c == '^'):
#             blizzard_dirs.append(1)
#             blizzard_poses.append((i, j))
#         elif (c == '<'):
#             blizzard_dirs.append(2)
#             blizzard_poses.append((i, j))
#         elif (c == 'v'):
#             blizzard_dirs.append(3)
#             blizzard_poses.append((i, j))
#         j += 1
#     grid.append(row)
#     i += 1

# Blizzards = []
# n, m = len(grid), len(grid[0])
# N = n * m // math.gcd(n, m)
# for count in range(N):
#     for i in range(len(blizzard_poses)):
#         if (blizzard_dirs[i] == 0): kx, ky = 1, 0
#         elif (blizzard_dirs[i] == 1): kx, ky = 0, -1
#         elif (blizzard_dirs[i] == 2): kx, ky = -1, 0
#         else: kx, ky = 0, 1
        
#         if (grid[blizzard_poses[i][0] + ky][blizzard_poses[i][1] + kx] == '#'):
#             if (blizzard_dirs[i] == 0): blizzard_poses[i] = (blizzard_poses[i][0], 1)
#             elif (blizzard_dirs[i] == 1): blizzard_poses[i] = (n - 2, blizzard_poses[i][1])
#             elif (blizzard_dirs[i] == 2): blizzard_poses[i] = (blizzard_poses[i][0], m - 2)
#             else: blizzard_poses[i] = (1, blizzard_poses[i][1])
#         else:
#             blizzard_poses[i] = (blizzard_poses[i][0] + ky, blizzard_poses[i][1] + kx)
#     Blizzards.append(set(blizzard_poses))

# print(explore((0, 1), (len(grid) - 1, grid[-1].index('.')), grid, Blizzards))
# print(time.time() - start_time)

##########
# PART 2 #
##########

def explore(u, target, t, grid, Blizzards):
    n, m = len(grid), len(grid[0])
    T = n * m // math.gcd(n, m)
    queue = []
    heapq.heappush(queue, (t, u))
    visited = set()
    while len(queue) != 0:
        t, u = heapq.heappop(queue)
        if (u == target): return t
        t2 = t % T
        if ((u, t2) not in visited):
            visited.add((u, t2))
            blizzard_poses = Blizzards[t2]
        
            # Choose next
            for k in [(1, 0), (0, -1), (-1, 0), (0, 1), (0, 0)]:
                v = (u[0] + k[0], u[1] + k[1])
                if (0 <= v[0] < n and 0 <= v[1] < m and grid[v[0]][v[1]] == '.'):
                    if (v not in blizzard_poses): heapq.heappush(queue, (t + 1, v))

    return None

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = []
blizzard_poses, blizzard_dirs = [], []
i = 0
for line in lines:
    j = 0
    row = []
    for c in line:
        if (c != '#'): row.append('.')
        else: row.append("#")
        if (c == '>'):
            blizzard_dirs.append(0)
            blizzard_poses.append((i, j))
        elif (c == '^'):
            blizzard_dirs.append(1)
            blizzard_poses.append((i, j))
        elif (c == '<'):
            blizzard_dirs.append(2)
            blizzard_poses.append((i, j))
        elif (c == 'v'):
            blizzard_dirs.append(3)
            blizzard_poses.append((i, j))
        j += 1
    grid.append(row)
    i += 1

Blizzards = []
n, m = len(grid), len(grid[0])
N = n * m // math.gcd(n, m)
for count in range(N):
    for i in range(len(blizzard_poses)):
        if (blizzard_dirs[i] == 0): kx, ky = 1, 0
        elif (blizzard_dirs[i] == 1): kx, ky = 0, -1
        elif (blizzard_dirs[i] == 2): kx, ky = -1, 0
        else: kx, ky = 0, 1
        
        if (grid[blizzard_poses[i][0] + ky][blizzard_poses[i][1] + kx] == '#'):
            if (blizzard_dirs[i] == 0): blizzard_poses[i] = (blizzard_poses[i][0], 1)
            elif (blizzard_dirs[i] == 1): blizzard_poses[i] = (n - 2, blizzard_poses[i][1])
            elif (blizzard_dirs[i] == 2): blizzard_poses[i] = (blizzard_poses[i][0], m - 2)
            else: blizzard_poses[i] = (1, blizzard_poses[i][1])
        else:
            blizzard_poses[i] = (blizzard_poses[i][0] + ky, blizzard_poses[i][1] + kx)
    Blizzards.append(set(blizzard_poses))

start, end = (0, 1), (len(grid) - 1, grid[-1].index('.'))
t1 = explore(start, end, 0, grid, Blizzards)
t2 = explore(end, start, t1, grid, Blizzards)
t3 = explore(start, end, t2, grid, Blizzards)
print(t3)
print(time.time() - start_time)