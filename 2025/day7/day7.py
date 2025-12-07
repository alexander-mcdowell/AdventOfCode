import timeit

##########
# PART 1 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
matrix = []
start = None
i = 0
for row in data:
    j = 0
    arr = []
    for c in row:
        if c=="S":
            start = (i, j)
        arr.append(c)
        j += 1
    i += 1
    matrix.append(arr)

count = 0
seen = set()
def beam(pos):
    global count
    for i in range(pos[0], len(matrix)):
        if ((i, pos[1]) in seen): return
        seen.add((i, pos[1]))
        if matrix[i][pos[1]]=='^':
            count += 1
            beam((i, pos[1] - 1))
            beam((i, pos[1] + 1))
            return
beam(start)
print(count)
print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

import heapq

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
matrix = []
start = None
i = 0
for row in data:
    j = 0
    arr = []
    for c in row:
        if c=="S":
            start = (i, j)
        arr.append(c)
        j += 1
    i += 1
    matrix.append(arr)

for i in range(start[0], len(matrix)):
    if matrix[i][start[1]]=='^':
        start = (i, start[1])
        break
D = {start: 1}
queue = [start]
seen = set([start])

count = 0
while len(queue) != 0:
    pos = heapq.heappop(queue)
    for split_pos in [(pos[0], pos[1]-1), (pos[0], pos[1]+1)]:
        found = False
        for i in range(split_pos[0], len(matrix)):
            if matrix[i][split_pos[1]]=='^':
                next_pos = (i, split_pos[1])
                if next_pos not in seen:
                    heapq.heappush(queue, (i, next_pos[1]))
                    seen.add((i, next_pos[1]))
                if next_pos not in D: D[next_pos] = D[pos]
                else: D[next_pos] += D[pos]

                found = True
                break
        if not found:
            count += D[pos]
print(count)
print(timeit.default_timer() - start_time)