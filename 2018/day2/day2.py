import time

##########
# PART 1 #
##########

# start_time = time.time()
# ids = open("input.txt").read().split("\n")
# two_count, three_count = 0, 0
# for id in ids:
#     two_flag, three_flag = False, False
#     for c in set(id):
#         num = id.count(c)
#         if (not two_flag and num == 2):
#             two_count += 1
#             two_flag = True
#         elif (not three_flag and num == 3):
#             three_count += 1
#             three_flag = True
# print(two_count * three_count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
ids = open("input.txt").read().split("\n")
end = False
for i in range(len(ids) - 1):
    if (end): break
    for j in range(i + 1, len(ids)):
        count = 0
        common = []
        for k in range(len(ids[i])):
            if (ids[i][k] != ids[j][k]):
                count += 1
                if (count == 2): break
            else: common.append(ids[i][k])
        if (count == 1):
            print("".join(common))
            end = True
            break
print(time.time() - start_time)