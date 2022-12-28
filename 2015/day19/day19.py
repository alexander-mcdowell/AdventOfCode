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

start_time = time.time()

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

best = -1
stack = [(target, 0)]
memoize = {}

while len(stack) != 0:
    s, steps = stack.pop(-1)
    if (best != -1 and steps >= best): break
    if (s in memoize):
        steps2 = memoize[s]
        if (steps >= steps2): continue
        memoize[s] = steps2
    else: memoize[s] = steps

    if (s == 'e'):
        if (best == -1 or steps < best):
            best = steps
        continue

    for i in range(len(s)):
        if (ord(s[i]) >= ord('a')): continue
        for j in range(max_replace_len, 0, -1):
            if (i + j > len(s)): continue
            x = s[i : i + j]

            if (x in rules_rev):
                t = s[:i] + rules_rev[x] + s[i + j:]
                if (rules_rev[x] == 'e' and len(t) != 1): continue
                stack.append((t, steps + 1))

print(best)
print(time.time() - start_time)