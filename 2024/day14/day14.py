import time

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
N = 100
W, H = 101, 103
counts = {}
for l in data:
    s, s2 = l.split(" ")
    s = s.split(",")
    x, y = int(s[0].split("=")[1]), int(s[1])
    s2 = s2.split(",")
    vx, vy = int(s2[0].split("=")[1]), int(s2[1])
    x2, y2 = (x + vx*N) % W, (y + vy*N) % H
    if ((x2, y2) not in counts): counts[(x2, y2)] = 1
    else: counts[(x2, y2)] += 1
q1, q2, q3, q4 = 0, 0, 0, 0
# Assume odd W and H
midx, midy = (W-1)//2, (H-1)//2
for p in counts:
    x, y = p
    if (x < midx and y < midy): q1 += counts[p]
    elif (x > midx and y < midy): q2 += counts[p]
    elif (x < midx and y > midy): q3 += counts[p]
    elif (x > midx and y > midy): q4 += counts[p]
print(q1, q2, q3, q4, q1 * q2 * q3 * q4)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

import os

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
# 22, 98, 123
N = 22 + 65 * 101
W, H = 101, 103

# while True:
#     os.system('cls')
counts = {}
for l in data:
    s, s2 = l.split(" ")
    s = s.split(",")
    x, y = int(s[0].split("=")[1]), int(s[1])
    s2 = s2.split(",")
    vx, vy = int(s2[0].split("=")[1]), int(s2[1])
    x2, y2 = (x + vx*N) % W, (y + vy*N) % H
    if ((x2, y2) not in counts): counts[(x2, y2)] = 1
    else: counts[(x2, y2)] += 1
grid = [['.' for _ in range(W)] for _ in range(H)]
for p in counts:
    grid[p[1]][p[0]] = '#'
for row in grid: print("".join(row))
# print(N)
# time.sleep(0.75)
# N += 101