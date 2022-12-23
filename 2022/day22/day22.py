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
        instructions.append(int(x))
        instructions.append("L")
    if (inst[-1] != "L"): instructions.pop(-1)
    instructions.append("R")
if (lines[i][-1] != "R"): instructions.pop(-1)

N = 4
faces = []
i = 0
while N * i != len(grid):
    faces2 = []
    temp = grid[N * i : N * (i + 1)]
    k = len(temp[0])//N
    for _ in range(k): faces2.append([])
    for line in temp:
        for j in range(k):
            faces2[j].append(line[N * j : N * (j + 1)])
    faces += faces2
    i += 1

i = 0
while i < len(faces):
    if (faces[i][0][0] == " "): faces.pop(i)
    else: i += 1
    
# Hardcode the faces
top = 1
bottom = 3
front = 4
back = 0
left = 2
right = 5

face_index = 0
i, j = 0, 0
direction = 0
for inst in instructions:
    if (inst == "R"): direction = (direction + 1) % 4
    elif (inst == "L"): direction = (direction - 1) % 4
    else:
        if (direction == 0): kx, ky = 1, 0
        elif (direction == 1): kx, ky = 0, 1
        elif (direction == 2): kx, ky = -1, 0
        else: kx, ky = 0, -1
        
        while True:
            flag = False
            for k in range(inst):
                if (not ((0 <= i + ky < N) and (0 <= j + kx < N))):
                    flag = True
                    inst -= k + 1
                    break
                if (faces[face_index][i + ky][j + kx] == "#"):
                    break
                elif (faces[face_index][i + ky][j + kx] == "."):
                    i += ky
                    j += kx
                else:
                    flag = True
                    inst -= k + 1
                    break
            
            if (flag):
                # Top
                if (face_index == top):
                    # Left from top =
                    # Right from top =
                    # Up from top =
                    # Down from top =
                    pass
                # Bottom
                elif (face_index == bottom):
                    # Left from bottom =
                    # Right from bottom =
                    # Up from bottom =
                    # Down from bottom =
                    pass
                # Left
                elif (face_index == left):
                    # Left from left =
                    # Right from left =
                    # Up from left =
                    # Down from left =
                    pass
                # Right
                elif (face_index == right):
                    # Left from right =
                    # Right from right =
                    # Up from right =
                    # Down from right =
                    pass
                # Front
                elif (face_index == front):
                    # Left from front =
                    # Right from front =
                    # Up from front =
                    # Down from front =
                    pass
                # Back
                else:
                    # Left from back =
                    # Right from back =
                    # Up from back =
                    # Down from back =
                    pass
                
            else: break

print(time.time() - start_time)