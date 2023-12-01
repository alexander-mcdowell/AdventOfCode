import time

##########
# PART 1 #
##########

def flip(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i]) - 1, -1, -1): new_row.append(grid[i][j])
        new_grid.append(new_row)
    return new_grid

def rot(grid):
    pass

start_time = time.time()
lines = open("input.txt").read().split("\n")
pattern_map = {}
grid = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
for line in lines:
    line = line.split(" => ")
    pattern, replace = line
    pattern = [list(row) for row in pattern.split("/")]
    replace = [list(row) for row in replace.split("/")]
    pattern_map[pattern] = replace
print(time.time() - start_time)