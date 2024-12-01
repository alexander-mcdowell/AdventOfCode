import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
list1 = []
list2 = []
for l in data:
    x, y = l.split("   ")
    x, y = int(x), int(y)
    list1.append(x)
    list2.append(y)
list1 = sorted(list1)
list2 = sorted(list2)
dist = 0
for i in range(len(list1)):
    dist += abs(list2[i] - list1[i])
print(dist)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
list1 = []
list2 = []
for l in data:
    x, y = l.split("   ")
    x, y = int(x), int(y)
    list1.append(x)
    list2.append(y)
list1 = sorted(list1)
list2 = sorted(list2)
dist = 0
for i in range(len(list1)):
    dist += list2.count(list1[i]) * list1[i]
print(dist)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()