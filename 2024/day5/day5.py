import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
rules = []
mode = True
total = 0
for l in data:
    if (l == ""):
        mode = False
        continue
    if (mode):
        rules.append(tuple([int(x) for x in l.split("|")]))
    else:
        vals = [int(x) for x in l.split(",")]
        orders = []
        for i in range(1, len(vals)):
            for j in range(i):
                x, y = vals[i - 1], vals[i]
                orders.append((x, y))
        valid = True
        for o in orders:
            if (not valid): break
            for r in rules:
                if (r[0] == o[1] and r[1] == o[0]):
                    valid = False
                    break
        if (valid): total += vals[len(vals)//2]
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
rules = set()
mode = True
total = 0
for l in data:
    if (l == ""):
        mode = False
        continue
    if (mode):
        rules.add(tuple([int(x) for x in l.split("|")]))
    else:
        vals = [int(x) for x in l.split(",")]
        i = 1
        incorrect = False
        while i < len(vals):
            valid = True
            for j in range(i):
                if (vals[i], vals[j]) in rules:
                    temp = vals[i]
                    vals[i] = vals[j]
                    vals[j] = temp
                    valid = False
                    incorrect = True
                    break
            if (valid): i += 1
        if (incorrect): total += vals[len(vals)//2]
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()