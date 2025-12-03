import time

##########
# PART 1 #
##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# total = 0
# for l in data:
#     best = 0
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             best = max(best, int(l[i] + l[j]))
#     total += best
# print(total)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
for l in data:
    digits = [[] for _ in range(10)]
    for i in range(len(l)): digits[int(l[i])].append(i)
    for i in range(10): digits[i] = digits[i][::-1]

    count = 0
    best = 0
    last_i = -1
    for remaining in range(11, -1, -1):
        for x in range(9, -1, -1):
            while len(digits[x]) != 0:
                i = digits[x][-1]
                if i < last_i: digits[x].pop()
                else: break
            if (len(digits[x]) == 0): continue
            if (i + remaining < len(l)):
                digits[x].pop()
                best = 10 * best + x
                last_i = i
                break
    total += best
print(total)
print(time.time() - start_time)