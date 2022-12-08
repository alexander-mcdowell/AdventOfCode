import time

##########
# PART 1 #
##########

# class Node:
#     def __init__(self, name, value, parent):
#         self.value = value
#         self.name = name
#         self.children = []
#         self.parent = parent
#     def add_child(self, node):
#         self.children.append(node)

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# root = Node(None, None, None)
# iter = root
# i = 0
# while i != len(lines):
#     line = lines[i].split(" ")
#     if (line[0] == "$"):
#         if (line[1] == "cd"):
#             if line[2] == "..":
#                 iter = iter.parent
#                 i += 1
#             else:
#                 dirname = line[2]
#                 found = False
#                 found_index = 0
#                 for n in iter.children:
#                     if (n.value == None and n.name == dirname):
#                         found = True
#                         break
#                     found_index += 1
#                 if (not found):
#                     iter.add_child(Node(dirname, None, iter))
#                     iter = iter.children[-1]
#                 else: iter = iter.children[found_index]
#                 i += 1
#         elif (line[1] == "ls"):
#             i += 1
#             while i != len(lines) and lines[i][0] != "$":
#                 line = lines[i].split(" ")
#                 if (line[0] == "dir"):
#                     dirname = line[1]
#                     found = False
#                     for n in iter.children:
#                         if (n.value == None and n.name == dirname):
#                             found = True
#                             break
#                     if (not found): iter.add_child(Node(dirname, None, iter))
#                 else:
#                     size, filename = int(line[0]), line[1]
#                     found = False
#                     for n in iter.children:
#                         if (n.value == size and n.name == filename):
#                             found = True
#                             break
#                     if (not found): iter.add_child(Node(filename, size, iter))
#                 i += 1
#     else: i += 1

# def calculate_size(root, S = 0):
#     sz = 0
#     for node in root.children:
#         if node.value == None:
#             x, s = calculate_size(node)
#             S += s
#             sz += x
#         else: sz += node.value
#     if (sz <= 100000): S += sz
#     return sz, S

# print(calculate_size(root)[1])
# print(time.time() - start_time)

##########
# PART 2 #
##########

class Node:
    def __init__(self, name, value, parent):
        self.value = value
        self.name = name
        self.children = []
        self.parent = parent
    def add_child(self, node):
        self.children.append(node)

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
root = Node(None, None, None)
iter = root
i = 0
while i != len(lines):
    line = lines[i].split(" ")
    if (line[0] == "$"):
        if (line[1] == "cd"):
            if line[2] == "..":
                iter = iter.parent
                i += 1
            else:
                dirname = line[2]
                found = False
                found_index = 0
                for n in iter.children:
                    if (n.value == None and n.name == dirname):
                        found = True
                        break
                    found_index += 1
                if (not found):
                    iter.add_child(Node(dirname, None, iter))
                    iter = iter.children[-1]
                else: iter = iter.children[found_index]
                i += 1
        elif (line[1] == "ls"):
            i += 1
            while i != len(lines) and lines[i][0] != "$":
                line = lines[i].split(" ")
                if (line[0] == "dir"):
                    dirname = line[1]
                    found = False
                    for n in iter.children:
                        if (n.value == None and n.name == dirname):
                            found = True
                            break
                    if (not found): iter.add_child(Node(dirname, None, iter))
                else:
                    size, filename = int(line[0]), line[1]
                    found = False
                    for n in iter.children:
                        if (n.value == size and n.name == filename):
                            found = True
                            break
                    if (not found): iter.add_child(Node(filename, size, iter))
                i += 1
    else: i += 1

def calculate_size(root, S = 0):
    sz = 0
    for node in root.children:
        if node.value == None:
            x, s = calculate_size(node)
            S += s
            sz += x
        else: sz += node.value
    if (sz <= 100000): S += sz
    return sz, S

def remove_dir(root, total, S = None):
    sz = 0
    for node in root.children:
        if node.value == None:
            x, s = remove_dir(node, total, S)
            if ((s != None and S == None) or (s != None and s < S)): S = s
            sz += x
        else: sz += node.value
    if (root.value == None and (70000000 - total) + sz >= 30000000 and (S == None or sz < S)): S = sz
    return sz, S

SZ = calculate_size(root)[0]
print(remove_dir(root, SZ)[1])
print(time.time() - start_time)