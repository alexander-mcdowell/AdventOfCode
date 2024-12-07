import time
from itertools import product

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
for l in data:
    row = [int(x) if x[-1]!=':' else int(x[:-1]) for x in l.split(" ")]
    target, vals = row[0], row[1:]
    for p in product([0, 1], repeat=len(vals)-1):
        val = vals[0]
        if (len(vals)==1):
            if (vals[0] == target): total += target
            break
        i = 0
        for x in vals[1:]:
            # 0 = add, 1 = multiply
            if (p[i]==0): val += x
            else: val *= x
            if (val > target): break
            i += 1
        if (val == target):
            total += target
            break
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

import math

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
for l in data:
    row = [int(x) if x[-1]!=':' else int(x[:-1]) for x in l.split(" ")]
    target, vals = row[0], row[1:]
    for p in product([0, 1, 2], repeat=len(vals)-1):
        val = vals[0]
        if (len(vals)==1):
            if (vals[0] == target): total += target
            break
        i = 0
        for x in vals[1:]:
            # 0 = add, 1 = multiply, 2 = concatenation
            if (p[i]==0): val += x
            elif (p[i] ==  1): val *= x
            else:
                length = int(math.log10(x)) + 1
                val = val * pow(10, length) + x
            if (val > target): break
            i += 1
        if (val == target):
            total += target
            break
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()