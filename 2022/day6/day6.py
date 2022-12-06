import time

##########
# PART 1 #
##########

# start_time = time.time()
# line = open("input.txt", "r+").read().split("\n")[0]
# for i in range(len(line) - 4):
#     substr = line[i : i + 4]
#     if (len(set(substr)) == 4):
#         print(i + 3)
#         break
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
line = open("input.txt", "r+").read().split("\n")[0]
for i in range(len(line) - 14):
    substr = line[i : i + 14]
    if (len(set(substr)) == 14):
        print(i + 14)
        break
print(time.time() - start_time)