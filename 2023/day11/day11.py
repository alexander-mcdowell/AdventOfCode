import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
for line in data: grid.append(list(line))
safe_rows, safe_cols = [], []
for i in range(len(grid)):
    if ('#' not in grid[i]): safe_rows.append(i)
for i in range(len(grid)):
    if ('#' not in [grid[j][i] for j in range(len(grid[i]))]): safe_cols.append(i)
enlarged = []
for i in range(len(grid)):
    if (i in safe_rows):
        enlarged.append(['.'] * (len(grid) + len(safe_cols)))
        enlarged.append(['.'] * (len(grid) + len(safe_cols)))
        continue
    row = []
    for j in range(len(grid[i])):
        row.append(grid[i][j])
        if (j in safe_cols): row.append('.')
    enlarged.append(row)

galaxies = []
for i in range(len(enlarged)):
    for j in range(len(enlarged[i])):
        if (enlarged[i][j] == '#'): galaxies.append((i, j))
total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        total += dist
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
for line in data: grid.append(list(line))
safe_rows, safe_cols = [], []
for i in range(len(grid)):
    if ('#' not in grid[i]): safe_rows.append(i)
for i in range(len(grid)):
    if ('#' not in [grid[j][i] for j in range(len(grid[i]))]): safe_cols.append(i)

enlarge_size = 1000000

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == '#'):
            row_increases, col_increases = 0, 0
            for x in safe_rows:
                if (x < i): row_increases += 1
                else: break 
            for x in safe_cols:
                if (x < j): col_increases += 1
                else: break 
            galaxies.append((i + (enlarge_size-1) * row_increases, j + (enlarge_size - 1) * col_increases))
total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        total += dist
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")