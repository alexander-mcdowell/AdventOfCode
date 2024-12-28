import time
import sys

# ##########
# # PART 1 #
# ##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# grid = []
# start_pos = None
# end_pos = None
# i = 0
# for l in data:
#     row = []
#     j = 0
#     for c in l:
#         if (c == 'S'): start_pos = (i, j)
#         elif (c == 'E'): end_pos = (i, j)
#         row.append(c)
#         j += 1
#     grid.append(row)
#     i += 1

# # Dijkstra's
# N, M = len(grid), len(grid[0])
# dists = [[-1 for _ in range(M)] for _ in range(N)]
# prevs = [[None for _ in range(M)] for _ in range(N)]
# dists[start_pos[0]][start_pos[1]] = 0
# stack = [(start_pos, 0)]
# while len(stack) != 0:
#     u_val, best_i = -1, 0
#     for i in range(len(stack)):
#         v, _ = stack[i]
#         if (u_val==-1 or dists[v[0]][v[1]] < u_val):
#             best_i = i
#             u_val = dists[v[0]][v[1]]
#     u, dir = stack.pop(best_i)
    
#     for dir2 in range(4):
#         delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir2]
#         v = (u[0] + delta[0], u[1] + delta[1])
#         if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#')): continue
#         v_val = dists[v[0]][v[1]]
#         x = u_val + ((dir2 - dir)%2) * 1000 + 1
#         if (v_val == -1 or x < v_val):
#             dists[v[0]][v[1]] = x
#             prevs[v[0]][v[1]] = u
#             stack.append((v, dir2))

# print(dists[end_pos[0]][end_pos[1]])
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
start_pos = None
end_pos = None
i = 0
for l in data:
    row = []
    j = 0
    for c in l:
        if (c == 'S'): start_pos = (i, j)
        elif (c == 'E'): end_pos = (i, j)
        row.append(c)
        j += 1
    grid.append(row)
    i += 1

# Dijkstra's
N, M = len(grid), len(grid[0])
dists = [[[-1 for _ in range(4)] for _ in range(M)] for _ in range(N)]
prevs = [[[[] for _ in range(4)] for _ in range(M)] for _ in range(N)]
dists[start_pos[0]][start_pos[1]][0] = 0

stack = [(start_pos, 0)]
while len(stack) != 0:
    # Priority queue
    u_val, best_i = -1, 0
    for i in range(len(stack)):
        v, v_dir = stack[i]
        if (u_val==-1 or dists[v[0]][v[1]][v_dir] < u_val):
            best_i = i
            u_val = dists[v[0]][v[1]][v_dir]
    u, dir = stack.pop(best_i)
    
    # Move in current direction
    delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir]
    v = (u[0] + delta[0], u[1] + delta[1])
    if (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#'):
        v_val = dists[v[0]][v[1]][dir]
        x = u_val + 1
        if (v_val == -1 or x < v_val):
            dists[v[0]][v[1]][dir] = x
            prevs[v[0]][v[1]][dir] = [(u, dir)]
            stack.append((v, dir))
        elif (x == v_val): prevs[v[0]][v[1]][dir].append((u, dir))
    
    # Turn from current direction
    for turn in [1, -1]:
        dir2 = (dir + turn) % 4
        v_val = dists[u[0]][u[1]][dir2]
        x = u_val + 1000
        if (v_val == -1 or x < v_val):
            dists[u[0]][u[1]][dir2] = x
            prevs[u[0]][u[1]][dir2] = [(u, dir)]
            stack.append((u, dir2))
        elif (x == v_val): prevs[u[0]][u[1]][dir2].append((u, dir))

min_path, best_dir = -1, None
for k in range(4):
    x = dists[end_pos[0]][end_pos[1]][k]
    if (min_path == -1 or x < min_path):
        min_path = x
        best_dir = k
print("Min path length:", min_path)

seen = set()
queue = [(end_pos, best_dir)]
while len(queue) != 0:
    u, u_dir = queue.pop(0)
    grid[u[0]][u[1]] = 'O'
    seen.add(u)
    for x in prevs[u[0]][u[1]][u_dir]: queue.append(x)
# for row in grid:
#     print("".join(row))
print("Best paths tiles:", len(seen))
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")