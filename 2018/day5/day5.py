##########
# PART 1 #
##########

# import time

# start_time = time.time()
# polymer = list(open("input.txt").read().split("\n")[0])
# i = 0
# while (i != len(polymer) - 1):
#     # Reaction
#     if (abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32):
#         polymer.pop(i)
#         polymer.pop(i)
#         i -= 1
#         if (i < 0): i = 0
#     else: i += 1
# print(len(polymer))
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

start_time = time.time()
polymer = open("input.txt").read().split("\n")[0]
char_set = set()
for c in set(polymer):
    if (ord(c) >= ord('a')): char_set.add(c)

shortest = -1
for c in char_set:
    polymer2 = polymer.replace(c, '')
    polymer2 = list(polymer2.replace(chr(ord(c) - 32), ''))

    i = 0
    while (i != len(polymer2) - 1):
        # Reaction
        if (abs(ord(polymer2[i]) - ord(polymer2[i + 1])) == 32):
            polymer2.pop(i)
            polymer2.pop(i)
            i -= 1
            if (i < 0): i = 0
        else: i += 1
    if (shortest == -1 or len(polymer2) < shortest): shortest = len(polymer2)
print(shortest)
print(time.time() - start_time)