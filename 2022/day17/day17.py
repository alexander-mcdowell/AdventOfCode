import time

##########
# PART 1 #
##########

# N = 2022

# start_time = time.time()
# instructions = list(open("input.txt", "r+").read().split("\n")[0])
# inst_counter = 0
# height = 0
# grid = []
# for i in range(N):
#     # Expand the grid
#     x, y = 2, height + 3
#     if (i % 5 == 1 or i % 5 == 2):
#         while y + 2 >= len(grid): grid.append([False for _ in range(7)])
#     elif (i % 5 == 3 and y + 3 >= len(grid)):
#         while y + 3 >= len(grid): grid.append([False for _ in range(7)])
#     elif (i % 5 == 4):
#         while y + 1 >= len(grid): grid.append([False for _ in range(7)])
#     else:
#         while y >= len(grid): grid.append([False for _ in range(7)])

#     while True:
#         inst = instructions[inst_counter]
#         #print(x, y, inst)

#         if (inst == ">"): kx = 1
#         else: kx = -1
        
#         # Wide 4
#         if (i % 5 == 0):
#             if (0 <= x + kx < 7 and x + kx + 4 <= 7 and True not in grid[y][x + kx : x + kx + 4]):
#                 x += kx
#             inst_counter += 1
#             if (inst_counter == len(instructions)): inst_counter = 0
            
#             if (y == 0): break
#             if (True not in grid[y - 1][x : x + 4]):
#                 y -= 1
#             else: break

#         # Cross
#         elif (i % 5 == 1):
#             if (0 <= x + kx < 7 and 0 <= x + kx + 2 < 7):
#                 if (not (grid[y + 1][x + kx] or grid[y + 1][x + kx + 1] or grid[y + 1][x + kx + 2] or
#                     grid[y + 2][x + kx + 1] or grid[y][x + kx + 1])):
#                     x += kx
#             inst_counter += 1
#             if (inst_counter == len(instructions)): inst_counter = 0        
            
#             if (y == 0): break
#             if (not (grid[y][x] or grid[y][x + 1] or grid[y][x + 2] or grid[y + 1][x + 1] or grid[y - 1][x + 1])):
#                 y -= 1
#             else: break
            
#         # L
#         elif (i % 5 == 2):
#             if (0 <= x + kx < 7 and 0 <= x + kx + 2 < 7):
#                 if (not (grid[y][x + kx] or grid[y][x + kx + 1] or grid[y][x + kx + 2] or grid[y + 1][x + kx + 2] or grid[y + 2][x + kx + 2])):
#                     x += kx
#             inst_counter += 1
#             if (inst_counter == len(instructions)): inst_counter = 0

#             if (y == 0): break
#             if (not (grid[y - 1][x] or grid[y - 1][x + 1] or grid[y - 1][x + 2] or grid[y][x + 2] or grid[y + 1][x + 2])):
#                 y -= 1
#             else: break

#         # Tall 4
#         elif (i % 5 == 3):
#             if (0 <= x + kx < 7):
#                 if (not (grid[y][x + kx] or grid[y + 1][x + kx] or grid[y + 2][x + kx] or grid[y + 3][x + kx])):
#                     x += kx
#             inst_counter += 1
#             if (inst_counter == len(instructions)): inst_counter = 0

#             if (y == 0): break
#             if (not (grid[y - 1][x] or grid[y][x] or grid[y + 1][x] or grid[y + 2][x])):
#                 y -= 1
#             else: break

#         # Square
#         else:
#             if (0 <= x + kx < 7 and 0 <= x + kx + 1 < 7):
#                 if (not (grid[y][x + kx] or grid[y][x + kx + 1] or grid[y + 1][x + kx] or grid[y + 1][x + kx + 1])):
#                     x += kx
#             inst_counter += 1
#             if (inst_counter == len(instructions)): inst_counter = 0

#             if (y == 0): break
#             if (not (grid[y - 1][x] or grid[y - 1][x + 1] or grid[y][x] or grid[y][x + 1])):
#                 y -= 1
#             else: break
    
