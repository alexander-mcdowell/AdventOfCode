import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", 'r+').read().split("\n")
# max_s = 0
# s = 0
# for l in lines:
#     if (l == ''):
#         if (s > max_s): max_s = s
#         s = 0
#     else:
#         s += int(l)
# print(max_s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", 'r+').read().split("\n")
max_s = []
s = 0
for l in lines:
    if (l == ''):
        max_s.append(s)
        s = 0
    else:
        s += int(l)
print(sum(sorted(max_s)[-3:]))
print(time.time() - start_time)