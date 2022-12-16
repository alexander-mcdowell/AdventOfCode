import time

##########
# PART 1 #
##########

# start_time = time.time()

# lines = open("input.txt", "r+").read().split("\n")
# valves = {}
# non_zero_valves = []
# for line in lines:
#     line = line.split(" ")
#     source, rate, dest = line[1], line[4], line[9:]
#     rate = int(rate[5:-1])
#     dest = [x.replace(",", "") for x in dest]
#     valves[source] = (rate, dest)
#     if (rate != 0): non_zero_valves.append(source)

# cost_matrices = {}
# for valve in ['AA'] + non_zero_valves:
#     # Dijkstra's Algorithm
#     cost_matrix = {u: -1 for u in valves}
#     cost_matrix[valve] = 0
#     pq = [(valve, 0)]
#     while len(pq) != 0:
#         u, cost, best_i = None, -1, 0
#         for i in range(len(pq)):
#             node = pq[i]
#             if (cost == -1 or node[1] < cost):
#                 u, cost, best_i = node[0], node[1], i
#         pq.pop(best_i)
#         if (cost == -1): break
        
#         for v in valves[u][1]:
#             if (cost_matrix[v] == -1 or cost + 1 < cost_matrix[v]):
#                 cost_matrix[v] = cost + 1
#                 pq.append((v, cost + 1))
#     cost_matrices[valve] = cost_matrix

# def search(u, non_zero_valves, cost_matrices, t = 30, curr = []):
#     if (t <= 0): return 0
#     if (len(curr) == 1 + len(non_zero_valves)): return 0
#     best_val = 0
#     cm = cost_matrices[u]
#     for v in non_zero_valves:
#         if (v not in curr):
#             t2 = t - (cm[v] + 1)
#             if (t2 <= 0): continue
#             val = t2 * valves[v][0] + search(v, non_zero_valves, cost_matrices, t2, curr + [v])
#             if (val > best_val): best_val = val
#     return best_val

# print(search('AA', non_zero_valves, cost_matrices, curr = ['AA']))
# print(time.time() - start_time)

##########
# PART 2 #
##########

from itertools import combinations

start_time = time.time()

lines = open("input.txt", "r+").read().split("\n")
valves = {}
non_zero_valves = []
for line in lines:
    line = line.split(" ")
    source, rate, dest = line[1], line[4], line[9:]
    rate = int(rate[5:-1])
    dest = [x.replace(",", "") for x in dest]
    valves[source] = (rate, dest)
    if (rate != 0): non_zero_valves.append(source)

cost_matrices = {}
for valve in ['AA'] + non_zero_valves:
    # Dijkstra's Algorithm
    cost_matrix = {u: -1 for u in valves}
    cost_matrix[valve] = 0
    pq = [(valve, 0)]
    while len(pq) != 0:
        u, cost, best_i = None, -1, 0
        for i in range(len(pq)):
            node = pq[i]
            if (cost == -1 or node[1] < cost):
                u, cost, best_i = node[0], node[1], i
        pq.pop(best_i)
        if (cost == -1): break
        
        for v in valves[u][1]:
            if (cost_matrix[v] == -1 or cost + 1 < cost_matrix[v]):
                cost_matrix[v] = cost + 1
                pq.append((v, cost + 1))
    cost_matrices[valve] = cost_matrix

def search(u, non_zero_valves, cost_matrices, t = 26, curr = []):
    if (t <= 0): return 0
    if (len(curr) == 1 + len(non_zero_valves)): return 0
    best_val = 0
    cm = cost_matrices[u]
    for v in non_zero_valves:
        if (v not in curr):
            t2 = t - (cm[v] + 1)
            if (t2 <= 0): continue
            val = t2 * valves[v][0] + search(v, non_zero_valves, cost_matrices, t2, curr + [v])
            if (val > best_val): best_val = val
    return best_val

best = 0
for r in range(1, 1 + len(non_zero_valves)//2):
    print("Testing elephant length " + str(r) + " path")
    for c in combinations(non_zero_valves, r):
        val = search('AA', c, cost_matrices, curr = ['AA'])
        if (val == 0): continue
        remaining = [x for x in non_zero_valves if x not in c]
        val += search('AA', remaining, cost_matrices, curr = ['AA'])
        if (val > best): best = val
print(best)
print(time.time() - start_time)