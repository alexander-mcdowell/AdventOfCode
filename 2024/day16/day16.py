import time
import sys
sys.setrecursionlimit(10000)

# ##########
# # PART 1 #
# ##########

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
dists = [[-1 for _ in range(M)] for _ in range(N)]
prevs = [[None for _ in range(M)] for _ in range(N)]
dists[start_pos[0]][start_pos[1]] = 0
stack = [(start_pos, 0)]
while len(stack) != 0:
    u_val, best_i = -1, 0
    for i in range(len(stack)):
        v, _ = stack[i]
        if (u_val==-1 or dists[v[0]][v[1]] < u_val):
            best_i = i
            u_val = dists[v[0]][v[1]]
    u, dir = stack.pop(best_i)
    
    for dir2 in range(4):
        delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir2]
        v = (u[0] + delta[0], u[1] + delta[1])
        if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#')): continue
        v_val = dists[v[0]][v[1]]
        x = u_val + ((dir2 - dir)%2) * 1000 + 1
        if (v_val == -1 or x < v_val):
            dists[v[0]][v[1]] = x
            prevs[v[0]][v[1]] = u
            stack.append((v, dir2))

print(dists[end_pos[0]][end_pos[1]])
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

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
    
    # Update moves
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
    
    # Update turns
    for turns in [1, -1]:
        dir2 = (dir + turns) % 4
        v_val = dists[u[0]][u[1]][dir2]
        x = u_val + 1000
        if (v_val == -1 or x < v_val):
            dists[u[0]][u[1]][dir2] = x
            prevs[u[0]][u[1]][dir2] = [(u, dir)]
            stack.append((u, dir2))
        elif (x == v_val): prevs[u[0]][u[1]][dir2].append((u, dir))

arr = [y for y in dists[end_pos[0]][end_pos[1]] if y != -1]
min_path = min(arr) if len(arr) != 0 else -1
print("Min path length:", min_path)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")