import time

##########
# PART 1 #
##########

# start_time = time.time()
# instructions = open("input.txt").read().split("\n")[0].split(',')
# q, r = 0, 0
# for inst in instructions:
#     if (inst == "n"):
#         q -= 1
#     elif (inst == "ne"):
#         r -= 1
#     elif (inst == "se"):
#         q += 1
#         r -= 1
#     elif (inst == "s"):
#         q += 1
#     elif (inst == "sw"):
#         r += 1
#     else:
#         q -= 1
#         r += 1

# if ((q < 0 and r >= 0) or (q >= 0 and r < 0)):
#     if (abs(q) >= abs(r)): q += r
#     else: r += q
# print(abs(q) + abs(r))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
instructions = open("input.txt").read().split("\n")[0].split(',')
q, r = 0, 0
best = 0
for inst in instructions:
    if (inst == "n"):
        q -= 1
    elif (inst == "ne"):
        r -= 1
    elif (inst == "se"):
        q += 1
        r -= 1
    elif (inst == "s"):
        q += 1
    elif (inst == "sw"):
        r += 1
    else:
        q -= 1
        r += 1

    q2, r2 = q, r
    if ((q2 < 0 and r2 >= 0) or (q2 >= 0 and r2 < 0)):
        if (abs(q2) >= abs(r2)): q2 += r2
        else: r2 += q2
    dist = abs(q2) + abs(r2)
    if (dist > best): best = dist
print(best)
print(time.time() - start_time)