import time

# ##########
# # PART 1 #
# ##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# graph = {}
# for l in data:
#     u, v = l.split("-")
#     if (u not in graph): graph[u] = set([v])
#     else: graph[u].add(v)
#     if (v not in graph): graph[v] = set([u])
#     else: graph[v].add(u)
# nodes = list(graph)
# valids = set()
# for i in range(len(nodes)):
#     u = nodes[i]
#     for v in graph[u]:
#         for w in graph[v]:
#             if (u in graph[w] and 't' in [u[0], v[0], w[0]]): valids.add(tuple(sorted([u, v, w])))
# print(len(valids))
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
graph = {}
for l in data:
    u, v = l.split("-")
    if (u not in graph): graph[u] = set([v])
    else: graph[u].add(v)
    if (v not in graph): graph[v] = set([u])
    else: graph[v].add(u)
nodes = list(graph)

best_len, best = 0, None
cluster = set()
seen = set()
def findLargest(adj):
    global best_len, best, cluster
    
    t = tuple(sorted([x for x in cluster]))
    if (t in seen): return
    seen.add(t)
    
    if (len(cluster) > best_len):
        best_len = len(cluster)
        best = cluster.copy()
    for u in adj:
        if (u in cluster): continue
        
        valid = True
        for v in cluster:
            if (u not in graph[v]):
                valid = False
                break
        if (not valid): continue
        
        cluster.add(u)
        findLargest(graph[u])
        cluster.remove(u)
        
findLargest(nodes)
print(",".join(sorted([x for x in best])))
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")