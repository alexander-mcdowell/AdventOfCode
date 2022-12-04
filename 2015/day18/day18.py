##########
# PART 1 #
##########

"""
data = open("day18in.txt").read().split("\n")
grid = [list(x) for x in data]

def step(grid):
    n, m = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(n):
        for j in range(m):
            neighbors = []
            if (i > 0):
                if (j > 0): neighbors.append(int(grid[i - 1][j - 1] == '#'))
                neighbors.append(int(grid[i - 1][j] == '#'))
                if (j < m - 1): neighbors.append(int(grid[i - 1][j + 1] == '#'))
            if (j > 0): neighbors.append(int(grid[i][j - 1] == '#'))
            if (j < m - 1): neighbors.append(int(grid[i][j + 1] == '#'))
            if (i < n - 1):
                if (j > 0): neighbors.append(int(grid[i + 1][j - 1] == '#'))
                neighbors.append(int(grid[i + 1][j] == '#'))
                if (j < m - 1): neighbors.append(int(grid[i + 1][j + 1] == '#'))
            
            x = sum(neighbors)
            if (grid[i][j] == '#'):
                if (x == 2 or x == 3): new_grid[i][j] = '#'
                else: new_grid[i][j] = '.'
            else:
                if (x == 3): new_grid[i][j] = '#'
                else: new_grid[i][j] = '.'
    return new_grid

N = 100
for k in range(N):
    grid = step(grid)

count = 0
for x in grid:
    for y in x:
        if (y == '#'): count += 1
print(count)
"""

##########
# PART 2 #
##########

data = open("day18in.txt").read().split("\n")
grid = [list(x) for x in data]
for i, j in [(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)]:
    grid[i][j] = '#'

def step(grid):
    n, m = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(n):
        for j in range(m):
            if ((i, j) in [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]):
                new_grid[i][j] = '#'
                continue

            neighbors = []
            if (i > 0):
                if (j > 0): neighbors.append(int(grid[i - 1][j - 1] == '#'))
                neighbors.append(int(grid[i - 1][j] == '#'))
                if (j < m - 1): neighbors.append(int(grid[i - 1][j + 1] == '#'))
            if (j > 0): neighbors.append(int(grid[i][j - 1] == '#'))
            if (j < m - 1): neighbors.append(int(grid[i][j + 1] == '#'))
            if (i < n - 1):
                if (j > 0): neighbors.append(int(grid[i + 1][j - 1] == '#'))
                neighbors.append(int(grid[i + 1][j] == '#'))
                if (j < m - 1): neighbors.append(int(grid[i + 1][j + 1] == '#'))
            
            x = sum(neighbors)
            if (grid[i][j] == '#'):
                if (x == 2 or x == 3): new_grid[i][j] = '#'
                else: new_grid[i][j] = '.'
            else:
                if (x == 3): new_grid[i][j] = '#'
                else: new_grid[i][j] = '.'
    return new_grid

N = 100
for k in range(N):
    grid = step(grid)

count = 0
for x in grid:
    for y in x:
        if (y == '#'): count += 1
print(count)