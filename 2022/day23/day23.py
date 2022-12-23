import time

##########
# PART 1 #
##########

# padding = 25

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# grid = []
# elf_poses = []
# i = 0
# for line in lines:
#     row = []
#     j = 0
#     for _ in range(padding): row.append('.')
#     for c in line:
#         if (c == "#"): elf_poses.append((padding + i, padding + j))
#         row.append(c)
#         j += 1
#     for _ in range(padding): row.append('.')
#     grid.append(row)
#     i += 1
# for _ in range(padding):
#     grid.insert(0, ['.' for _ in range(2 * padding + len(lines[0]))])
#     grid.append(['.' for _ in range(2 * padding + len(lines[0]))])

# # print(0)
# # for row in grid:
# #     print("".join(row))
# # print()

# n, m = len(grid), len(grid[0])
# adjacencies = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# elf_orders = [[0, 1, 2, 3] for _ in range(len(elf_poses))]

# count = 1
# while True:
#     if (count == 11): break
    
#     ##############
#     # FIRST HALF #
#     ##############
    
#     proposals = {0: [], 1: [], 2: [], 3: []}
#     for index in range(len(elf_poses)):
#         i, j = elf_poses[index]
#         temp = []
#         total_dirs_compared = 0
#         for proposal in elf_orders[index]:
#             k = adjacencies[proposal]
#             compares = 0
#             avail = 0
#             if (0 <= i + k[0] < n and 0 <= j + k[1] < m):
#                 if (grid[i + k[0]][j + k[1]] == "."): avail += 1
#                 compares += 1
                    
#             if (k[0] != 0):
#                 if (0 <= i + k[0] < n and 0 <= j + k[1] + 1 < m):
#                     if (grid[i + k[0]][j + k[1] + 1] == "."): avail += 1
#                     compares += 1
#                 if (0 <= i + k[0] < n and 0 <= j + k[1] - 1 < m):
#                     if (grid[i + k[0]][j + k[1] - 1] == "."): avail += 1
#                     compares += 1
#             if (k[1] != 0):
#                 if (0 <= i + k[0] + 1 < n and 0 <= j + k[1] < m):
#                     if (grid[i + k[0] + 1][j + k[1]] == "."): avail += 1
#                     compares += 1
#                 if (0 <= i + k[0] - 1 < n and 0 <= j + k[1] < m):
#                     if (grid[i + k[0] - 1][j + k[1]] == "."): avail += 1
#                     compares += 1
            
#             if (compares == 0): continue
#             if (avail == compares):
#                 temp.append(proposal)
            
#             total_dirs_compared += 1

#         #print((i, j), temp)
#         elf_orders[index].append(elf_orders[index].pop(0))
#         if (len(temp) == total_dirs_compared or len(temp) == 0): continue

#         proposals[temp[0]].append((i, j))


#     #print(proposals)
    
#     ###############
#     # SECOND HALF #
#     ###############
    
#     srcs = []
#     dests = []
#     for proposal in proposals:
#         for src in proposals[proposal]:
#             srcs.append(src)
#             dests.append((src[0] + adjacencies[proposal][0], src[1] + adjacencies[proposal][1]))
    
#     #print(srcs)
#     #print(dests)
#     moves = 0
#     for i in range(len(srcs)):
#         if (dests.count(dests[i]) == 1):
#             grid[srcs[i][0]][srcs[i][1]] = '.'
#             grid[dests[i][0]][dests[i][1]] = '#'
#             index = 0
#             for elf in elf_poses:
#                 if (elf == srcs[i]): break
#                 index += 1
#             elf_poses[index] = dests[i]
#             moves += 1

#     if (moves == 0): break

#     # for row in grid:
#     #     print("".join(row))
#     # print()

#     count += 1

# ##################
# # FIND RECTANGLE #
# ##################

