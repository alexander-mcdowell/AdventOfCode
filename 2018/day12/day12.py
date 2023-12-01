##########
# PART 1 #
##########

import time

start_time = time.time()
lines = open("input.txt").read().split("\n")
N = 20
state = list(lines[0].split(": ")[1])
rules = {}
for line in lines[2:]:
    line = line.split(" => ")
    rules[tuple(line[0])] = line[1]
print(time.time() - start_time)