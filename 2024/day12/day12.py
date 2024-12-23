import time

##########
# PART 1 #
##########

# def find(i):
#     if (regions[i] == i): return i
#     else: return find(regions[i])
# def union(i, j):
#     x = find(i)
#     regions[i] = x
#     regions[find(j)] = x

# def DFS(pos):
#     index = M * pos[0] + pos[1]
#     if (index in seen): return
#     seen.add(index)
#     regions[index] = index
#     for delta in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#         pos2 = (pos[0] + delta[0], pos[1] + delta[1])
#         if (0 <= pos2[0] < N and 0 <= pos2[1] < M and grid[pos[0]][pos[1]] == grid[pos2[0]][pos2[1]]):
#             index2 = M * pos2[0] + pos2[1]
#             union(index, index2)
#             DFS(pos2)

# start_time = time.time()
# f = open("input.txt", 'r')
# grid = [list(l) for l in f.read().split("\n")]
# N, M = len(grid), len(grid[0])
# regions = [i for i in range(N * M)]
# for i in range(N):
#     for j in range(M):
#         seen = set()
#         DFS((i, j))
# # for i in range(len(regions)):
# #     print(i, i // M, i % M, find(regions[i]))
# areas = {}
# for x in regions:
#     y = find(x)
#     if (y not in areas): areas[y] = 1
#     else: areas[y] += 1
# perimeters = {}
# for i in range(N):
#     for j in range(M):
#         index = M * i + j
#         pos = (i, j)
#         # Check adjacent nodes and subtract 1 for each one in the same group
#         perim_contrib = 4
#         for delta in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#             pos2 = (pos[0] + delta[0], pos[1] + delta[1])
#             if (0 <= pos2[0] < N and 0 <= pos2[1] < M and grid[pos[0]][pos[1]] == grid[pos2[0]][pos2[1]]):
#                 perim_contrib -= 1
#         x = find(index)
#         if (x not in perimeters): perimeters[x] = perim_contrib
#         else: perimeters[x] += perim_contrib
# price = 0
# for x in areas:
#     #print(x // M, x % M, grid[x // M][x%M], areas[x], perimeters[x])
#     price += areas[x] * perimeters[x]
# print(price)
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

def find(i):
    if (regions[i] == i): return i
    else: return find(regions[i])
def union(i, j):
    x = find(i)
    regions[i] = x
    regions[find(j)] = x

def DFS(pos):
    index = M * pos[0] + pos[1]
    if (index in seen): return
    seen.add(index)
    regions[index] = index
    for delta in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        pos2 = (pos[0] + delta[0], pos[1] + delta[1])
        if (0 <= pos2[0] < N and 0 <= pos2[1] < M and grid[pos[0]][pos[1]] == grid[pos2[0]][pos2[1]]):
            index2 = M * pos2[0] + pos2[1]
            union(index, index2)
            DFS(pos2)

start_time = time.time()
f = open("input.txt", 'r')
grid = [list(l) for l in f.read().split("\n")]
N, M = len(grid), len(grid[0])
regions = [i for i in range(N * M)]
for i in range(N):
    for j in range(M):
        seen = set()
        DFS((i, j))
# for i in range(len(regions)):
#     print(i, i // M, i % M, find(regions[i]))
areas = {}
for x in regions:
    y = find(x)
    if (y not in areas): areas[y] = 1
    else: areas[y] += 1
# To calculate sides, follow the "right wall" for a single element in each region until we return to the start
sides = {}
for x in areas:
    side_count = 0
    start_pos = (x // M, x % M)
    # Move as far down as possible
    while True:
        if (start_pos[0] + 1 < N and grid[start_pos[0]][start_pos[1]] == grid[start_pos[0] + 1][start_pos[1]]):
            start_pos = (start_pos[0] + 1, start_pos[1])
        else: break
    # Follow the right wall at all times until we reach the position we started at.
price = 0
for x in areas:
    print(x // M, x % M, grid[x // M][x%M], areas[x], sides[x])
    price += areas[x] * sides[x]
print(price)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")