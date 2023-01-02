import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# tree = {}
# nodes = []
# for line in lines:
#     line = line.split(" -> ")
#     node, val = line[0].split(" ")
#     val = int(val[1:-1])
#     if (len(line) == 2): children = line[1].split(", ")
#     else: children = []
#     tree[node] = (val, children)
#     nodes.append(node)
# for i in range(len(nodes)):
#     found = True
#     for j in range(len(nodes)):
#         if (i == j): continue
#         if (nodes[i] in tree[nodes[j]][1]):
#             found = False
#             break
#     if (found):
#         print(nodes[i])
#         break
# print(time.time() - start_time)

##########
# PART 2 #
##########

def balance(u, tree):
    if (len(tree[u][1]) == 0): return tree[u][0], None
    weights = []
    for v in tree[u][1]:
        val, adjusted = balance(v, tree)
        if (val == None): return None, adjusted
        weights.append(val)
    weight_set = set(weights)
    if (len(weight_set) == 2):
        a, b = weight_set
        if (weights.count(a) == 1):
            i = weights.index(a)
            return None, b - a + tree[tree[u][1][i]][0]
        else:
            i = weights.index(b)
            return None, a - b + tree[tree[u][1][i]][0]
    else:
        return len(tree[u][1]) * weights[0] + tree[u][0], None

start_time = time.time()
lines = open("input.txt").read().split("\n")
tree = {}
nodes = []
for line in lines:
    line = line.split(" -> ")
    node, val = line[0].split(" ")
    val = int(val[1:-1])
    if (len(line) == 2): children = line[1].split(", ")
    else: children = []
    tree[node] = (val, children)
    nodes.append(node)
root = None
for i in range(len(nodes)):
    found = True
    for j in range(len(nodes)):
        if (i == j): continue
        if (nodes[i] in tree[nodes[j]][1]):
            found = False
            break
    if (found):
        root = nodes[i]
        break
print(balance(root, tree)[1])
print(time.time() - start_time)