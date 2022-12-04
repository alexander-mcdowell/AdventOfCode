##########
# PART 1 #
##########

"""
s = open("day18in.txt").read().split("\n")[0]

def step(s):
    t = ""
    for i in range(len(s)):
        left, center, right = 0, 0, 0
        if (i > 0): left = (s[i - 1] == '^')
        center = (s[i] == '^')
        if (i < len(s) - 1): right = (s[i + 1] == '^')
        
        # 110, 011, 100, 001 are traps
        if ((left, center, right) in [(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)]): t += '^'
        else: t += '.'
    return t

N = 40
total_safes = 0
for _ in range(N):
    total_safes += s.count('.')
    s = step(s)
print(total_safes)
"""

##########
# PART 2 #
##########

# There appears to be some kind of repeating pattern with the input (lots of triangles of varying size in the grid)
# But a simple brute-force appears to be fast enough.
# Program seems to be a variation of the cellular automaton Rule 110.

s = open("day18in.txt").read().split("\n")[0]

def step(s):
    t = ""
    for i in range(len(s)):
        left, center, right = 0, 0, 0
        if (i > 0): left = (s[i - 1] == '^')
        center = (s[i] == '^')
        if (i < len(s) - 1): right = (s[i + 1] == '^')
        
        # 110, 011, 100, 001 are traps
        if ((left, center, right) in [(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)]): t += '^'
        else: t += '.'
    return t

N = 400000
total_safes = 0
for _ in range(N):
    k = s.count('.')
    total_safes += k
    s = step(s)
print(total_safes)