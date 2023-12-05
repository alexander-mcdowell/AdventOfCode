import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
seeds = [int(x) for x in data[0][7:].split(" ")]
maps = [[] for _ in range(7)]
i = 2
mode = None
while i < len(data):
    line = data[i]
    if (line == ""):
        i += 1
        mode = None
        continue
    if (mode == None):
        if (line[:4] == "seed"): mode = 0
        elif (line[:4] == "soil"): mode = 1
        elif (line[:4] == "fert"): mode = 2
        elif (line[:4] == "wate"): mode = 3
        elif (line[:4] == "ligh"): mode = 4
        elif (line[:4] == "temp"): mode = 5
        else: mode = 6
    else:
        dest, source, length = [int(x) for x in line.split(" ")]
        i1, i2 = (source, source + length - 1), (dest, dest + length - 1)
        maps[mode].append((i1, i2))
    i += 1
min_val = -1
vals = []
for s in seeds:
    vals.append(s)
    for i in range(7):
        x = vals[-1]
        for pair in maps[i]:
            i1, i2 = pair
            if (i1[0] <= x <= i1[1]):
                x = x - i1[0] + i2[0]
                break
        vals.append(x)

    if (min_val == -1): min_val = vals[-1]
    elif (vals[-1] < min_val): min_val = vals[-1]
print(min_val)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
seeds = [int(x) for x in data[0][7:].split(" ")]
maps = [[] for _ in range(7)]
i = 2
mode = None
while i < len(data):
    line = data[i]
    if (line == ""):
        i += 1
        mode = None
        continue
    if (mode == None):
        if (line[:4] == "seed"): mode = 0
        elif (line[:4] == "soil"): mode = 1
        elif (line[:4] == "fert"): mode = 2
        elif (line[:4] == "wate"): mode = 3
        elif (line[:4] == "ligh"): mode = 4
        elif (line[:4] == "temp"): mode = 5
        else: mode = 6
    else:
        dest, source, length = [int(x) for x in line.split(" ")]
        i1, i2 = (source, source + length - 1), (dest, dest + length - 1)
        maps[mode].append((i1, i2))
    i += 1

def helper(mode, interval, maps):
    # No two mappings may overlap, so once a mapping is succesful, that interval cannot be remapped.
    if (mode == 7): return min(interval)
    min_val = -1
    intervals = [(interval[0], interval[1])]
    while len(intervals) != 0:
        interval = intervals.pop(0)
        found = False
        for pair in maps[mode]:
            # src interval, dest interval
            i1, i2 = pair
            
            # Source interval outside of input interval ---> Interval is unchanged.
            if (i1[1] < interval[0] or i1[0] > interval[1]): continue
            
            # Source interval contains input interval ---> Change entire interval.
            elif (i1[0] <= interval[0] and interval[1] <= i1[1]):
                val = helper(mode + 1, (interval[0] - i1[0] + i2[0], interval[1] - i1[0] + i2[0]), maps)
                if  (val == -1): continue
                elif (min_val == -1 or val < min_val): min_val = val
                found = True
                break
                
            # Break up input interval into changed (1) and unchanged (0) intervals.
            else:
                intervals2 = [(0, interval[0], i1[0] - 1), (1, i1[0], i1[1]), (0, i1[1] + 1, interval[1])]
                to_add = []
                for x in intervals2:
                    x = (x[0], max(interval[0], x[1]), min(interval[1], x[2]))
                    if (x[1] <= x[2]):
                        # Change
                        if (x[0] == 1):
                            val = helper(mode + 1, (x[1] - i1[0] + i2[0], x[2] - i1[0] + i2[0]), maps)
                            if  (val == -1): continue
                            elif (min_val == -1 or val < min_val): min_val = val
                        # Don't change
                        else: to_add.append((x[1], x[2]))
                for x in to_add: intervals.append(x)
                found = True
                break

        # What is left is unchanged
        if not found:
            val = helper(mode + 1, interval, maps)
            if  (val == -1): continue
            elif (min_val == -1 or val < min_val): min_val = val
    return min_val

global_min_val = -1
for i in range(len(seeds)//2):
    val = helper(0, (seeds[2 * i], seeds[2*i] + seeds[2 * i + 1] - 1), maps)
    if (global_min_val == -1 or val < global_min_val): global_min_val = val
print(global_min_val)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()