import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# S = 0
# for line in lines:
#     line = line.replace(" ", "\t")
#     nums = [int(x) for x in line.split("\t")]
#     S += max(nums) - min(nums)
# print(S)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
S = 0
for line in lines:
    line = line.replace(" ", "\t")
    nums = [int(x) for x in line.split("\t")]
    end = False
    for i in range(len(nums)):
        if (end): break
        for j in range(i + 1, len(nums)):
            a, b = min(nums[i], nums[j]), max(nums[i], nums[j])
            if (b % a == 0):
                S += b//a
                break
print(S)
print(time.time() - start_time)