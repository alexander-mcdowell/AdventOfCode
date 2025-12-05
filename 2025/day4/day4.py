import timeit

##########
# PART 1 #
##########

# start_time = timeit.default_timer()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# n, m = len(data), len(data[0])
# count = 0
# for i in range(n):
#     for j in range(m):
#         if data[i][j]==".": continue
#         adjacent_rolls = 0
#         for deltai in [-1, 0, 1]:
#             for deltaj in [-1, 0, 1]:
#                 if deltai==0 and deltaj == 0: continue
#                 i2, j2 = i + deltai, j + deltaj
#                 if (not (0 <= i2 < n and 0 <= j2 < m)): continue
#                 if data[i2][j2] == '@': adjacent_rolls += 1
#         if adjacent_rolls<4:
#             count += 1
# print(count)
# print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
grid = f.read().split("\n")
n, m = len(grid), len(grid[0])
count = 0
while True:
    removals = 0
    new_grid = [['.' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==".":
                new_grid[i][j] = '.'
                continue
            adjacent_rolls = 0
            for deltai in [-1, 0, 1]:
                for deltaj in [-1, 0, 1]:
                    if deltai==0 and deltaj == 0: continue
                    i2, j2 = i + deltai, j + deltaj
                    if (not (0 <= i2 < n and 0 <= j2 < m)): continue
                    if grid[i2][j2] == '@': adjacent_rolls += 1
            if adjacent_rolls<4:
                new_grid[i][j] = '.'
                count += 1
                removals += 1
            else: new_grid[i][j] = '@'
    if removals == 0: break
    grid = new_grid
print(count)
print(timeit.default_timer() - start_time)