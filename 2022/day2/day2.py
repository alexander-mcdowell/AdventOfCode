import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", 'r+').read().split("\n")
# total = 0
# for l in lines:
#     op, me = l.split(" ")
#     total += ord(me) - ord('X') + 1
#     if ((op == 'A' and me == 'X') or (op == 'B' and me == 'Y') or (op == 'C' and me == 'Z')): total += 3
#     elif ((op == 'A' and me == 'Y') or (op == 'B' and me == 'Z') or (op == 'C' and me == 'X')): total += 6
# print(total)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", 'r+').read().split("\n")
total = 0
for l in lines:
    op, me = l.split(" ")
    if (me == 'X'):
        if (op == 'A'): total += 3
        elif (op == 'B'): total += 1
        else: total += 2
    elif (me == 'Y'):
        if (op == 'A'): total += 4
        elif (op == 'B'): total += 5
        else: total += 6
    else:
        if (op == 'A'): total += 8
        elif (op == 'B'): total += 9
        else: total += 7
print(total)
print(time.time() - start_time)