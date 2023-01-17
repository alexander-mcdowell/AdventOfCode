##########
# PART 1 #
##########

# import time
# import hashlib

# start_time = time.time()
# key = open("input.txt").read().split("\n")[0]
# n = 1
# s = ""
# while True:
#     hash = hashlib.md5((key + str(n)).encode()).hexdigest()
#     if (hash[:5] == '00000'):
#         s += hash[5]
#         if (len(s) == 8): break
#     n += 1
# print(s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time
import hashlib

start_time = time.time()
key = open("input.txt").read().split("\n")[0]
n = 1
s = ['' for _ in range(8)]
while True:
    hash = hashlib.md5((key + str(n)).encode()).hexdigest()
    if (hash[:5] == '00000'):
        if (not (ord('0') <= ord(hash[5]) <= ord('7'))):
            n += 1
            continue
        if (s[int(hash[5])] != ''):
            n += 1
            continue
        s[int(hash[5])] = hash[6]
        print(s)
        if ('' not in s): break
    n += 1
print("".join(s))
print(time.time() - start_time)