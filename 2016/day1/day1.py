##########
# PART 1 #
##########

"""
data = open("day1in.txt").read().split(", ")
x, y, orient = 0, 0, 0
for action in data:
    d = action[0]
    val = int(action[1:])
    
    if (d == 'L'): orient = (orient + 1) % 4
    else:
        if (orient == 0): orient = 3
        else: orient -= 1

    if (orient == 0): y -= val
    elif (orient == 1): x -= val
    elif (orient == 2): y += val
    else: x += val
print(abs(x) + abs(y))
"""

##########
# PART 2 #
##########

# There is likely a more efficient way that uses intersecting line segments
# but that seems like a hassle.

data = open("day1in.txt").read().split(", ")
x, y, orient = 0, 0, 0
visited = []
end = False
for action in data:
    d = action[0]
    val = int(action[1:])
    
    if (d == 'L'): orient = (orient + 1) % 4
    else:
        if (orient == 0): orient = 3
        else: orient -= 1

    for _ in range(val):
        if (orient == 0): y -= 1
        elif (orient == 1): x -= 1
        elif (orient == 2): y += 1
        else: x += 1
        
        if ((x, y) in visited):
            print(abs(x) + abs(y))
            end = True
            break
        visited.append((x, y))
    if (end): break