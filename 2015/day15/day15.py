#########
# DAY 1 #
#########

"""
# I would love to do Lagrange Multipliers for this but I did it the dumb brute-force easy way.

data = open("day15in.txt").read().split("\n")
flavors = []
for flavor in data:
    flavor = flavor.split(" ")
    flavors.append([int(flavor[i].replace(",", "")) for i in range(2, 12, 2)])
    
amounts = [100] + (len(flavors) - 1) * [0]

best = 0
while True:
    score = 1
    # Ignore calories
    for j in range(len(flavors[0]) - 1):
        x = 0
        for i in range(len(flavors)): x += flavors[i][j] * amounts[i]
        x = max(0, x)
        score *= x
    
    if (score > best): best = score
    
    end = True
    for i in range(len(amounts) - 1, 0, -1):
        amounts[i] += 1
        amounts[0] -= 1
        if (amounts[0] < 0):
            amounts[i] = 0
            amounts[0] = 0
            amounts[0] = 100 - sum(amounts)
        else:
            end = False
            break
    if (end): break

print(best)
"""

##########
# PART 2 #
##########

data = open("day15in.txt").read().split("\n")
flavors = []
for flavor in data:
    flavor = flavor.split(" ")
    flavors.append([int(flavor[i].replace(",", "")) for i in range(2, 12, 2)])
    
amounts = [100] + (len(flavors) - 1) * [0]

best = 0
while True:
    score = 1
    # Ignore calories
    for j in range(len(flavors[0]) - 1):
        x = 0
        for i in range(len(flavors)): x += flavors[i][j] * amounts[i]
        x = max(0, x)
        score *= x
    calories = 0
    for i in range(len(flavors)): calories += flavors[i][len(flavors[0]) - 1] * amounts[i]
    
    if (calories == 500 and score > best): best = score
    
    end = True
    for i in range(len(amounts) - 1, 0, -1):
        amounts[i] += 1
        amounts[0] -= 1
        if (amounts[0] < 0):
            amounts[i] = 0
            amounts[0] = 0
            amounts[0] = 100 - sum(amounts)
        else:
            end = False
            break
    if (end): break

print(best)