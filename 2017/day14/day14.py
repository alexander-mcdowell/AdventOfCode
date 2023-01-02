import time

##########
# PART 1 #
##########

# start_time = time.time()
# key = open("input.txt").read().split("\n")[0]

# def get_hash(s):
#     lengths = [ord(x) for x in s if x != '']
#     lengths += [17, 31, 73, 47, 23]
#     arr = list(range(256))
#     pos = 0
#     skip_size = 0
#     for _ in range(64):
#         for length in lengths:
#             subarray = []
#             i = pos
#             for _ in range(length):
#                 subarray.append(arr[i])
#                 i = (i + 1) % len(arr)
#             for j in range(length):
#                 i = (i - 1) % len(arr)
#                 arr[i] = subarray[j]
#             pos = (pos + length + skip_size) % len(arr)
#             skip_size += 1
#     s = ""
#     for i in range(16):
#         val = 0
#         for j in range(16 * i, 16 * (i + 1)):
#             val ^= arr[j]
#         h = hex(val)[2:]
#         if (len(h) == 1): h = '0' + h
#         s += h
#     return s

# def to_bin(x):
#     if (ord(x) >= ord('a')): return bin(int(10 + ord(x) - ord('a')))[2:]
#     return bin(int(x))[2:]

# count = 0
# for k in range(128):
#     hash = get_hash(key + "-" + str(k))
#     row = [to_bin(c) for c in hash]
#     count += ("".join(row)).count('1')
# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
key = open("input.txt").read().split("\n")[0]

def get_hash(s):
    lengths = [ord(x) for x in s if x != '']
    lengths += [17, 31, 73, 47, 23]
    arr = list(range(256))
    pos = 0
    skip_size = 0
    for _ in range(64):
        for length in lengths:
            subarray = []
            i = pos
            for _ in range(length):
                subarray.append(arr[i])
                i = (i + 1) % len(arr)
            for j in range(length):
                i = (i - 1) % len(arr)
                arr[i] = subarray[j]
            pos = (pos + length + skip_size) % len(arr)
            skip_size += 1
    s = ""
    for i in range(16):
        val = 0
        for j in range(16 * i, 16 * (i + 1)):
            val ^= arr[j]
        h = hex(val)[2:]
        if (len(h) == 1): h = '0' + h
        s += h
    return s

def to_bin(x):
    if (ord(x) >= ord('a')): return bin(int(10 + ord(x) - ord('a')))[2:]
    s = bin(int(x))[2:]
    if (len(s) < 4): s = (4 - len(s)) * '0' + s
    return s

grid = []
points = []
for k in range(128):
    hash = get_hash(key + "-" + str(k))
    row = []
    i = 0
    for c in hash:
        for x in to_bin(c):
            if (x == '1'):
                row.append(True)
                points.append((k, i))
            else: row.append(False)
            i += 1
    grid.append(row)

def explore(point, grid):
    prev = set()
    stack = [point]
    while (len(stack) != 0):
        point = stack.pop(-1)
        prev.add(point)
        for adj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (0 <= point[0] + adj[0] < 128 and 0 <= point[1] + adj[1] < 128):
                point2 = (point[0] + adj[0], point[1] + adj[1])
                if (point2 not in prev and grid[point2[0]][point2[1]]): stack.append(point2)
    return prev

groups = 0
while (len(points) != 0):
    point = points[0]
    for point in explore(point, grid): points.remove(point)
    groups += 1
print(groups)
print(time.time() - start_time)