#     if (i % 5 == 0):
#         # Place wide 4
#         for x2 in range(x, x + 4): grid[y][x2] = True
#         height = max(height, y + 1)
#     elif (i % 5 == 1):
#         # Place cross
#         grid[y][x + 1] = True
#         grid[y + 1][x] = True
#         grid[y + 1][x + 1] = True
#         grid[y + 1][x + 2] = True
#         grid[y + 2][x + 1] = True

#         height = max(height, y + 3)
#     elif (i % 5 == 2):
#         # Place L
#         grid[y][x] = True
#         grid[y][x + 1] = True
#         grid[y][x + 2] = True
#         grid[y + 1][x + 2] = True
#         grid[y + 2][x + 2] = True
        
#         height = max(height, y + 3)
#     elif (i % 5 == 3):
#         # Place tall 4
#         grid[y][x] = True
#         grid[y + 1][x] = True
#         grid[y + 2][x] = True
#         grid[y + 3][x] = True
        
#         height = max(height, y + 4)
#     else:
#         # Place square
#         grid[y][x] = True
#         grid[y][x + 1] = True
#         grid[y + 1][x] = True
#         grid[y + 1][x + 1] = True
        
#         height = max(height, y + 2)

#     # print(height)
#     # for x in grid[::-1]:
#     #     for y in x:
#     #         if (y): print("#", end = '')
#     #         else: print(".", end = "")
#     #     print()
#     # print()
# print(height)
# print(time.time() - start_time)

##########
# PART 2 #
##########

N = 1000000000000

