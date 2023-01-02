import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# valid = 0
# for line in lines:
#     line = line.split(" ")
#     if (len(set(line)) == len(line)): valid += 1
# print(valid)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
valid = 0
for line in lines:
    line = line.split(" ")
    if (len(set(line)) == len(line)):
        end = False
        for i in range(len(line)):
            if (end): break
            for j in range(i + 1, len(line)):
                counts1 = {c: line[i].count(c) for c in line[i]}
                counts2 = {c: line[j].count(c) for c in line[j]}
                if (counts1 == counts2):
                    end = True
                    break
        if (not end): valid += 1
print(valid)
print(time.time() - start_time)