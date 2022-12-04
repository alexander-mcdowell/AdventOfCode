##########
# PART 1 #
##########

"""
data = open("day19in.txt").read().split("\n")
rules = {}
for l in data:
    if (l == ""): break
    src, replace = l.split(" => ")
    if (src not in rules): rules[src] = []
    rules[src].append(replace)
s = data[-1]

possible = []
i = 0
while (i < len(s)):
    if (i < len(s) - 1):
        if (ord('Z') >= ord(s[i]) >= ord('A') and ord('z') >= ord(s[i + 1]) >= ord('a')):
            x = s[i : i + 2]
        else: x = s[i]
    else: x = s[i]

    if (x in rules):
        for y in rules[x]:
            t = s[:i] + y + s[i + len(x):]
            if (t not in possible): possible.append(t)
    i += len(x)
print(len(possible))
"""

##########
# PART 2 #
##########

import time

data = open("day19in.txt").read().split("\n")
rules = {}
for l in data:
    if (l == ""): break
    src, replace = l.split(" => ")
    if (src not in rules): rules[src] = []
    rules[src].append(replace)
target = data[-1]

max_replace_len = 0
rules_rev = {}
for k in rules:
    for x in rules[k]:
        rules_rev[x] = k
        if (len(x) > max_replace_len): max_replace_len = len(x)

def reduce(s):
    global rules_rev, target
    if (s == 'e'):
        return 0

    best = 10000000000000000
    for i in range(len(s)):
        if (ord(s[i]) >= ord('a')): continue
        for j in range(max_replace_len, 0, -1):
            if (i + j > len(s)): continue
            x = s[i : i + j]

            if (x in rules_rev):
                t = s[:i] + rules_rev[x] + s[i + j:]
                if (rules_rev[x] == 'e' and len(t) != 1): continue
                counter = reduce(t)
                steps = counter + 1
                if (steps < best): best = steps
    return best

start_time = time.time()
print(reduce(target))
print(time.time() - start_time)