##########
# PART 1 #
##########

# import time

# def f(s, i, node, tree):
#     S = 0
#     num_children, header_len = s[i], s[i + 1]
#     children = []
#     node2 = node
#     i += 2
#     for _ in range(num_children):
#         children.append(node2 + 1)
#         node2, i, x = f(s, i, node2 + 1, tree)
#         S += x
#     tree[node] = [children, s[i : i + header_len]]
#     S += sum(tree[node][-1])
#     return node2, i + header_len, S

# start_time = time.time()
# s = [int(x) for x in open("input.txt").read().strip().split(' ')]
# tree = {}
# print(f(s, 0, 0, tree)[-1])
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

def f(s, i, node, tree):
    num_children, header_len = s[i], s[i + 1]
    children = []
    node2 = node
    i += 2
    for _ in range(num_children):
        children.append(node2 + 1)
        node2, i = f(s, i, node2 + 1, tree)
    tree[node] = [children, s[i : i + header_len]]
    return node2, i + header_len

start_time = time.time()
s = [int(x) for x in open("input.txt").read().strip().split(' ')]
tree = {}

memory = {}

def value_of(x, tree):
    global memory
    children, metadata = tree[x]
    if (x in memory): return memory[x]
    if (len(children) == 0):
        S = sum(metadata)
        memory[x] = S
        return S
    counts = {k - 1: metadata.count(k) for k in set(metadata)}
    S = 0
    for i in counts:
        if (not (0 <= i < len(children))): continue
        S += counts[i] * value_of(children[i], tree)
    memory[x] = S
    return S

f(s, 0, 0, tree)
print(value_of(0, tree))
print(time.time() - start_time)