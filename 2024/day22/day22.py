import time

# ##########
# # PART 1 #
# ##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# N = 2000
# total = 0
# for l in data:
#     x = int(l)
#     for _ in range(N):
#         x = ((x * 64) ^ x) % 16777216
#         x = ((x // 32) ^ x) % 16777216
#         x = ((x * 2048) ^ x) % 16777216
#     total += x
# print(total)
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")

M = 2**24
N = 2000

# total = 0
all_seq = {}
i = 0
for l in data:
    x = int(l)
    last = x % 10
    k = 0
    seq = [x % 10]
    for _ in range(N):
        x = ((x << 6) ^ x) % M
        x = ((x >> 5) ^ x) % M
        x = ((x << 11) ^ x) % M
        diff = (x%10) - last
        last = x % 10
        
        seq.append(diff)
        if (len(seq) > 4): seq.pop(0)
        if (len(seq) == 4):
            if (tuple(seq) not in all_seq):
                all_seq[tuple(seq)] = [0 for _ in range(len(data))]
                all_seq[tuple(seq)][i] = x % 10
            elif (all_seq[tuple(seq)][i] == 0): all_seq[tuple(seq)][i] = x % 10
    i += 1
best = 0
for s in all_seq:
    x = sum(all_seq[s])
    if (x > best): best = x
print(best)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")