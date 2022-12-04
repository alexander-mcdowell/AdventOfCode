import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# count = 0
# for line in lines:
#     pair1, pair2 = line.split(",")
#     pl1, pu1 = [int(x) for x in pair1.split("-")]
#     pl2, pu2 = [int(x) for x in pair2.split("-")]
#     if (pl1 >= pl2 and pl1 <= pu2 and pu1 >= pl2 and pu1 <= pu2): count += 1
#     elif (pl2 >= pl1 and pl2 <= pu1 and pu2 >= pl1 and pu2 <= pu1): count += 1
# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
count = 0
for line in lines:
    pair1, pair2 = line.split(",")
    pl1, pu1 = [int(x) for x in pair1.split("-")]
    pl2, pu2 = [int(x) for x in pair2.split("-")]
    if (pl1 >= pl2 and pl1 <= pu2): count += 1
    elif (pl2 >= pl1 and pl2 <= pu1): count += 1
print(count)
print(time.time() - start_time)