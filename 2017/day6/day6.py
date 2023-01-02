import time

##########
# PART 1 #
##########

# start_time = time.time()
# blocks = [int(x) for x in open("input.txt").read().split("\n")[0].split("\t")]
# states = set([tuple(blocks)])
# steps = 1
# while True:
#     best_i, val = 0, -1
#     for i in range(len(blocks)):
#         if (val == -1 or blocks[i] > val):
#             best_i = i
#             val = blocks[i]
#     blocks[best_i] = 0
#     i = best_i
#     for _ in range(val):
#         i = (i + 1) % len(blocks)
#         blocks[i] += 1
#     b = tuple(blocks)
#     if (b in states):
#         print(steps)
#         break
#     states.add(b)
#     steps += 1
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
blocks = [int(x) for x in open("input.txt").read().split("\n")[0].split("\t")]
states = set([tuple(blocks)])
steps = 1
while True:
    best_i, val = 0, -1
    for i in range(len(blocks)):
        if (val == -1 or blocks[i] > val):
            best_i = i
            val = blocks[i]
    blocks[best_i] = 0
    i = best_i
    for _ in range(val):
        i = (i + 1) % len(blocks)
        blocks[i] += 1
    b = tuple(blocks)
    if (b in states): break
    states.add(b)
    steps += 1
target_blocks = tuple(blocks)
count = 1
while True:
    best_i, val = 0, -1
    for i in range(len(blocks)):
        if (val == -1 or blocks[i] > val):
            best_i = i
            val = blocks[i]
    blocks[best_i] = 0
    i = best_i
    for _ in range(val):
        i = (i + 1) % len(blocks)
        blocks[i] += 1
    b = tuple(blocks)
    if (b == target_blocks):
        print(count)
        break
    count += 1
print(time.time() - start_time)