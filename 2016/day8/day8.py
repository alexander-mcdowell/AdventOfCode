##########
# PART 1 #
##########

"""
data = open("day8in.txt").read().split("\n")
n, m = 6, 50
grid = [[0 for _ in range(m)] for _ in range(n)]

for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "rect"):
        x, y = [int(k) for k in inst[1].split('x')]
        x, y = min(x, m - 1), min(y, n - 1)
        for i in range(y):
            for j in range(x): grid[i][j] = 1
        
    elif (inst[0] == "rotate"):
        if (inst[1] == "row"):
            r = int(inst[2][2:])
            k = int(inst[-1])
            
            new_row = [0 for _ in range(m)]
            for j in range(m): new_row[(j + k) % m] = grid[r][j]
            for j in range(m): grid[r][j] = new_row[j]
            
        elif (inst[1] == "column"):
            c = int(inst[2][2:])
            k = int(inst[-1])
            
            new_col = [0 for _ in range(n)]
            for j in range(n): new_col[(j + k) % n] = grid[j][c]
            for j in range(n): grid[j][c] = new_col[j]

count = 0
for x in grid: count += sum(x)
print(count)
"""

##########
# PART 2 #
##########

data = open("day8in.txt").read().split("\n")
n, m = 6, 50
grid = [[0 for _ in range(m)] for _ in range(n)]

for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "rect"):
        x, y = [int(k) for k in inst[1].split('x')]
        x, y = min(x, m - 1), min(y, n - 1)
        for i in range(y):
            for j in range(x): grid[i][j] = 1
        
    elif (inst[0] == "rotate"):
        if (inst[1] == "row"):
            r = int(inst[2][2:])
            k = int(inst[-1])
            
            new_row = [0 for _ in range(m)]
            for j in range(m): new_row[(j + k) % m] = grid[r][j]
            for j in range(m): grid[r][j] = new_row[j]
            
        elif (inst[1] == "column"):
            c = int(inst[2][2:])
            k = int(inst[-1])
            
            new_col = [0 for _ in range(n)]
            for j in range(n): new_col[(j + k) % n] = grid[j][c]
            for j in range(n): grid[j][c] = new_col[j]

for x in grid:
    for y in x: print('#' if y == 1 else ' ', end = '')
    print()