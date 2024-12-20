import time

# ##########
# # PART 1 #
# ##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")

# start_pos = None
# end_pos = None
# grid = []
# i = 0
# total_length = 0
# empty_poses = set()
# for l in data:
#     row = []
#     j = 0
#     for c in l:
#         if (c in ['S', 'E', '.']): empty_poses.add((i, j))
#         if (c in ['E', '.']): total_length += 1
#         if (c == 'S'):
#             row.append('.')
#             start_pos = (i, j)
#         elif (c == 'E'):
#             row.append('.')
#             end_pos = (i, j)
#         else: row.append(c)
#         j += 1
#     grid.append(row)
#     i += 1
# N, M = len(grid), len(grid[0])

# last_dir = None
# u = start_pos
# pos_to_length = {}
# pos_to_length[start_pos] = 0
# length = 0
# while u != end_pos:
#     for dir in range(4):
#         if (last_dir != None and dir == (last_dir + 2)%4): continue
#         delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir]
#         v = (u[0] + delta[0], u[1] + delta[1])

#         if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#')): continue
        
#         length += 1
#         pos_to_length[v] = length
#         u = v
#         last_dir = dir
#         break
# total_length = pos_to_length[end_pos]

# paths = {}
# for u in pos_to_length:
#     for dir in range(4):
#         delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir]
#         v = (u[0] + delta[0], u[1] + delta[1])
#         v2 = (u[0] + 2 * delta[0], u[1] + 2 * delta[1])
        
#         # Attempt a cheat
#         if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] == '#')): continue
#         if (not (0 <= v2[0] < N and 0 <= v2[1] < M and grid[v2[0]][v2[1]] == '.')): continue
#         new_length = pos_to_length[u] + (total_length - pos_to_length[v2]) + 2
#         if (new_length < total_length):
#             if (new_length not in paths): paths[new_length] = 1
#             else: paths[new_length] += 1
# count = 0
# for x in paths:
#     if (total_length - x >= 100): count += paths[x]
# print(count)
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")

start_pos = None
end_pos = None
grid = []
i = 0
total_length = 0
empty_poses = set()
for l in data:
    row = []
    j = 0
    for c in l:
        if (c in ['S', 'E', '.']): empty_poses.add((i, j))
        if (c in ['E', '.']): total_length += 1
        if (c == 'S'):
            row.append('.')
            start_pos = (i, j)
        elif (c == 'E'):
            row.append('.')
            end_pos = (i, j)
        else: row.append(c)
        j += 1
    grid.append(row)
    i += 1
N, M = len(grid), len(grid[0])

last_dir = None
u = start_pos
pos_to_length = {}
pos_to_length[start_pos] = 0
length = 0
while u != end_pos:
    for dir in range(4):
        if (last_dir != None and dir == (last_dir + 2)%4): continue
        delta = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir]
        v = (u[0] + delta[0], u[1] + delta[1])

        if (not (0 <= v[0] < N and 0 <= v[1] < M and grid[v[0]][v[1]] != '#')): continue
        
        length += 1
        pos_to_length[v] = length
        u = v
        last_dir = dir
        break
total_length = pos_to_length[end_pos]

paths = {}
poses = list(pos_to_length)
for i in range(len(poses)):
    u = poses[i]
    for j in range(i + 1, len(poses)):
        v = poses[j]
        delta = abs(u[0] - v[0]) + abs(u[1] - v[1])
        if (delta > 20): continue
        new_length = pos_to_length[u] + (total_length - pos_to_length[v]) + delta
        if (new_length < total_length):
            if (new_length not in paths): paths[new_length] = 1
            else: paths[new_length] += 1
count = 0
K = 100
for x in paths:
    if (total_length - x >= K): count += paths[x]
print(count)

print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")