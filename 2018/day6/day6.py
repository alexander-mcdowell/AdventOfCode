##########
# PART 1 #
##########

# import time

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# coords = []
# max_x, max_y = -1, -1
# for line in lines:
#     x, y = [int(k) for k in line.split(', ')]
#     coords.append((x, y))
#     if (x > max_x): max_x = x
#     if (y > max_y): max_y = y

# avoid = set()
# grid = []
# for y in range(max_y + 1):
#     row = []
#     for x in range(max_x + 1):
#         best, best_i, unique = -1, None, True
#         for i in range(len(coords)):
#             dist = abs(x - coords[i][0]) + abs(y - coords[i][1])
#             if (dist == 0):
#                 best_i = i
#                 break
#             if (best == -1 or dist < best):
#                 best = dist
#                 best_i = i
#                 unique = True
#             elif (dist == best):
#                 unique = False
#         if (unique):
#             row.append(best_i)
#             if (x == 0 or x == max_x): avoid.add(row[-1])
#         else: row.append(-1)
#     grid.append(row)
#     if (y == 0 or y == max_y): avoid = avoid.union(set(row))
# if (-1 in avoid): avoid.remove(-1)
# area_dict = {}
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         coord = grid[y][x]
#         if (coord not in avoid and coord != -1):
#             if (coord not in area_dict): area_dict[coord] = 0
#             area_dict[coord] += 1
# print(max([area_dict[k] for k in area_dict]))
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

start_time = time.time()
lines = open("input.txt").read().split("\n")
coords = []
max_x, max_y = -1, -1
for line in lines:
    x, y = [int(k) for k in line.split(', ')]
    coords.append((x, y))
    if (x > max_x): max_x = x
    if (y > max_y): max_y = y

N = 10000
area = 0
for y in range(max_y + 1):
    row = []
    for x in range(max_x + 1):
        best, best_i, unique = -1, None, True
        sum_dist = 0
        for i in range(len(coords)):
            sum_dist += abs(x - coords[i][0]) + abs(y - coords[i][1])
        if (sum_dist < N): area += 1
print(area)
print(time.time() - start_time)