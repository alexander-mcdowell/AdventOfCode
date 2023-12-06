import time
import math

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
times = [int(x) for x in data[0].split("Time: ")[1].split(' ') if x != '']
distance = [int(x) for x in data[1].split("Distance: ")[1].split(' ') if x != '']
# x = time held, t = time to beat
# Distance x(t - x)
# Find roots of tx - x^2 + d
# high root - low root + 1 = total number of values
prod = 1
for i in range(len(times)):
    t, d = times[i], distance[i]
    low, high = int(1 + math.floor((t - math.sqrt(t*t - 4*d))/2)), int(math.ceil((t + math.sqrt(t*t - 4*d))/2) - 1)
    prod *= (high - low + 1)
print(prod)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
T = int("".join([x for x in data[0].split("Time: ")[1].split(' ') if x != '']))
D = int("".join([x for x in data[1].split("Distance: ")[1].split(' ') if x != '']))
low, high = int(1 + math.floor((T - math.sqrt(T*T- 4*D))/2)), int(math.ceil((T + math.sqrt(T*T - 4*D))/2) - 1)
print(high - low + 1)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")