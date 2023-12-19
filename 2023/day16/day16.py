import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
grid = [list(row) for row in data]
n, m = len(grid), len(grid[0])
energized = [[False for _ in range(m)] for _ in range(n)]

# 0 = right, 1 = down, 2 = left, 3 = up
stack = [(0, 0, 0)]
seen = set()
while len(stack) != 0:
    i, j, inst = stack.pop()
    if ((i, j, inst) in seen): continue
    seen.add((i, j, inst))

    delta = 1 if inst in [0, 1] else -1
    # Right / Left
    if (inst in [0, 2]):
        k = j
        while 0 <= k < m:
            energized[i][k] = True
            if (grid[i][k] in ['/', '|', '\\']):
                if (grid[i][k] == '/'): stack.append((i - delta, k, 3 if inst == 0 else 1))
                elif (grid[i][k] == '|'):
                    stack.append((i + 1, k, 1))
                    stack.append((i - 1, k, 3))
                else: stack.append((i + delta, k, 1 if inst == 0 else 3))
                break
            k += delta
    # Down / Up
    else:
        k = i
        while 0 <= k < n:
            energized[k][j] = True
            if (grid[k][j] in ['/', '-', '\\']):
                if (grid[k][j] == '/'): stack.append((k, j - delta, 2 if inst == 1 else 0))
                elif (grid[k][j] == '-'):
                    stack.append((k, j + 1, 0))
                    stack.append((k, j - 1, 2))
                else: stack.append((k, j + delta, 0 if inst == 1 else 2))
                break
            k += delta

total = 0
for row in energized: total += row.count(True)
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()

# 0 = right, 1 = down, 2 = left, 3 = up
energized_max = 0
start_poses = [(0, x, 1) for x in range(m)] + [(n - 1, x, 3) for x in range(m)] + [(x, 0, 0) for x in range(n)] + [(x, m - 1, 2) for x in range(n)]
for pos in start_poses:
    stack = [pos]
    energized = [[False for _ in range(m)] for _ in range(n)]
    seen = set()
    while len(stack) != 0:
        i, j, inst = stack.pop()
        if ((i, j, inst) in seen): continue
        seen.add((i, j, inst))

        delta = 1 if inst in [0, 1] else -1
        # Right / Left
        if (inst in [0, 2]):
            k = j
            while 0 <= k < m:
                energized[i][k] = True
                if (grid[i][k] in ['/', '|', '\\']):
                    if (grid[i][k] == '/'): stack.append((i - delta, k, 3 if inst == 0 else 1))
                    elif (grid[i][k] == '|'):
                        stack.append((i + 1, k, 1))
                        stack.append((i - 1, k, 3))
                    else: stack.append((i + delta, k, 1 if inst == 0 else 3))
                    break
                k += delta
        # Down / Up
        else:
            k = i
            while 0 <= k < n:
                energized[k][j] = True
                if (grid[k][j] in ['/', '-', '\\']):
                    if (grid[k][j] == '/'): stack.append((k, j - delta, 2 if inst == 1 else 0))
                    elif (grid[k][j] == '-'):
                        stack.append((k, j + 1, 0))
                        stack.append((k, j - 1, 2))
                    else: stack.append((k, j + delta, 0 if inst == 1 else 2))
                    break
                k += delta

    total = 0
    for row in energized: total += row.count(True)
    if (total > energized_max): energized_max = total
print(energized_max)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")