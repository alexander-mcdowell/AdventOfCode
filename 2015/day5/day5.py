##########
# PART 1 #
##########

"""
data = open("day5in.txt").read().split("\n")
count = 0
for s in data:
    vowels = 0
    double_letter = False
    contains = True
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]): double_letter = True
        if (s[i : i + 2] in ["ab", "cd", "pq", "xy"]):
            contains = False
            break
        if (s[i] in "aeiou"): vowels += 1
    if (s[len(s) - 1] in "aeiou"): vowels += 1
    if (contains and double_letter and vowels >= 3): count += 1

print(count)
"""

##########
# PART 2 #
##########

data = open("day5in.txt").read().split("\n")
count = 0
for s in data:
    rule2 = False
    pair_counts = {}
    for i in range(len(s) - 2):
        if (s[i] == s[i + 2]): rule2 = True
        
        if (s[i] == s[i + 1] == s[i + 2]): continue
        if (s[i:i + 2] not in pair_counts): pair_counts[s[i:i + 2]] = 0
        pair_counts[s[i:i + 2]] += 1

    if (not (s[len(s) - 1] == s[len(s) - 2] == s[len(s) - 3])):
        if (s[len(s) - 2:len(s)] not in pair_counts): pair_counts[s[len(s) - 2:len(s)]] = 0
        pair_counts[s[len(s) - 2:len(s)]] += 1
    
    rule1 = False
    for x in pair_counts:
        if (pair_counts[x] >= 2): rule1 = True
    
    if (rule1 and rule2): count += 1
    
print(count)