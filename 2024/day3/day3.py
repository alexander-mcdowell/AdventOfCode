import time
import re

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
p = re.compile("(?<=mul\()(\d+,\d+)(?=\))")
for l in data:
    s = p.findall(l)
    for s2 in s:
        arr = [int(x) for x in s2.split(",")]
        total += arr[0] * arr[1]
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
p = re.compile("(?<=mul\()(\d+,\d+)(?=\))|(don't\(\))|(do\(\))")
should_multiply = True
for l in data:
    for x in p.findall(l):
        s1, s2, s3 = x
        if (s1 != "" and should_multiply):
            arr = [int(y) for y in s1.split(",")]
            total += arr[0] * arr[1]
        if (s2 != ""): should_multiply = False
        elif (s3 != ""): should_multiply = True
    
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()