# left = 0
# while True:
#     boundary = []
#     for i in range(n): boundary.append(grid[i][left])
#     if ('#' in boundary): break
#     left += 1
# right = m - 1
# while True:
#     boundary = []
#     for i in range(n): boundary.append(grid[i][right])
#     if ('#' in boundary): break
#     right -= 1
# top = 0
# while True:
#     boundary = grid[top]
#     if ('#' in boundary): break
#     top += 1
# bottom = n - 1
# while True:
#     boundary = grid[bottom]
#     if ('#' in boundary): break
#     bottom -= 1
    
# open_count = 0
# for i in range(top, bottom + 1):
#     for j in range(left, right + 1):
#         if (grid[i][j] == '.'): open_count += 1
# print(open_count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

padding = 100

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = []
elf_poses = []
i = 0
for line in lines:
    row = []
    j = 0
    for _ in range(padding): row.append('.')
    for c in line:
        if (c == "#"): elf_poses.append((padding + i, padding + j))
        row.append(c)
        j += 1
    for _ in range(padding): row.append('.')
    grid.append(row)
    i += 1
for _ in range(padding):
    grid.insert(0, ['.' for _ in range(2 * padding + len(lines[0]))])
    grid.append(['.' for _ in range(2 * padding + len(lines[0]))])

n, m = len(grid), len(grid[0])
adjacencies = [(-1, 0), (1, 0), (0, -1), (0, 1)]
elf_orders = [[0, 1, 2, 3] for _ in range(len(elf_poses))]

count = 1
while True:

    ##############
    # FIRST HALF #
    ##############
    
    proposals = {0: [], 1: [], 2: [], 3: []}
    for index in range(len(elf_poses)):
        i, j = elf_poses[index]
        temp = []
        total_dirs_compared = 0
        for proposal in elf_orders[index]:
            k = adjacencies[proposal]
            compares = 0
            avail = 0
            if (0 <= i + k[0] < n and 0 <= j + k[1] < m):
                if (grid[i + k[0]][j + k[1]] == "."): avail += 1
                compares += 1
                    
            if (k[0] != 0):
                if (0 <= i + k[0] < n and 0 <= j + k[1] + 1 < m):
                    if (grid[i + k[0]][j + k[1] + 1] == "."): avail += 1
                    compares += 1
                if (0 <= i + k[0] < n and 0 <= j + k[1] - 1 < m):
                    if (grid[i + k[0]][j + k[1] - 1] == "."): avail += 1
                    compares += 1
            if (k[1] != 0):
                if (0 <= i + k[0] + 1 < n and 0 <= j + k[1] < m):
                    if (grid[i + k[0] + 1][j + k[1]] == "."): avail += 1
                    compares += 1
                if (0 <= i + k[0] - 1 < n and 0 <= j + k[1] < m):
                    if (grid[i + k[0] - 1][j + k[1]] == "."): avail += 1
                    compares += 1
            
            if (compares == 0): continue
            if (avail == compares):
                temp.append(proposal)
            
            total_dirs_compared += 1

        elf_orders[index].append(elf_orders[index].pop(0))
        if (len(temp) == total_dirs_compared or len(temp) == 0): continue

        proposals[temp[0]].append((i, j))

    ###############
    # SECOND HALF #
    ###############
    
    srcs = []
    dests = []
    for proposal in proposals:
        for src in proposals[proposal]:
            srcs.append(src)
            dests.append((src[0] + adjacencies[proposal][0], src[1] + adjacencies[proposal][1]))
 
    moves = 0
    dest_counts = {x: dests.count(x) for x in set(dests)}
    for i in range(len(srcs)):
        if (dests[i] in dest_counts and dest_counts[dests[i]] == 1):
            grid[srcs[i][0]][srcs[i][1]] = '.'
            grid[dests[i][0]][dests[i][1]] = '#'
            elf_poses[elf_poses.index(srcs[i])] = dests[i]
            moves += 1

    if (moves == 0): break
    
    count += 1
print(count)
print(time.time() - start_time)