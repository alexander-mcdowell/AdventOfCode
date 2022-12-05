import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# i_max = 0
# while True:
#     if (lines[i_max][1] == "1"):
#         n = max([int(x) for x in lines[i_max].split(" ") if x != ''])
#         break
#     i_max += 1
# stacks = [[] for _ in range(n)]
# for i in range(i_max):
#     k = 0
#     for j in range(len(lines[i])//4):
#         crate = lines[i][4 * j + 1 : 4 * (j + 1) - 2]
#         if (crate != ' '): stacks[k].append(crate)
#         k += 1
# for i in range(i_max + 2, len(lines)):
#     inst = lines[i].split(" ")
#     count, src, dest = int(inst[1]), int(inst[3]), int(inst[5])
#     for _ in range(count):
#         stacks[dest - 1].insert(0, stacks[src - 1].pop(0))
# s = ""
# for stack in stacks: s += stack[0]
# print(s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
i_max = 0
while True:
    if (lines[i_max][1] == "1"):
        n = max([int(x) for x in lines[i_max].split(" ") if x != ''])
        break
    i_max += 1
stacks = [[] for _ in range(n)]
for i in range(i_max):
    k = 0
    for j in range(len(lines[i])//4):
        crate = lines[i][4 * j + 1 : 4 * (j + 1) - 2]
        if (crate != ' '): stacks[k].append(crate)
        k += 1
for i in range(i_max + 2, len(lines)):
    inst = lines[i].split(" ")
    count, src, dest = int(inst[1]), int(inst[3]), int(inst[5])
    to_append = stacks[src - 1][:count]
    stacks[src - 1] = stacks[src - 1][count:]
    stacks[dest - 1] = to_append + stacks[dest - 1]
s = ""
for stack in stacks: s += stack[0]
print(s)
print(time.time() - start_time)