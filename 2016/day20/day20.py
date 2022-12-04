##########
# PART 1 #
##########

"""
data = open("day20in.txt").read().split("\n")

intervals = {}
lows = {}
for i in range(len(data)):
    low, high = [int(x) for x in data[i].split("-")]
    intervals[i] = (low, high)
    lows[low] = i
intervals = [intervals[lows[x]] for x in sorted(lows)]

lowest = 0
for interval in intervals:
    low, high = interval
    if (high >= lowest >= low): lowest = high + 1
print(lowest)
"""

##########
# PART 2 #
##########

data = open("day20in.txt").read().split("\n")

def remove_interval(source, target):
    for i in range(len(source)):
        x = source[i]
        if (x[0] <= target[0] and target[1] <= x[1]):
            if (target[1] != x[1]): source.insert(i + 1, [target[1] + 1, x[1]])
            if (target[0] != x[0]): source.insert(i + 1, [x[0], target[0] - 1])
            source.pop(i)
            break
        elif (target[0] <= x[0] and x[1] <= target[1]):
            source.pop(i)
            y = [target]
            remove_interval(y, x)
            if (len(y) == 2):
                left_partition, right_partition = y
                remove_interval(source, left_partition)
                remove_interval(source, right_partition)
            else: remove_interval(source, y[0])
            break
        elif (x[0] <= target[0] <= x[1] and x[1] < target[1]):
            left_partition, right_partition = [target[0], x[1]], [x[1] + 1, target[1]]
            remove_interval(source, left_partition)
            remove_interval(source, right_partition)
            break
        elif (x[0] <= target[1] <= x[1] and target[0] < x[0]):
            left_partition, right_partition = [target[0], x[0] - 1], [x[0], target[1]]
            remove_interval(source, left_partition)
            remove_interval(source, right_partition)
            break

valid = [[0, 4294967295]]
for line in data:
    interval = [int(x) for x in line.split('-')]
    remove_interval(valid, interval)
count = 0
for interval in valid:
    count += interval[1] - interval[0] + 1
print(count)