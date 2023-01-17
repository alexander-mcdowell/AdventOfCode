##########
# PART 1 #
##########

# import time
# import hashlib

# start_time = time.time()
# puzzle_key = open("input.txt").read().split("\n")[0]
# n = 1
# triple_list = []
# end = False
# keys = []
# while not end:
#     hash = hashlib.md5((puzzle_key + str(n)).encode()).hexdigest()
#     added = False
#     for i in range(len(hash) - 2):
#         if (i + 5 <= len(hash) and len(set(hash[i : i + 5])) == 1):
#             j = 0
#             while j != len(triple_list):
#                 if (n <= 1000 + triple_list[j][1] and hash[i] == triple_list[j][0]):
#                     keys.append((triple_list.pop(j)[1], n))
#                     if (len(keys) == 64):
#                         print(sorted(keys)[-1][0])
#                         end = True
#                         break
#                 else: j += 1
#         if (not added and len(set(hash[i : i + 3])) == 1):
#             if ((hash[i], n) not in triple_list):
#                 triple_list.append((hash[i], n))
#                 added = True
#         if (end): break
#     if (end): break
#     i = 0
#     while i != len(triple_list):
#         if (n > 1000 + triple_list[i][1]): triple_list.pop(i)
#         else: i += 1
#     n += 1  
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time
import hashlib

start_time = time.time()
puzzle_key = open("input.txt").read().split("\n")[0]
n = 0
triple_list = []
end = False
keys = []
while not end:
    i = 0
    while i != len(triple_list):
        if (n > 1000 + triple_list[i][1]): triple_list.pop(i)
        else: i += 1

    hash = puzzle_key + str(n)
    for _ in range(2017):
        hash = hashlib.md5(hash.encode()).hexdigest()

    added = False
    for i in range(len(hash) - 2):
        if (i + 5 <= len(hash) and len(set(hash[i : i + 5])) == 1):
            j = 0
            while j != len(triple_list):
                if (triple_list[j][1] < n and hash[i] == triple_list[j][0]):
                    keys.append((triple_list.pop(j)[1], n))
                    if (len(keys) == 75):
                        print(sorted(keys)[63][0])
                        end = True
                        break
                else: j += 1
        if (end): break
        if (not added and len(set(hash[i : i + 3])) == 1):
            triple_list.append((hash[i], n))
            added = True
    if (end): break

    n += 1  
print(time.time() - start_time)
