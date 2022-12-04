##########
# PART 1 #
##########

from itertools import permutations

data = open("day17in.txt").read().split("\n")
nums = sorted([int(x) for x in data])

def get_ways(x, n, nums, last_i = -1, way = []):
    global ways
    if (x == n):
        ways.append(way)
        return
    
    for i in range(last_i + 1, len(nums)):
        y = nums[i]
        if (x + y <= n):
            get_ways(x + y, n, nums, i, way + [y])
        else: break
    return

ways = []
get_ways(0, 150, nums)
smallest, total_ways = 10000000000000, []
for x in ways:
    if (len(x) < smallest):
        smallest = len(x)
for x in ways:
    if (len(x) == smallest): total_ways.append(x)
print(len(total_ways))
