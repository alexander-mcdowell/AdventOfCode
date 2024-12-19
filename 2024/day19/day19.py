import time

# ##########
# # PART 1 #
# ##########

isPossible = set()
def checkPossible(s):
    if (s == ""): return True
    if (s in isPossible): return True
    for t in substrs:
        if (s[:len(t)] == t and checkPossible(s[len(t):])):
            isPossible.add(s)
            return True
    return False

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
substrs = data[0].split(", ")
count = 0
for l in data[2:]:
    s = l
    if (checkPossible(s)): count += 1
print(count)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

counts = {}
def getCounts(s):
    if (s == ""): return 1
    if (s in counts): return counts[s]
    for t in substrs:
        if (s[:len(t)] == t):
            count = getCounts(s[len(t):])
            if (count == 0): continue
            if (s not in counts): counts[s] = count
            else: counts[s] += count
    if (s in counts): return counts[s]
    return 0

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
substrs = data[0].split(", ")
total = 0
for l in data[2:]: total += getCounts(l)
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")