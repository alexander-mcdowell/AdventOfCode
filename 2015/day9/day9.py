##########
# PART 1 #
##########

"""
data = open("day9in.txt").read().split("\n")
node_map = {}
for route in data:
    route = route.split(" ")
    if (route[0] not in node_map): node_map[route[0]] = []
    if (route[2] not in node_map): node_map[route[2]] = []
    node_map[route[0]].append((route[2], int(route[4])))
    node_map[route[2]].append((route[0], int(route[4])))

def recurse(u, node_map, previous = []):
    if (len(previous) + 1 == len(node_map)): return 0
    best_cost = 10000000000000000000000
    for v, c in node_map[u]:
        if (v not in previous):
            cost = c + recurse(v, node_map, previous + [u])
            if (cost < best_cost): best_cost = cost
    return best_cost

best_distance = 10000000000000000000000
for start in node_map:
    dist = recurse(start, node_map)
    if (dist < best_distance): best_distance = dist
print(best_distance)
"""

##########
# PART 2 #
##########

data = open("day9in.txt").read().split("\n")
node_map = {}
for route in data:
    route = route.split(" ")
    if (route[0] not in node_map): node_map[route[0]] = []
    if (route[2] not in node_map): node_map[route[2]] = []
    node_map[route[0]].append((route[2], int(route[4])))
    node_map[route[2]].append((route[0], int(route[4])))

def recurse(u, node_map, previous = []):
    best_cost = 0
    for v, c in node_map[u]:
        if (v not in previous):
            cost = c + recurse(v, node_map, previous + [u])
            if (cost > best_cost): best_cost = cost
    return best_cost

best_distance = 0
for start in node_map:
    dist = recurse(start, node_map)
    if (dist > best_distance): best_distance = dist
print(best_distance)

"""
# Dijkstra's algorithm
max_val = 10000000000000000000000
best_distance = max_val
for start in node_map:
    queue = [start]
    cost = {u: max_val for u in node_map}
    cost[start] = 0
    previous = []
    
    while (len(queue) != 0):
        # Priority queue selection
        u = None
        best_val, best_index = max_val, 0
        i = 0
        for x in queue:
            if (cost[x] < best_val):
                best_val = cost[x]
                u = x
                best_index = i
            i += 1
        previous.append(u)
        queue.pop(best_index)
        
        for v, x in node_map[u]:
            if (v not in previous and cost[u] + x < cost[v]):
                cost[v] = cost[u] + x
                queue.append(v)

    print(start, cost)
    if (len(previous) == len(node_map)):
        smallest_dist = cost[previous[-1]]
        if (smallest_dist < best_distance):
            best_distance = smallest_dist

print(best_distance)
"""