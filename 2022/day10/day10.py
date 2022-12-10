import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# i = 1
# X = 1
# total = 0
# desired_cycles = [20, 60, 100, 140, 180, 220]
# for line in lines:
#     if (line == "noop"):
#         if (i in desired_cycles):
#             total += X * i
#     else:
#         value = int(line.split(" ")[1])
#         if (i in desired_cycles):
#             total += X * i
#         i += 1
#         if (i in desired_cycles):
#             total += X * i
#         X += value
#     i += 1
# print(total)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = [["." for _ in range(40)] for _ in range(6)]
i = 0
X = 1
total = 0
for line in lines:
    row_num, col_num = i // 40, i % 40
    if (line == "noop"):
        if (X - 1 <= i % 40 <= X + 1): c = "#"
        else: c = "."
        grid[row_num][col_num] = c
    else:
        value = int(line.split(" ")[1])

        if (X - 1 <= i % 40 <= X + 1): c = "#"
        else: c = "."
        grid[row_num][col_num] = c
        i += 1

        row_num, col_num = i // 40, i % 40
        if (X - 1 <= i % 40 <= X + 1): c = "#"
        else: c = "."
        grid[row_num][col_num] = c
        X += value
    i += 1
for row in grid:
    print("".join(row))
print(time.time() - start_time)