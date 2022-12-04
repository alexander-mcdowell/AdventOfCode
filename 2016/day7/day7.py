##########
# PART 1 #
##########

"""
data = open("day7in.txt").read().split("\n")

count = 0
for s in data:
    start_brack, end_brack = [], []
    for i in range(len(s)):
        if (s[i] == '['): start_brack.append(i)
        elif (s[i] == ']'): end_brack.append(i)
        
    valid = False
    for i in range(len(s) - 3):
        t = s[i : i + 4]
        if (t[0] == t[3] and t[1] == t[2] and t[0] != t[1]):
            start, end = None, None
            for j in range(len(start_brack)):
                if (start_brack[j] < i < end_brack[j]):
                    start = start_brack[j]
                    end = end_brack[j]
                    break
            
            if (start == None or end == None): valid = True
            else:
                valid = False
                break
    if (valid): count += 1
print(count)
"""

##########
# PART 2 #
##########

data = open("day7in.txt").read().split("\n")

count = 0
for s in data:
    start_brack, end_brack = [], []
    for i in range(len(s)):
        if (s[i] == '['): start_brack.append(i)
        elif (s[i] == ']'): end_brack.append(i)
        
    valid = False
    aba, bab = [], []
    for i in range(len(s) - 2):
        t = s[i : i + 3]
        if (t[0] == t[2] and t[0] != t[1] and '[' not in t and ']' not in t):
            start, end = None, None
            for j in range(len(start_brack)):
                if (start_brack[j] < i < end_brack[j]):
                    start = start_brack[j]
                    end = end_brack[j]
                    break
            
            # ABA check
            if (start == None or end == None):
                aba.append(t)
                t_prime = t[1] + t[0] + t[1]
                if (t_prime in bab):
                    valid = True
                    break
            # BAB check
            else:
                bab.append(t)
                t_prime = t[1] + t[0] + t[1]
                if (t_prime in aba):
                    valid = True
                    break
    if (valid): count += 1
print(count)