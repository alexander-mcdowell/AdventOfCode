import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = [list(line) for line in data]
shifted = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (shifted[i][j] != 'O'): continue
        k = i - 1
        while k >= 0:
            if (shifted[k][j] != '.'): break
            k -= 1
        shifted[i][j] = '.'
        shifted[k + 1][j] = 'O'
total = 0
for i in range(len(shifted)):
    index = len(grid) - i
    total += index * shifted[i].count('O')
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

def shift(grid, dir):
    shifted = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    # North
    if (dir == 0):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (shifted[i][j] != 'O'): continue
                k = i - 1
                while k >= 0:
                    if (shifted[k][j] != '.'): break
                    k -= 1
                shifted[i][j] = '.'
                shifted[k + 1][j] = 'O'
    # West
    elif (dir == 1):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (shifted[i][j] != 'O'): continue
                k = j - 1
                while k >= 0:
                    if (shifted[i][k] != '.'): break
                    k -= 1
                shifted[i][j] = '.'
                shifted[i][k + 1] = 'O'
    # South
    elif (dir == 2):
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i])):
                if (shifted[i][j] != 'O'): continue
                k = i + 1
                while k < len(grid):
                    if (shifted[k][j] != '.'): break
                    k += 1
                shifted[i][j] = '.'
                shifted[k - 1][j] = 'O'
    # East
    else:
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1, -1, -1):
                if (shifted[i][j] != 'O'): continue
                k = j + 1
                while k < len(grid[i]):
                    if (shifted[i][k] != '.'): break
                    k += 1
                shifted[i][j] = '.'
                shifted[i][k - 1] = 'O'
    return shifted

def stringify(grid):
    s = ""
    for row in grid: s += "".join(row)
    return s

start_time = time.time()
record = {stringify(grid): 0}
cycles = 1
shifted = grid
while True:
    for i in range(4): shifted = shift(shifted, i)
    s = stringify(shifted)
    if (s in record):
        # Repeats in cycle [record[s], cycles - 1]
        # (record[s] + k * period, record[s] + k * period) ==> (record[s], record[s] + period - 1)
        rev_record = {record[k]: k for k in record}
        period = cycles - record[s]
        target = (10**9 - record[s]) % period + record[s]
        t = rev_record[target]
        shifted = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])): row.append(t[len(grid[i]) * i + j])
            shifted.append(row)

        total = 0
        for i in range(len(shifted)):
            index = len(grid) - i
            total += index * shifted[i].count('O')
        break
    else: record[s] = cycles
    cycles += 1
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")