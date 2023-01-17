##########
# PART 1 #
##########

# import time

# start_time = time.time()
# serial = int(open("input.txt").read().strip())

# def get_power_level(x, y, serial):
#     rackID = x + 10
#     power = (rackID * y + serial) * rackID
#     power = ((power % 1000) - (power % 100))//100
#     return power - 5

# grid = []
# for y in range(1, 301):
#     row = []
#     for x in range(1, 301): row.append(get_power_level(x, y, serial))
#     grid.append(row)

# N = 3
# best, best_loc = -1, None
# for i in range(300 - N + 1):
#     for j in range(300 - N + 1):
#         S = sum([sum(row[j : j + N]) for row in grid[i : i + Ns]])
#         if (S > best):
#             best = S
#             best_loc = (j + 1, i + 1)
# print(best, best_loc)
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

start_time = time.time()
serial = int(open("input.txt").read().strip())

def get_power_level(x, y, serial):
    rackID = x + 10
    power = (rackID * y + serial) * rackID
    power = ((power % 1000) - (power % 100))//100
    return power - 5

grid = []
for y in range(1, 301):
    row = []
    for x in range(1, 301): row.append(get_power_level(x, y, serial))
    grid.append(row)

# Shitty approach that works. Try everything until it takes too long to discover the next best i, j, N
best, best_loc = -1, None
for N in range(1, 301):
    for i in range(300 - N + 1):
        for j in range(300 - N + 1):
            S = sum([sum(row[j : j + N]) for row in grid[i : i + N]])
            if (S > best):
                best = S
                best_loc = (j + 1, i + 1, N)
                print(best, best_loc)
print(best, best_loc)
print(time.time() - start_time)