import time

##########
# PART 1 #
##########

def find_row_reflect(grid):
    for i in range(len(grid)-1):
        j, k = i, i+1
        is_mirror = True
        while j>=0 and k<len(grid):
            if (grid[j] != grid[k]):
                is_mirror = False
                break
            j -= 1
            k += 1
        if (is_mirror): return i + 1
    return None

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
total = 0
for line in data:
    if (line == ""):
        transpose = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])): transpose[j][i] = grid[i][j]
        left_cols = find_row_reflect(transpose)
        if (left_cols != None): total += left_cols
        else:
            above_rows = find_row_reflect(grid)
            total += 100 * above_rows
        grid = []
    else: grid.append(list(line))
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

def find_row_reflect2(grid, ignore):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = "#" if grid[y][x] == "." else "."
            for i in range(len(grid)-1):
                j, k = i, i+1
                is_mirror = True
                while j>=0 and k<len(grid):
                    if (grid[j] != grid[k]):
                        is_mirror = False
                        break
                    j -= 1
                    k += 1
                if (is_mirror):
                    if (i + 1 != ignore): return i + 1
            grid[y][x] = "#" if grid[y][x] == "." else "."
    return None

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = []
total = 0
for line in data:
    if (line == ""):
        transpose = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])): transpose[j][i] = grid[i][j]
        left_cols = find_row_reflect2(transpose, find_row_reflect(transpose))
        if (left_cols != None): total += left_cols
        else:
            above_rows = find_row_reflect2(grid, find_row_reflect(grid))
            total += 100 * above_rows
        grid = []
    else: grid.append(list(line))
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")