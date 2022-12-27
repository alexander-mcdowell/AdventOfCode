import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# grid = []
# i = 0
# found = False
# start = None
# for line in lines:
#     if (len(line) == 0):
#         i += 1
#         break
#     row = []
#     for j in range(len(line)):
#         if (line[j] == "."):
#             if (not found):
#                 found = True
#                 start = (i, j)
#         row.append(line[j])
#     grid.append(row)
#     i += 1

# temp = lines[i].split("R")
# instructions = []
# for inst in temp:
#     for x in inst.split("L"):
#         instructions.append(int(x))
#         instructions.append("L")
#     if (inst[-1] != "L"): instructions.pop(-1)
#     instructions.append("R")
# if (lines[i][-1] != "R"): instructions.pop(-1)

# pos = list(start)
# direction = 0
# for inst in instructions:
#     if (inst == "R"): direction = (direction + 1) % 4
#     elif (inst == "L"): direction = (direction - 1) % 4
#     else:
#         if (direction == 0): kx, ky = 1, 0
#         elif (direction == 1): kx, ky = 0, 1
#         elif (direction == 2): kx, ky = -1, 0
#         else: kx, ky = 0, -1
        
#         while True:
#             flag = False
#             for k in range(inst):
#                 if (not ((0 <= pos[0] + ky < len(grid)) and (0 <= pos[1] + kx < len(grid[pos[0] + ky])))):
#                     flag = True
#                     inst -= k + 1
#                     break
#                 if (grid[pos[0] + ky][pos[1] + kx] == "#"):
#                     break
#                 elif (grid[pos[0] + ky][pos[1] + kx] == "."):
#                     pos[0] += ky
#                     pos[1] += kx
#                 else:
#                     flag = True
#                     inst -= k + 1
#                     break
                
#             # Find the start
#             if (flag):
#                 pos2 = [x for x in pos]
#                 while ((0 <= pos2[0] - ky < len(grid)) and (0 <= pos2[1] - kx < len(grid[pos2[0] - ky])) and grid[pos2[0] - ky][pos2[1] - kx] != " "):
#                     pos2[0] -= ky
#                     pos2[1] -= kx
                
#                 if (grid[pos2[0]][pos2[1]] == "#"):
#                     break
#                 else: pos = [x for x in pos2]
#             else: break

# print(pos, direction)
# print(1000 * (1 + pos[0]) + 4 * (1 + pos[1]) + direction)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = []
i = 0
for line in lines:
    if (len(line) == 0):
        i += 1
        break
    row = []
    for j in range(len(line)): row.append(line[j])
    grid.append(row)
    i += 1

temp = lines[i].split("R")
instructions = []
for inst in temp:
    for x in inst.split("L"):
        if (x != ''):
            instructions.append(int(x))
            instructions.append("L")
    if (inst != ''):
        if (inst[-1] != "L"): instructions.pop(-1)
        instructions.append("R")
if (lines[i][-1] != "R"): instructions.pop(-1)

# Hardcode the net
"""
    01
    2
34
5

0 = top
1 = right
2 = back
3 = left
4 = bottom
5 = front

    #a# #e#
    d#b b#f
    #c# #g#

    #c#
    h#g
    #i#

#h# #i#
d#j j#f
#k# #l#

#k#
a#l
#e#

"""

top = 0
bottom = 4
front = 5
back = 2
left = 3
right = 1

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

N = 50
face_index = top
i, j = 0, N
direction = 0
for inst in instructions:
    if (inst == "R"): direction = (direction + 1) % 4
    elif (inst == "L"): direction = (direction - 1) % 4
    else:        
        while True:
            if (direction == RIGHT): kx, ky = 1, 0
            elif (direction == DOWN): kx, ky = 0, 1
            elif (direction == LEFT): kx, ky = -1, 0
            else: kx, ky = 0, -1
            
            flag = False
            for k in range(inst):
                if (not ((0 <= i + ky < len(grid) and 0 <= j + kx < len(grid[i + ky])))):
                    flag = True
                    inst -= k + 1
                    break
                if (grid[i + ky][j + kx] == "#"): break
                elif (grid[i + ky][j + kx] == "."):
                    i += ky
                    j += kx
                else:
                    flag = True
                    inst -= k + 1
                    break
            
            if (flag):
                if (i < N and N <= j < 2 * N): face_index = 0
                elif (i < N and 2 * N <= j < 3 * N): face_index = 1
                elif (N <= i < 2 * N and N <= j < 2 * N): face_index = 2
                elif (2 * N <= i < 3 * N and j < N): face_index = 3
                elif (2 * N <= i < 3 * N and N <= j < 2 * N): face_index = 4
                else: face_index = 5
                
                row, col = i % N, j % N
                # Top
                if (face_index == top):
                    # Left from top = Left to right on left
                    if (direction == LEFT):
                        direction_new = RIGHT
                        i_new, j_new = 2 * N + (N - 1 - row), 0
                    # Up from top = Left to right on front
                    else:
                        direction_new = RIGHT
                        i_new, j_new = 3 * N + col, 0
                # Bottom
                elif (face_index == bottom):
                    # Right from bottom = Right to left on right
                    if (direction == RIGHT):
                        direction_new = LEFT
                        i_new, j_new = N - 1 - row, 3 * N - 1
                    # Down from bottom = Right to left on front
                    else:
                        direction_new = LEFT
                        i_new, j_new = 3 * N + col, N - 1
                # Left
                elif (face_index == left):
                    # Up from left = Left to right on back
                    if (direction == UP):
                        direction_new = RIGHT
                        i_new, j_new = N + col, N
                    # Left from left = Left to right on top
                    else:
                        direction_new = RIGHT
                        i_new, j_new = N - 1 - row, N
                # Right
                elif (face_index == right):
                    # Right from right = Right to left on bottom
                    if (direction == RIGHT):
                        direction_new = LEFT
                        i_new, j_new = 2 * N + (N - 1 - row), 2 * N - 1
                    # Up from right = Bottom to top on front
                    elif (direction == UP):
                        direction_new = UP
                        i_new, j_new = 4 * N - 1, col
                    # Down from right = Right to left on back
                    else:
                        direction_new = LEFT
                        i_new, j_new = N + col, 2 * N - 1
                # Front
                elif (face_index == front):
                    # Left from front = Top to bottom on top
                    if (direction == LEFT):
                        direction_new = DOWN
                        i_new, j_new = 0, N + row
                    # Down from front = Top to bottom on right
                    elif (direction == DOWN):
                        direction_new = DOWN
                        i_new, j_new = 0, 2 * N + col
                    # Right from front = Bottom to top on bottom
                    else:
                        direction_new = UP
                        i_new, j_new = 3 * N - 1, N + row
                # Back
                else:
                    # Left from back = Top to bottom on left
                    if (direction == LEFT):
                        direction_new = DOWN
                        i_new, j_new = 2 * N, row
                    # Right from back = Bottom to top on right
                    else:
                        direction_new = UP
                        i_new, j_new = N - 1, 2 * N + row
                
                if (grid[i_new][j_new] == '#'): break
                else: i, j, direction = i_new, j_new, direction_new
            else: break

i, j = i + 1, j + 1
print(i, j, direction)
print(1000 * i + 4 * j + direction)
print(time.time() - start_time)