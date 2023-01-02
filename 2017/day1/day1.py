import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# for line in lines:
#     digit_sum = 0
#     for i in range(len(line)):
#         if (line[i] == line[(i + 1) % len(line)]): digit_sum += int(line[i])
#     print(digit_sum)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
for line in lines:
    digit_sum = 0
    n = len(line)
    for i in range(n):
        if (line[i] == line[(i + n//2) % n]): digit_sum += int(line[i])
    print(digit_sum)
print(time.time() - start_time)