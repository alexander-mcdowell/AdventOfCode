import time

##########
# PART 1 #
##########

# def to_list(s):
#     if (s == "[]"): return []
#     if (s[0] != "["): return int(s)
#     arr = []
#     t = ""
#     depth = 0
#     for i in range(1, len(s) - 1):
#         if (s[i] == "," and depth == 0):
#             arr.append(to_list(t))
#             t = ""
#         else:
#             if (s[i] == "["): depth += 1
#             elif (s[i] == "]"): depth -= 1
#             t += s[i]
#     if (t != ""): arr.append(to_list(t))
#     return arr

# def compare(a, b):
#     if (type(a) == int and type(b) == int):
#         if (a == b): return None
#         return a < b
#     if (type(a) == int): a = [a]
#     elif (type(b) == int): b = [b]
#     i = 0
#     while i != len(a) and i != len(b):
#         val = compare(a[i], b[i])
#         if (val != None): return val
#         i += 1
#     if (len(a) == len(b)): return None
#     return len(a) < len(b)

# start_time = time.time()
# pairs = open("input.txt", "r+").read().split("\n\n")
# indices_sum = 0
# i = 1
# for pair in pairs:
#     first, second = pair.split("\n")
#     first, second = to_list(first), to_list(second)
#     if (compare(first, second)):
#         indices_sum += i
#     i += 1
# print(indices_sum)
# print(time.time() - start_time)

##########
# PART 2 #
##########

def to_list(s):
    if (s == "[]"): return []
    if (s[0] != "["): return int(s)
    arr = []
    t = ""
    depth = 0
    for i in range(1, len(s) - 1):
        if (s[i] == "," and depth == 0):
            arr.append(to_list(t))
            t = ""
        else:
            if (s[i] == "["): depth += 1
            elif (s[i] == "]"): depth -= 1
            t += s[i]
    if (t != ""): arr.append(to_list(t))
    return arr

def compare(a, b):
    if (type(a) == int and type(b) == int):
        if (a == b): return None
        return a < b
    if (type(a) == int): a = [a]
    elif (type(b) == int): b = [b]
    i = 0
    while i != len(a) and i != len(b):
        val = compare(a[i], b[i])
        if (val != None): return val
        i += 1
    if (len(a) == len(b)): return None
    return len(a) < len(b)

start_time = time.time()
pairs = open("input.txt", "r+").read().split("\n\n")
indices_sum = 0
packets = [[[2]], [[6]]]
# Comparison sort I guess. Yucky O(n^2)
for pair in pairs:
    first, second = pair.split("\n")
    first, second = to_list(first), to_list(second)
    if (len(packets) == 0):
        if (compare(first, second)): packets.append(first)
        else: packets.append(second)
    else:
        for p in [first, second]:
            for i in range(len(packets)):
                if (compare(p, packets[i])):
                    packets.insert(i, p)
                    break
            packets.append(p)
index1, index2 = None, None
for i in range(len(packets)):
    if (packets[i] == [[2]]): index1 = i + 1
    elif (packets[i] == [[6]]): index2 = i + 1
    if (index1 != None and index2 != None):
        print(index1 * index2)
        break
print(time.time() - start_time)