start_time = time.time()
instructions = list(open("input.txt", "r+").read().split("\n")[0])
inst_counter = 0
height = 0
Height = 0
grid = []
lasts = [None for _ in range(len(instructions))]
shape = 0
cycle_found = False
while shape < N:
    # Expand the grid
    x, y = 2, height + 3
    if (shape % 5 == 1 or shape % 5 == 2):
        while y + 2 >= len(grid): grid.append([False for _ in range(7)])
    elif (shape % 5 == 3 and y + 3 >= len(grid)):
        while y + 3 >= len(grid): grid.append([False for _ in range(7)])
    elif (shape % 5 == 4):
        while y + 1 >= len(grid): grid.append([False for _ in range(7)])
    else:
        while y >= len(grid): grid.append([False for _ in range(7)])

    while True:
        inst = instructions[inst_counter]
        #print(x, y, inst)

        if (inst == ">"): kx = 1
        else: kx = -1
        
        # Wide 4
        if (shape % 5 == 0):
            if (0 <= x + kx < 7 and x + kx + 4 <= 7 and True not in grid[y][x + kx : x + kx + 4]):
                x += kx
            inst_counter += 1
            if (inst_counter == len(instructions)): inst_counter = 0
            
            if (y == 0): break
            if (True not in grid[y - 1][x : x + 4]):
                y -= 1
            else: break

        # Cross
        elif (shape % 5 == 1):
            if (0 <= x + kx < 7 and 0 <= x + kx + 2 < 7):
                if (not (grid[y + 1][x + kx] or grid[y + 1][x + kx + 1] or grid[y + 1][x + kx + 2] or
                    grid[y + 2][x + kx + 1] or grid[y][x + kx + 1])):
                    x += kx
            inst_counter += 1
            if (inst_counter == len(instructions)): inst_counter = 0        
            
            if (y == 0): break
            if (not (grid[y][x] or grid[y][x + 1] or grid[y][x + 2] or grid[y + 1][x + 1] or grid[y - 1][x + 1])):
                y -= 1
            else: break
            
        # L
        elif (shape % 5 == 2):
            if (0 <= x + kx < 7 and 0 <= x + kx + 2 < 7):
                if (not (grid[y][x + kx] or grid[y][x + kx + 1] or grid[y][x + kx + 2] or grid[y + 1][x + kx + 2] or grid[y + 2][x + kx + 2])):
                    x += kx
            inst_counter += 1
            if (inst_counter == len(instructions)): inst_counter = 0

            if (y == 0): break
            if (not (grid[y - 1][x] or grid[y - 1][x + 1] or grid[y - 1][x + 2] or grid[y][x + 2] or grid[y + 1][x + 2])):
                y -= 1
            else: break

        # Tall 4
        elif (shape % 5 == 3):
            if (0 <= x + kx < 7):
                if (not (grid[y][x + kx] or grid[y + 1][x + kx] or grid[y + 2][x + kx] or grid[y + 3][x + kx])):
                    x += kx
            inst_counter += 1
            if (inst_counter == len(instructions)): inst_counter = 0

            if (y == 0): break
            if (not (grid[y - 1][x] or grid[y][x] or grid[y + 1][x] or grid[y + 2][x])):
                y -= 1
            else: break

        # Square
        else:
            if (0 <= x + kx < 7 and 0 <= x + kx + 1 < 7):
                if (not (grid[y][x + kx] or grid[y][x + kx + 1] or grid[y + 1][x + kx] or grid[y + 1][x + kx + 1])):
                    x += kx
            inst_counter += 1
            if (inst_counter == len(instructions)): inst_counter = 0

            if (y == 0): break
            if (not (grid[y - 1][x] or grid[y - 1][x + 1] or grid[y][x] or grid[y][x + 1])):
                y -= 1
            else: break
    
    if (shape % 5 == 0):
        # Place wide 4
        for x2 in range(x, x + 4): grid[y][x2] = True
        height = max(height, y + 1)
    elif (shape % 5 == 1):
        # Place cross
        grid[y][x + 1] = True
        grid[y + 1][x] = True
        grid[y + 1][x + 1] = True
        grid[y + 1][x + 2] = True
        grid[y + 2][x + 1] = True

        height = max(height, y + 3)
    elif (shape % 5 == 2):
        # Place L
        grid[y][x] = True
        grid[y][x + 1] = True
        grid[y][x + 2] = True
        grid[y + 1][x + 2] = True
        grid[y + 2][x + 2] = True
        
        height = max(height, y + 3)
    elif (shape % 5 == 3):
        # Place tall 4
        grid[y][x] = True
        grid[y + 1][x] = True
        grid[y + 2][x] = True
        grid[y + 3][x] = True
        
        height = max(height, y + 4)
    else:
        # Place square
        grid[y][x] = True
        grid[y][x + 1] = True
        grid[y + 1][x] = True
        grid[y + 1][x + 1] = True
        
        height = max(height, y + 2)
    
    # Check if region blocked
    if (height > 1):
        for i in range(height - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                found = True
                for k in range(7):
                    if (not (grid[i][k] or grid[j][k])):
                        found = False
                        break
                # Everything at or below row i is obscured by row i + row j
                if (found and j != 0):
                    #print("Block", i, j)
                    L = len(grid[:j])
                    grid = grid[j:height]
                    y = 0
                    if (j > 0): Height += L
                    height = len(grid)
                    break
            if (found): break
    
    if (not cycle_found):
        for k in range(len(instructions)):
            if (inst_counter == k):
                if lasts[k] != None:
                    if (shape % 5 == lasts[k][0] and height == lasts[k][1]):
                        flag = True
                        for i in range(len(grid)):
                            for j in range(7):
                                if (grid[i][j] != lasts[k][2][i][j]):
                                    flag = False
                                    break
                        # Cycle found!
                        if (flag):
                            print(k, shape, lasts[k][-2], lasts[k][-1], height + Height)
                            iter_diff = shape - lasts[k][-2]
                            num_repeats = (N - shape)//(iter_diff)
                            shape += iter_diff * num_repeats
                            Height += num_repeats * (height + Height - lasts[k][-1])
                            cycle_found = True
                            break
                lasts[k] = (shape % 5, height, [[y for y in x] for x in grid], shape, height + Height)
    shape += 1
        
print(Height + height)
print(time.time() - start_time)