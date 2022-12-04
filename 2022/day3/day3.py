import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# total = 0
# for rucksack in lines:
#     pack1, pack2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
#     common = [x for x in set(pack1) if x in pack2][0]
#     if (ord(common) >= ord('a')): total += ord(common) - ord('a') + 1
#     else: total += ord(common) - ord('A') + 27
# print(total)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
total = 0
for i in range(len(lines)//3):
    rucksacks = [x for x in lines[3 * i : 3 * (i + 1)]]
    common = [x for x in set(rucksacks[0]) if x in rucksacks[1]]
    common = [x for x in set(common) if x in rucksacks[2]][0]
    if (ord(common) >= ord('a')): total += ord(common) - ord('a') + 1
    else: total += ord(common) - ord('A') + 27
print(total)
print(time.time() - start_time)