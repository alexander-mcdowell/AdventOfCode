import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = [list(l) for l in data]
count = 0
for i in range(len(grid)):
    for j in range(len(grid) - 3):
        if ("".join(grid[i][j:j+4]) in ["XMAS", "SAMX"]): count += 1
for i in range(len(grid) - 3):
    for j in range(len(grid)):
        s = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
        if (s in ["XMAS", "SAMX"]): count += 1
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        s = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]
        if (s in ["XMAS", "SAMX"]): count += 1
for i in range(3, len(grid)):
    for j in range(len(grid) - 3):
        s = grid[i][j] + grid[i - 1][j + 1] + grid[i - 2][j + 2] + grid[i - 3][j + 3]
        if (s in ["XMAS", "SAMX"]): count += 1
print(count)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = [list(l) for l in data]
count = 0
for i in range(len(grid) - 2):
    for j in range(len(grid)-2):
        subgrid = [row[j:j+3] for row in grid[i:i+3]]
        diag1 = subgrid[0][0] + subgrid[1][1] + subgrid[2][2]
        diag2 = subgrid[2][0] + subgrid[1][1] + subgrid[0][2]
        if (diag1 in ["MAS", "SAM"] and diag2 in ["MAS", "SAM"]): count += 1
        
print(count)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()