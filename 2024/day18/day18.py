import time

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
N, M = 71, 71
start_pos = (0, 0)
end_pos = (N - 1, M - 1)
grid = [['.' for _ in range(M)] for _ in range(N)]

count = 1024
for l in data[:count]:
    x, y = [int(z) for z in l.split(",")]
    grid[y][x] = '#'
# for row in grid: print("".join(row))

# Dijkstra's
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
        x = u_val + 1
        if (v_val == -1 or x < v_val):
            dists[v[0]][v[1]] = x
            prevs[v[0]][v[1]] = u
            stack.append((v, dir2))

print(dists[end_pos[0]][end_pos[1]])
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
N, M = 71, 71
start_pos = (0, 0)
end_pos = (N - 1, M - 1)
grid = [['.' for _ in range(M)] for _ in range(N)]

def dijkstra():
    dists = [[-1 for _ in range(M)] for _ in range(N)]
    prevs = [[None for _ in range(M)] for _ in range(N)]
    dists[start_pos[0]][start_pos[1]] = 0
    stack = [start_pos]
    while len(stack) != 0:
        u_val, best_i = -1, 0
        for i in range(len(stack)):
            v = stack[i]
            if (u_val==-1 or dists[v[0]][v[1]] < u_val):
                best_i = i
                u_val = dists[v[0]][v[1]]
        u = stack.pop(best_i)
        
        for k in range(4):
            delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][k]
            v = (u[0] + delta[0], u[1] + delta[1])
            if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#')): continue
            v_val = dists[v[0]][v[1]]
            x = u_val + 1
            if (v_val == -1 or x < v_val):
                dists[v[0]][v[1]] = x
                prevs[v[0]][v[1]] = u
                stack.append(v)
    return dists, prevs

# Thanks to Ashe for this suggestion
for l in data:
    block_j, block_i = [int(z) for z in l.split(",")]
    grid[block_i][block_j] = '#'
for l in data[::-1]:
    block_j, block_i = [int(z) for z in l.split(",")]
    grid[block_i][block_j] = '.'

    dists, prevs = dijkstra()

    if (dists[end_pos[0]][end_pos[1]] != -1):
        print(block_j, block_i)
        break
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")