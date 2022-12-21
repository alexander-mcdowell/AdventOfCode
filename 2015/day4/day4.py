##########
# PART 1 #
##########

# import time
# import hashlib

# start_time = time.time()
# secret_word = open("input.txt").read()
# n = 1
# while True:
#     new_word = secret_word + str(n)
#     if (hashlib.md5(new_word.encode()).hexdigest()[:5] == "00000"):
#         print(n)
#         break
#     n += 1
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time
import hashlib

start_time = time.time()
secret_word = open("input.txt").read()
n = 1
while True:
    new_word = secret_word + str(n)
    if (hashlib.md5(new_word.encode()).hexdigest()[:6] == "000000"):
        print(n)
        break
    n += 1
print(time.time() - start_time)