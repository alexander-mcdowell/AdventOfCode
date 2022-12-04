##########
# PART 1 #
##########

"""
nums = sorted([int(x) for x in open("day24in.txt").read().split("\n")])
target = sum(nums) // 3

def get_groups(target, nums, i_start = 0):
    if (target < 0): return None
    if (target == 0): return []

    groups = []
    for i in range(i_start, len(nums)):
        x = nums[i]
        subgroups = get_groups(target - x, nums, i + 1)
        if (subgroups != None):
            if (subgroups == []): groups.append([x])
            else:
                for y in subgroups: groups.append([x] + y)
    if (groups == []): return None
    else: return groups

total_groups = []
group_dict = {}
for group in get_groups(target, nums):
    size = len(group)
    if (size not in group_dict): group_dict[size] = []
    group_dict[size].append(group)
    total_groups.append(group)
min_size = min(group_dict)

best_size, best_entanglement = 10000000, 10000000
for size in range(min_size, max(group_dict) + 1):
    for i in range(len(group_dict[min_size])):
        group1 = group_dict[min_size][i]

        entanglement = 1
        nums_copy = [x for x in nums]
        for x in group1:
            entanglement *= x
            nums_copy.remove(x)

        if (sum(nums_copy) == 2 * target):
            if (len(group1) < best_size or (len(group1) == best_size and entanglement < best_entanglement)):
                best_size = len(group1)
                best_entanglement = entanglement

    if (best_size != 10000000): break

print(best_entanglement)
"""

##########
# PART 1 #
##########

nums = sorted([int(x) for x in open("day24in.txt").read().split("\n")])
target = sum(nums) // 4

def get_groups(target, nums, i_start = 0):
    if (target < 0): return None
    if (target == 0): return []

    groups = []
    for i in range(i_start, len(nums)):
        x = nums[i]
        subgroups = get_groups(target - x, nums, i + 1)
        if (subgroups != None):
            if (subgroups == []): groups.append([x])
            else:
                for y in subgroups: groups.append([x] + y)
    if (groups == []): return None
    else: return groups

total_groups = []
group_dict = {}
for group in get_groups(target, nums):
    size = len(group)
    if (size not in group_dict): group_dict[size] = []
    group_dict[size].append(group)
    total_groups.append(group)
min_size = min(group_dict)

best_size, best_entanglement = 10000000, 10000000
for size in range(min_size, max(group_dict) + 1):
    for i in range(len(group_dict[min_size])):
        group1 = group_dict[min_size][i]

        entanglement = 1
        nums_copy = [x for x in nums]
        for x in group1:
            entanglement *= x
            nums_copy.remove(x)

        if (sum(nums_copy) == 3 * target):
            if (len(group1) < best_size or (len(group1) == best_size and entanglement < best_entanglement)):
                best_size = len(group1)
                best_entanglement = entanglement

    if (best_size != 10000000): break

print(best_entanglement)