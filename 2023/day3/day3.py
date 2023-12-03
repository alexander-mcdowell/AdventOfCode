import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = [list(line) for line in data]
nums = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]
        # Symbol
        if (c != "." and not (ord('0') <= ord(c) <= ord('9'))):
            for delta in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if (0 <= i + delta[0] < len(grid) and 0 <= j + delta[1] < len(grid[i])):
                    i2 = i + delta[0]
                    j2 = j + delta[1]
                    c2 = grid[i2][j2]
                    if (ord('0') <= ord(c2) <= ord('9')):
                        # Find start and end of number
                        start = j2
                        end = j2
                        while (start - 1 >= 0 and ord('0') <= ord(grid[i2][start - 1]) <= ord('9')): start -= 1
                        while (end + 1 < len(grid[i2]) and ord('0') <= ord(grid[i2][end + 1]) <= ord('9')): end += 1
                        s = "".join(grid[i2][start:end+1])
                        nums.add((i2, start, end, int(s)))
total = 0
for x in nums: total += x[-1]
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

grid = [list(line) for line in data]
gears = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]
        # Symbol
        if (c == "*"):
            for delta in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if (0 <= i + delta[0] < len(grid) and 0 <= j + delta[1] < len(grid[i])):
                    i2 = i + delta[0]
                    j2 = j + delta[1]
                    c2 = grid[i2][j2]
                    if (ord('0') <= ord(c2) <= ord('9')):
                        # Find start and end of number
                        start = j2
                        end = j2
                        while (start - 1 >= 0 and ord('0') <= ord(grid[i2][start - 1]) <= ord('9')): start -= 1
                        while (end + 1 < len(grid[i2]) and ord('0') <= ord(grid[i2][end + 1]) <= ord('9')): end += 1
                        s = "".join(grid[i2][start:end+1])
                        if ((i, j) not in gears): gears[(i, j)] = set()
                        gears[(i, j)].add((i2, start, end, int(s)))
total = 0
for x in gears:
    if (len(gears[x]) == 2):
        nums = list(gears[x])
        total += nums[0][-1] * nums[1][-1]
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()