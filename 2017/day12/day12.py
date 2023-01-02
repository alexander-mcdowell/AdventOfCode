import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# adj = {}
# for line in lines:
#     line = line.split(" <-> ")
#     node, children = line
#     children = children.split(", ")
#     if (node not in adj): adj[node] = []
#     for child in children:
#         if (child not in adj): adj[child] = []
#         adj[node].append(child)
#         adj[child].append(node)

# def dfs(node, adj, prev = set()):
#     count = 1
#     prev.add(node)
#     for child in adj[node]:
#         if (child not in prev):
#             count2, prev2 = dfs(child, adj, prev)
#             prev.union(prev2)
#             count += count2
#     return count, prev

# print(dfs('0', adj)[0])
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
adj = {}
for line in lines:
    line = line.split(" <-> ")
    node, children = line
    if (node not in adj): adj[node] = []
    children = children.split(", ")
    for child in children:
        if (child not in adj[node]): adj[node].append(child)
        if (child != node):
            if (child not in adj): adj[child] = []
            if (node not in adj[child]): adj[child].append(node)

def dfs(node, adj, prev):
    count = 1
    prev.add(node)
    for child in adj[node]:
        if (child not in prev):
            count2, prev2 = dfs(child, adj, prev)
            prev.union(prev2)
            count += count2
    return count, prev

queue = list(adj)
count = 0
while len(queue) != 0:
    node = queue[0]
    group = dfs(node, adj, set())[1]
    for node in group: queue.remove(node)
    count += 1
print(count)
print(time.time() - start_time)