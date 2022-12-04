##########
# PART 1 #
##########

"""
data = open("day22in.txt").read().split("\n")
nodes = {}
node_list = []
for i in range(2, len(data)):
    line = data[i]
    line = [x for x in line.split(' ') if x != '']
    node = line[0].split('-')
    node = (int(node[-2][1:]), int(node[-1][1:]))
    nodes[node] = (int(line[1][:-1]), int(line[2][:-1]))
    node_list.append(node)

counts = 0
for i in range(len(node_list)):
    for j in range(len(node_list)):
        if (i == j): continue
        i_used = nodes[node_list[i]][1]
        j_avail = nodes[node_list[j]][0] - nodes[node_list[j]][1]
        if (i_used != 0 and i_used <= j_avail):
            counts += 1
print(counts)
"""

##########
# PART 2 #
##########