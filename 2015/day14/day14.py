##########
# PART 1 #
##########

"""
data = open("day14in.txt").read().split("\n")
reindeer = []
for x in data:
    x = x.split(" ")
    reindeer.append((x[0], int(x[3]), int(x[6]), int(x[-2])))

T = 2503
t = 0
flying_timer, rest_timer, positions = [], [], []
for i in range(len(reindeer)):
    flying_timer.append(reindeer[i][2])
    rest_timer.append(0)
    positions.append(0)

while (t < T):
    for i in range(len(reindeer)):
        if (flying_timer[i] != 0):
            positions[i] += reindeer[i][1]
            flying_timer[i] -= 1
            if (flying_timer[i] == 0): rest_timer[i] = reindeer[i][-1]
        else:
            rest_timer[i] -= 1
            if (rest_timer[i] == 0): flying_timer[i] = reindeer[i][2]
    t += 1
print(max(positions))
"""

##########
# PART 2 #
##########

data = open("day14in.txt").read().split("\n")
reindeer = []
for x in data:
    x = x.split(" ")
    reindeer.append((x[0], int(x[3]), int(x[6]), int(x[-2])))

T = 2503
t = 0
flying_timer, rest_timer, positions, points = [], [], [], []
for i in range(len(reindeer)):
    flying_timer.append(reindeer[i][2])
    rest_timer.append(0)
    positions.append(0)
    points.append(0)

while (t < T):
    for i in range(len(reindeer)):
        if (flying_timer[i] != 0):
            positions[i] += reindeer[i][1]
            flying_timer[i] -= 1
            if (flying_timer[i] == 0): rest_timer[i] = reindeer[i][-1]
        else:
            rest_timer[i] -= 1
            if (rest_timer[i] == 0): flying_timer[i] = reindeer[i][2]

    # Award a point to the reindeer in first
    best, best_i = 0, []
    for i in range(len(reindeer)):
        if (positions[i] > best):
            best = positions[i]
            best_i = [i]
        elif (positions[i] == best): best_i.append(i)
    for i in best_i: points[i] += 1

    t += 1
print(max(points))