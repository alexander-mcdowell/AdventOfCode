import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# grid = [[int(x) for x in line] for line in lines]
# visible = 0
# for i in range(1, len(grid) - 1):
#     for j in range(1, len(grid[i]) - 1):
#         # Left
#         flag = True
#         for k in range(1, j + 1):
#             if (grid[i][j] <= grid[i][j - k]):
#                 flag = False
#                 break
#         if (flag):
#             visible += 1
#             continue
#         # Right
#         flag = True
#         for k in range(1, len(grid[i]) - j):
#             if (grid[i][j] <= grid[i][j + k]):
#                 flag = False
#                 break
#         if (flag):
#             visible += 1
#             continue
#         # Up
#         flag = True
#         for k in range(1, i + 1):
#             if (grid[i][j] <= grid[i - k][j]):
#                 flag = False
#                 break
#         if (flag):
#             visible += 1
#             continue
#         # Down
#         flag = True
#         for k in range(1, len(grid) - i):
#             if (grid[i][j] <= grid[i + k][j]):
#                 flag = False
#                 break
#         if (flag):
#             visible += 1
# print(visible + 2 * len(grid) + 2 * len(grid[0]) - 4)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = [[int(x) for x in line] for line in lines]
max_score = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        score = 1
        
        # Left
        count = 0
        for k in range(1, j + 1):
            count += 1
            if (grid[i][j] <= grid[i][j - k]):
                break
        score *= count
        # Right
        count = 0
        for k in range(1, len(grid[i]) - j):
            count += 1
            if (grid[i][j] <= grid[i][j + k]):
                break
        score *= count
        # Up
        count = 0
        for k in range(1, i + 1):
            count += 1
            if (grid[i][j] <= grid[i - k][j]):
                break
        score *= count
        # Down
        count = 0
        for k in range(1, len(grid) - i):
            count += 1
            if (grid[i][j] <= grid[i + k][j]):
                break
        score *= count
        
        if (score > max_score):
            max_score = score
print(max_score)
print(time.time() - start_time)