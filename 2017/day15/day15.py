import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# A, B = int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])
# count = 0
# mask = (1 << 16) - 1
# for _ in range(40 * 10 ** 6):
#     A = (16807 * A) % 2147483647
#     B = (48271 * B) % 2147483647
#     if (A & mask == B & mask): count += 1
# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
A, B = int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])
count = 0
mask = (1 << 16) - 1
for i in range(5000000):
    while True:
        A = (16807 * A) % 2147483647
        if (A % 4 == 0): break
    while True:
        B = (48271 * B) % 2147483647
        if (B % 8 == 0): break
    if (A & mask == B & mask): count += 1
print(count)
print(time.time() - start_time)