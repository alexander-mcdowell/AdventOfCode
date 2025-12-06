import timeit

##########
# PART 1 #
##########

start_time = timeit.timeit()
f = open("input.txt", 'r')
data = f.read().split("\n")
ranges = []
queries = False
fresh = 0
for l in data:
    if queries:
        x = int(l)
        for range in ranges:
            if range[0] <= x <= range[1]:
                fresh += 1
                break
    else:
        if l=="":
            ranges = sorted(ranges, key=lambda x: x[0])
            queries = True
        else: ranges.append([int(x) for x in l.split("-")])
print("Part 1", fresh)
print(timeit.time() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
ranges = []
queries = False
fresh = 0
for l in data:
    if l=="":
        break
    else: ranges.append([int(x) for x in l.split("-")])

fresh = 0
prev = None
ranges = sorted(ranges, key=lambda x: x[0])
for i in range(len(ranges)):
    interval = ranges[i]
    # Add first interval
    if prev==None:
        fresh += interval[1]-interval[0]+1
        prev = interval
    else:
        # Interval is completely contained in previous, do not add it
        if prev[0] <= interval[0] <= prev[1] and prev[0] <= interval[1] <= prev[1]:
            continue
        # Lower part of interval is contained in previous
        elif prev[0] <= interval[0] <= prev[1]:
            fresh += interval[1] - max(interval[0], prev[1]+1) + 1
        # Disjoint intervals
        else:
            fresh += interval[1]-interval[0]+1
        prev = [prev[0], interval[1]]

print("Part 2:", fresh)
print(timeit.default_timer() - start_time)