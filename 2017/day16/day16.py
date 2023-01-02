import time

##########
# PART 1 #
##########

# start_time = time.time()
# instructions = open("input.txt").read().split("\n")[0].split(",")
# arr = list('abcdefghijklmnop')
# for inst in instructions:
#     if (inst[0] == 's'):
#         for _ in range(int(inst[1:])): arr.insert(0, arr.pop(-1))
#         continue
#     elif (inst[0] == 'x'):
#         i, j = inst[1:].split("/")
#         i, j = int(i), int(j)
#     else:
#         a, b = inst[1], inst[3]
#         i, j = arr.index(a), arr.index(b)
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
# print("".join(arr))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
instructions = open("input.txt").read().split("\n")[0].split(",")
arr = list('abcdefghijklmnop')
memoize = {}
inst_counter = 0
t = 0
N = 10 ** 9
do_memoize = True
while t < N:
    inst = instructions[inst_counter]
    s = "".join(arr)
    if (do_memoize):
        if ((inst_counter, s) in memoize):
            dt = t - memoize[(inst_counter, s)]
            N = (N - t) % dt
            t = 0
            do_memoize = False
        memoize[(inst_counter, s)] = t
    
    if (inst[0] == 's'):
        for _ in range(int(inst[1:])): arr.insert(0, arr.pop(-1))
        inst_counter = (inst_counter + 1) % len(instructions)
        t += 1
        continue
    elif (inst[0] == 'x'):
        i, j = inst[1:].split("/")
        i, j = int(i), int(j)
    else:
        a, b = inst[1], inst[3]
        i, j = arr.index(a), arr.index(b)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    inst_counter = (inst_counter + 1) % len(instructions)
    t += 1
print("".join(arr))
print(time.time() - start_time)