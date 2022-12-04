##########
# PART 1 #
##########

"""
from itertools import permutations

data = open("day13in.txt").read().split("\n")
val_map = {}
people = []
for seating in data:
    seating = seating.split(" ")
    person1, person2, value = seating[0], seating[-1][:-1], int(seating[3])
    if (seating[2] == "lose"): value *= -1
    if (person1 not in people): people.append(person1)
    val_map[person1 + person2] = value

best = 0
# There are repeats but its fine
for p in permutations(people, r = len(people)):
    total = 0
    for i in range(len(p)):
        j = (i + 1) % len(p)
        total += val_map[p[i] + p[j]] + val_map[p[j] + p[i]]
    if (total > best): best = total
print(best)
"""

##########
# PART 2 #
##########

from itertools import permutations

data = open("day13in.txt").read().split("\n")
val_map = {}
people = []
for seating in data:
    seating = seating.split(" ")
    person1, person2, value = seating[0], seating[-1][:-1], int(seating[3])
    if (seating[2] == "lose"): value *= -1
    if (person1 not in people): people.append(person1)
    val_map[person1 + person2] = value
for person in people:
    val_map[person + "Me"] = 0
    val_map["Me" + person] = 0
people.append("Me")

best = 0
for p in permutations(people, r = len(people)):
    total = 0
    for i in range(len(p)):
        j = (i + 1) % len(p)
        total += val_map[p[i] + p[j]] + val_map[p[j] + p[i]]
    if (total > best): best = total
print(best)