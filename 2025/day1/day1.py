import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
x = 50
count = 0
for l in data:
    x = (x + int(l[1:]) * (-1 if l[0]=="L" else 1)) % 100
    if x==0: count += 1
print(count)
print(time.time() - start_time)

##########
# PART 2 #
##########

import math

start_time = time.time()
x = 50
count = 0
for l in data:
    dx = int(l[1:]) * (-1 if l[0]=="L" else 1)
    if dx>=0: k = (x+dx)//100
    else:
        if x==0: count -= 1
        k = int(math.ceil((abs(dx)-x)/100))
        if ((x+dx)%100 == 0): count += 1
    count += k
    x = (x + dx) % 100
print(count)
print(time.time() - start_time)