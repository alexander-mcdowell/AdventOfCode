##########
# PART 1 #
##########

"""
data = open("day21in.txt").read().split("\n")
s = list("abcdefgh")
for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "swap"):
        if (inst[1] == "position"):
            i, j = int(inst[2]), int(inst[5])
        else:
            i, j = s.index(inst[2]), s.index(inst[5])
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    elif (inst[0] == "rotate"):
        if (inst[1] == "based"):
            i = s.index(inst[6]) + 1
            if (i >= 5): i += 1
            for _ in range(i): s = [s[-1]] + s[:-1]
        elif (inst[1] == "left"):
            steps = int(inst[2]) % len(s)
            for _ in range(steps): s = s[1:] + [s[0]]
        else:
            steps = int(inst[2]) % len(s)
            for _ in range(steps): s = [s[-1]] + s[:-1]
    elif (inst[0] == "reverse"):
        i, j = int(inst[2]), int(inst[4])
        t = s[i:j + 1]
        s = s[:i] + t[::-1] + s[j + 1:]
    elif (inst[0] == "move"):
        c = s.pop(int(inst[2]))
        s.insert(int(inst[5]), c)
print("".join(s))
"""

##########
# PART 2 #
##########

from itertools import permutations

data = open("day21in.txt").read().split("\n")
s = list("abcdefgh")
target = "fbgdceah"
for p in permutations(s, len(s)):
    s = list(p)
    for inst in data:
        inst = inst.split(" ")
        if (inst[0] == "swap"):
            if (inst[1] == "position"):
                i, j = int(inst[2]), int(inst[5])
            else:
                i, j = s.index(inst[2]), s.index(inst[5])
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        elif (inst[0] == "rotate"):
            if (inst[1] == "based"):
                i = s.index(inst[6]) + 1
                if (i >= 5): i += 1
                for _ in range(i): s = [s[-1]] + s[:-1]
            elif (inst[1] == "left"):
                steps = int(inst[2]) % len(s)
                for _ in range(steps): s = s[1:] + [s[0]]
            else:
                steps = int(inst[2]) % len(s)
                for _ in range(steps): s = [s[-1]] + s[:-1]
        elif (inst[0] == "reverse"):
            i, j = int(inst[2]), int(inst[4])
            t = s[i:j + 1]
            s = s[:i] + t[::-1] + s[j + 1:]
        elif (inst[0] == "move"):
            c = s.pop(int(inst[2]))
            s.insert(int(inst[5]), c)
    if ("".join(s) == target):
        print("".join(p))
        break