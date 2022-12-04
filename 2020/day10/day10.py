##########
# PART 1 #
##########

"""
data = open("day10in.txt").read().split("\n")
joltages = sorted([int(x) for x in data])
current = 0
rating = joltages[-1]
i = 0
# Always at least one difference of 3
count1, count3 = 0, 1
while (current != rating and i != len(joltages)):
    diff = joltages[i] - current
    if (diff == 1):
        current += 1
        count1 += 1
    elif (diff == 3):
        current += 3
        count3 += 1
    i += 1
print(count1 * count3)
"""

##########
# PART 2 #
##########

data = open("day10in.txt").read().split("\n")
joltages = sorted([int(x) for x in data])
joltage_map = {0: 1}
queue = [0]
while (len(queue) != 0):
    current = queue.pop(0)
    for k in [1, 2, 3]:
        next = k + current
        if (next in joltages):
            if (next not in joltage_map): joltage_map[next] = 0
            joltage_map[next] += joltage_map[current]
            if (next not in queue): queue.append(next)
print(joltage_map[joltages[-1]])