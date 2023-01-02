import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# scanners = {}
# for line in lines:
#     depth, r = line.split(": ")
#     scanners[int(depth)] = [0, int(r) - 1, 1]
# caught_score = 0
# for pos in range(max(scanners) + 1):
#     if (pos in scanners and scanners[pos][0] == 0):
#         caught_score += pos * (1 + scanners[pos][1])
#     for k in scanners:
#         if (scanners[k][0] == scanners[k][1] and scanners[k][2] == 1): scanners[k][2] = -1
#         if (scanners[k][0] == 0 and scanners[k][2] == -1): scanners[k][2] = 1
#         scanners[k][0] += scanners[k][2]
# print(caught_score)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
scanners = {}
for line in lines:
    depth, r = line.split(": ")
    scanners[int(depth)] = 2 * (int(r) - 1)
keys = list(scanners)

t = 0
while True:
    valid = True
    for k in scanners:
        if ((t + k) % scanners[k] == 0):
            valid = False
            break
    if (valid):
        print(t)
        break
    t += 1
print(time.time() - start_time)