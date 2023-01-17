##########
# PART 1 #
##########

# import time

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# preceeding = {}
# for line in lines:
#     line = line.split(" ")
#     src, dest = line[1], line[7]
#     if (src not in preceeding): preceeding[src] = []
#     if (dest not in preceeding): preceeding[dest] = []
#     preceeding[dest].append(src)

# s = ""
# while True:
#     src = None
#     for node in preceeding:
#         if (preceeding[node] != None and len(preceeding[node]) == 0):
#             if (src == None or ord(node) < ord(src)):
#                 src = node
#     if (src == None): break
#     s += src
#     preceeding[src] = None
#     for node in preceeding:
#         if (preceeding[node] != None and src in preceeding[node]): preceeding[node].remove(src)
# print(s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

start_time = time.time()
lines = open("input.txt").read().split("\n")
preceeding = {}
for line in lines:
    line = line.split(" ")
    src, dest = line[1], line[7]
    if (src not in preceeding): preceeding[src] = []
    if (dest not in preceeding): preceeding[dest] = []
    preceeding[dest].append(src)

total = 0
workers = 5
dt = 60
chosen = [[None, 0] for _ in range(workers)]
while True:
    flag = False
    picked = set()
    for i in range(workers):
        if (chosen[i][1] == 0):
            if (chosen[i][0] != None):
                src = chosen[i][0]
                for node in preceeding:
                    if (preceeding[node] != None and src in preceeding[node]): preceeding[node].remove(src)
                preceeding[src] = None
                chosen[i] = [None, 0]
            
            src = None
            for node in preceeding:
                if (preceeding[node] != None and node not in picked and len(preceeding[node]) == 0):
                    found = False
                    for node2 in chosen:
                        if (node2[0] == node):
                            found = True
                            break
                    if (not found and (src == None or ord(node) < ord(src))):
                        src = node
            if (src == None):
                chosen[i] = [None, 0]
                continue
            chosen[i] = [src, dt + ord(src) - ord('A') + 1]
            picked.add(src)
            flag = True
    if (not flag):
        flag = True
        for i in range(workers):
            if (chosen[i][0] != None):
                flag = False
                break
        if (flag): break

    min_time = -1
    for i in range(workers):
        if (chosen[i][0] != None and (min_time == -1 or chosen[i][1] < min_time)):
            min_time = chosen[i][1]
    for i in range(workers):
        if (chosen[i][0] != None): chosen[i][1] -= min_time
    total += min_time

print(total)
print(time.time() - start_time)