##########
# PART 1 #
##########

"""
data = open("day6in.txt").read().split("\n")
n = len(data[0])
col_freqs = [{} for _ in range(n)]
for word in data:
    for i in range(n):
        c = word[i]
        if c not in col_freqs[i]: col_freqs[i][c] = 0
        col_freqs[i][c] += 1
s = ""
for i in range(n):
    best, best_c = 0, ""
    for c in col_freqs[i]:
        if (col_freqs[i][c] > best):
            best = col_freqs[i][c]
            best_c = c
    s += best_c
print(s)
"""

##########
# PART 2 #
##########

data = open("day6in.txt").read().split("\n")
n = len(data[0])
col_freqs = [{} for _ in range(n)]
for word in data:
    for i in range(n):
        c = word[i]
        if c not in col_freqs[i]: col_freqs[i][c] = 0
        col_freqs[i][c] += 1
s = ""
for i in range(n):
    best, best_c = 10000000000, ""
    for c in col_freqs[i]:
        if (col_freqs[i][c] < best):
            best = col_freqs[i][c]
            best_c = c
    s += best_c
print(s)