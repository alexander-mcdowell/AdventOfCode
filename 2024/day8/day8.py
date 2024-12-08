import time
import math

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
antennaes = {}
grid = []
i = 0
for l in data:
    row = []
    j = 0
    for c in l:
        if (c != "."):
            if c not in antennaes: antennaes[c] = [(i, j)]
            else: antennaes[c].append((i, j))
        row.append(c)
        j += 1
    grid.append(row)
    i += 1

n, m = len(grid), len(grid[0])
antinodes = set()
for a_type in antennaes:
    arr = antennaes[a_type]
    for i in range(1, len(arr)):
        for j in range(i):
            a1, a2 = arr[i], arr[j]
            diff = [a2[0] - a1[0], a2[1] - a1[1]]
            g = math.gcd(diff[0], diff[1])
            diff = [diff[0]//g, diff[1]//g]
            
            for coeff in [1, -1]:
                y, x = a1[0] + coeff * diff[0], a1[1] + coeff * diff[1]
                if ((y, x) == a2): continue
                if (not (0 <= y < n and 0 <= x < m)): break
                antinodes.add((y, x))
            for coeff in [1, -1]:
                y, x = a2[0] + coeff * diff[0], a2[1] + coeff * diff[1]
                if ((y, x) == a1): continue
                if (not (0 <= y < n and 0 <= x < m)): break
                antinodes.add((y, x))
print(len(antinodes))
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
antennaes = {}
grid = []
i = 0
for l in data:
    row = []
    j = 0
    for c in l:
        if (c != "."):
            if c not in antennaes: antennaes[c] = [(i, j)]
            else: antennaes[c].append((i, j))
        row.append(c)
        j += 1
    grid.append(row)
    i += 1

n, m = len(grid), len(grid[0])
antinodes = set()
for a_type in antennaes:
    arr = antennaes[a_type]
    for i in range(1, len(arr)):
        for j in range(i):
            a1, a2 = arr[i], arr[j]
            diff = [a2[0] - a1[0], a2[1] - a1[1]]
            g = math.gcd(diff[0], diff[1])
            diff = [diff[0]//g, diff[1]//g]
            
            for sign in [1, -1]:
                y, x = a1
                while True:
                    y, x = y + sign * diff[0], x + sign * diff[1]
                    if (not (0 <= y < n and 0 <= x < m)): break
                    antinodes.add((y, x))
                y, x = a2
                while True:
                    y, x = y + sign * diff[0], x + sign * diff[1]
                    if (not (0 <= y < n and 0 <= x < m)): break
                    antinodes.add((y, x))
print(len(antinodes))
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()