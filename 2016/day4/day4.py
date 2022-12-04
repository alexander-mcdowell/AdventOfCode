##########
# PART 1 #
##########

"""
data = open("day4in.txt").read().split("\n")
sector_ids = 0
for line in data:
    line = line.split('[')
    s = line[0]
    checksum = line[1][:-1]
    
    counts = {}
    for c in set(s):
        if (c == '-' or ord('9') >= ord(c) >= ord('0')): continue
        count = s.count(c)
        if (count not in counts): counts[count] = []
        counts[count].append(c)
    for x in counts: counts[x] = sorted(counts[x])
    proposed = ""
    key_set = sorted(counts)
    x = 0
    while (x < 5):
        arr = counts[key_set.pop(-1)]
        while (len(arr) != 0 and x < 5):
            proposed += arr.pop(0)
            x += 1

    if (proposed == checksum):
        id = int(s.split("-")[-1])
        sector_ids += id
print(sector_ids)
"""

##########
# PART 2 #
##########

data = open("day4in.txt").read().split("\n")
for line in data:
    line = line.split('[')
    s = line[0]
    checksum = line[1][:-1]
    
    counts = {}
    for c in set(s):
        if (c == '-' or ord('9') >= ord(c) >= ord('0')): continue
        count = s.count(c)
        if (count not in counts): counts[count] = []
        counts[count].append(c)
    for x in counts: counts[x] = sorted(counts[x])
    proposed = ""
    key_set = sorted(counts)
    x = 0
    while (x < 5):
        arr = counts[key_set.pop(-1)]
        while (len(arr) != 0 and x < 5):
            proposed += arr.pop(0)
            x += 1

    if (proposed == checksum):
        decrypted = ""
        s = s.split('-')
        id = int(s[-1])
        
        for i in range(len(s) - 1):
            for c in s[i]:
                decrypted += chr((((ord(c) - ord('a')) + id) % 26) + ord('a'))
            if (i != len(s) - 2): decrypted += ' '
        if (decrypted == "northpole object storage"):
            print(id)
            break