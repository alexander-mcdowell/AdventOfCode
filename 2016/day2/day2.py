##########
# PART 1 #
##########

"""
import math

data = open("day2in.txt").read().split("\n")
num = 5
s = ""
for line in data:
    for c in line:
        if (c == 'U'):
            if (num > 3): num -= 3
        elif (c == 'D'):
            if (num < 7): num += 3
        elif (c == 'L'): num = max(num - 1, 3 * (math.ceil(num / 3) - 1) + 1)
        else: num = min(num + 1, int(3 * math.ceil(num / 3)))
    s += str(num)
print(s)
"""

##########
# PART 2 #
##########

import math

data = open("day2in.txt").read().split("\n")
pos = (-2, 0)
pos_map = {(-2, 0): '5', (-1, 0): '6', (0, 0): '7', (1, 0): '8', (2, 0): '9',
           (-1, 1): '2', (0, 1): '3', (1, 1): '4', (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C',
           (0, 2): '1', (0, -2): 'D'}
s = ""
for line in data:
    for c in line:
        if (c == 'U'): new_pos = (pos[0], pos[1] + 1)
        elif (c == 'D'): new_pos = (pos[0], pos[1] - 1)
        elif (c == 'L'): new_pos = (pos[0] - 1, pos[1])
        else: new_pos = (pos[0] + 1, pos[1])

        if (new_pos in pos_map): pos = new_pos
    s += str(pos_map[pos])
print(s)