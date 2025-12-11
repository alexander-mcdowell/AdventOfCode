import timeit

##########
# PART 1 #
##########

# from collections import deque

# start_time = timeit.default_timer()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# graph = {}
# routes = {}
# for line in data:
#     device, outs = line.split(": ")
#     graph[device] = outs.split(" ")
#     routes[device] = 0

# routes["you"] = 1
# routes["out"] = 0
# queue = deque(["you"])
# seen = set()
# while len(queue) != 0:
#     device = queue.popleft()
#     if device in seen: continue
#     seen.add(device)
#     if device == "out": continue
#     for adj in graph[device]:
#         routes[adj] += routes[device]
#         queue.append(adj)
# print(routes["out"  ])
# print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
graph = {}
for line in data:
    device, outs = line.split(": ")
    graph[device] = outs.split(" ")

memo = {}
def routes_to(device, target):
    if device==target: return 1
    if device not in graph: return 0
    if device in memo: return memo[device]
    count = 0
    for adj in graph[device]:
        count += routes_to(adj, target)
    memo[device] = count
    return count

routes = [["svr","fft","dac","out"], ["svr","dac","fft","out"]]
count = 0
for route in routes:
    subcount = 1
    for i in range(len(route)-1):
        memo = {}
        x = routes_to(route[i], route[i+1])
        subcount *= x
    count += subcount
print(count)
print(timeit.default_timer() - start_time)