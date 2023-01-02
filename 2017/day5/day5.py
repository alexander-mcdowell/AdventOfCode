import time

##########
# PART 1 #
##########

# start_time = time.time()
# arr = [int(x) for x in open("input.txt").read().split("\n")]
# i = 0
# steps = 0
# while 0 <= i < len(arr):
#     offset = arr[i]
#     arr[i] += 1
#     i += offset
#     steps += 1
# print(steps)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
arr = [int(x) for x in open("input.txt").read().split("\n")]
i = 0
steps = 0
while 0 <= i < len(arr):
    offset = arr[i]
    if (offset >= 3): arr[i] -= 1
    else: arr[i] += 1
    i += offset
    steps += 1
print(steps)
print(time.time() - start_time)