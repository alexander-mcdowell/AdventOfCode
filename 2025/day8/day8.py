import timeit
import heapq

##########
# PART 1 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
points = []
disjoint_sets = []
i = 0
for point in data:
    x,y,z = point.split(",")
    points.append((int(x), int(y), int(z)))
    disjoint_sets.append(i)
    i += 1

def find(x):
    if disjoint_sets[x] == x: return x
    y = find(disjoint_sets[x])
    disjoint_sets[x] = y
    return y

pq = []
for i in range(len(data)):
    p1 = points[i]

    for j in range(i + 1, len(data)):
        p2 = points[j]
        d = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        heapq.heappush(pq, (d, [i, j]))

count = 0
for _ in range(len(data)):
    d, pair = heapq.heappop(pq)
    i, j = pair
    i2, j2 = find(i), find(j)
    if i2 != j2:
        disjoint_sets[j] = i2
        disjoint_sets[j2] = i2

groups = {}
for x in range(len(disjoint_sets)):
    y = find(x)
    if y not in groups: groups[y] = 1
    else: groups[y] += 1
rev_groups = {}
for x in groups:
    y = groups[x]
    if y not in rev_groups: rev_groups[y] = 1
    else: rev_groups[y] += 1

prod = 1
for _ in range(3):
    x = max(rev_groups)
    rev_groups.pop(x)
    prod *= x
print(prod)
print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")

# Read in each point and construct the disjoint sets so each point points at itself
points = []
disjoint_sets = []
pq = []
i = 0
for point in data:
    x,y,z = point.split(",")
    p1 = (int(x), int(y), int(z))
    points.append(p1)
    disjoint_sets.append(i)
    
    # Add each pair to the priority queue
    for j in range(len(points)-1):
        p2 = points[j]
        d = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        heapq.heappush(pq, (d, [i, j]))
    
    i += 1

# Helper function to find root
def find(x):
    if disjoint_sets[x] == x: return x
    y = find(disjoint_sets[x])
    disjoint_sets[x] = y
    return y

# Track how many total connected components there are and use union-find to check
# if we should/should not add an edge. If we do, reduce the connected component count
connected_components = len(points)
while len(pq) != 0:
    d, pair = heapq.heappop(pq)
    i, j = pair
    i2, j2 = find(i), find(j)
    if i2 != j2:
        disjoint_sets[j] = i2
        disjoint_sets[j2] = i2
        connected_components -= 1

    if connected_components==1:
        print(points[i][0] * points[j][0])
        break

print(timeit.default_timer() - start_time)