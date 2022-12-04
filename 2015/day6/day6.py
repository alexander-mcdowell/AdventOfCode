##########
# PART 1 #
##########

"""
data = open("day6in.txt").read().split("\n")
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "toggle"):
        x1, y1 = [int(k) for k in inst[1].split(",")]
        x2, y2 = [int(k) for k in inst[3].split(",")]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x] = 1 - grid[y - 1][x - 1]
    elif (inst[0] == "turn"):
        x1, y1 = [int(k) for k in inst[2].split(",")]
        x2, y2 = [int(k) for k in inst[4].split(",")]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                k = 0
                if (inst[1] == "on"): k = 1
                elif (inst[1] == "off"): k = 0
                grid[y][x] = k
count = 0
for x in grid: count += sum(x)
print(count)
"""

##########
# PART 2 #
##########

data = open("day6in.txt").read().split("\n")
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "toggle"):
        x1, y1 = [int(k) for k in inst[1].split(",")]
        x2, y2 = [int(k) for k in inst[3].split(",")]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x] += 2
    elif (inst[0] == "turn"):
        x1, y1 = [int(k) for k in inst[2].split(",")]
        x2, y2 = [int(k) for k in inst[4].split(",")]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                k = 0
                if (inst[1] == "on"): grid[y][x] += 1
                elif (inst[1] == "off"): grid[y][x] = max(0, grid[y][x] - 1)
count = 0
for x in grid: count += sum(x)
print(count)