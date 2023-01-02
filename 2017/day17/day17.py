import time

##########
# PART 1 #
##########

# start_time = time.time()
# steps = int(open("input.txt").read().split("\n")[0])
# arr = [0]
# i = 0
# for x in range(1, 2018):
#     i = (i + steps) % len(arr)
#     arr.insert(i + 1, x)
#     i += 1
# print(arr[(i + 1) % len(arr)])
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
steps = int(open("input.txt").read().split("\n")[0])
arr = [0]
i = 0
at_one = None
length = 1
for x in range(1, 50000001):
    i = (i + steps) % length
    i += 1
    if (i == 1): at_one = x
    length += 1
print(at_one)
print(time.time() - start_time)