import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
id_sum = 0
for s in data:
    id, bag = s.split(": ")
    id = int(id.split("Game ")[1])
    flag = True
    for sets in bag.split("; "):
        if (not flag): break
        reds, blues, greens = 0, 0, 0
        cubes = [x.split(", ") for x in sets.split(", ")]
        cubes = [tuple(c[0].split(" ")) for c in cubes]
        cubes = [(int(c[0]), c[1]) for c in cubes]
        for c in cubes:
            if (c[1] == "red"): reds += c[0]
            elif (c[1] == "blue"): blues += c[0]
            else: greens += c[0]
        if (not (reds <= 12 and greens <= 13 and blues <= 14)): flag = False
    if (flag): id_sum += id
print(id_sum)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
power_sum = 0
for s in data:
    id, bag = s.split(": ")
    id = int(id.split("Game ")[1])
    flag = True
    min_red, min_blue, min_green = 0, 0, 0
    for sets in bag.split("; "):
        if (not flag): break
        cubes = [x.split(", ") for x in sets.split(", ")]
        cubes = [tuple(c[0].split(" ")) for c in cubes]
        cubes = [(int(c[0]), c[1]) for c in cubes]
        for c in cubes:
            if (c[1] == "red"):
                if (c[0] > min_red): min_red = c[0]
            elif (c[1] == "blue"):
                if (c[0] > min_blue): min_blue = c[0]
            else:
                if (c[0] > min_green): min_green = c[0]
    power = min_red * min_blue * min_green
    power_sum += power
print(power_sum)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()