##########
# PART 1 #
##########

"""
data = open("day3in.txt").read().split("\n")[0]
houses = {}
pos = (0, 0)
i = 0
while (True):
    try:
        houses[pos]
    except Exception as _:
        houses[pos] = None
    
    if (i == len(data)): break
    c = data[i]
    if (c == "^"): pos = (pos[0] - 1, pos[1])
    elif (c == "v"): pos = (pos[0] + 1, pos[1])
    elif (c == "<"): pos = (pos[0], pos[1] - 1)
    else: pos = (pos[0], pos[1] + 1)
    i += 1

print(len(houses))
"""

##########
# PART 2 #
##########

data = open("day3in.txt").read().split("\n")[0]
houses = [{}, {}]
pos = [(0, 0), (0, 0)]
turn = 0
i = 0
while (True):
    try:
        houses[1 - turn][pos[turn]]
    except Exception as _:
        try:
            houses[turn][pos[turn]]
        except Exception as _:
            houses[turn][pos[turn]] = None
    
    if (i == len(data)): break
    c = data[i]
    if (c == "^"): pos[turn] = (pos[turn][0] - 1, pos[turn][1])
    elif (c == "v"): pos[turn] = (pos[turn][0] + 1, pos[turn][1])
    elif (c == "<"): pos[turn] = (pos[turn][0], pos[turn][1] - 1)
    else: pos[turn] = (pos[turn][0], pos[turn][1] + 1)
    i += 1
    turn = 1 - turn

print(len(houses[0]) + len(houses[1]))