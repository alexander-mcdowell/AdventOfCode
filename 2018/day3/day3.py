import time

##########
# PART 1 #
##########

# start_time = time.time()
# fabrics = open("input.txt").read().split("\n")
# overlaps = set()
# for i in range(len(fabrics)):
#     fabric = fabrics[i]
#     fabric = fabric.split(" ")
#     x, y = [int(k) for k in fabric[2][:-1].split(",")]
#     w, h = [int(k) for k in fabric[3].split('x')]
#     for j in range(len(fabrics)):
#         if (i == j): continue
#         fabric2 = fabrics[j]
#         fabric2 = fabric2.split(" ")
#         x2, y2 = [int(k) for k in fabric2[2][:-1].split(",")]
#         w2, h2 = [int(k) for k in fabric2[3].split('x')]
        
#         for x3 in range(x, x + w):
#             if (not (x2 <= x3 < x2 + w2)): continue
#             for y3 in range(y, y + h):
#                 if (y2 <= y3 < y2 + h2): overlaps.add((x3, y3))
# print(len(overlaps))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
fabrics = open("input.txt").read().split("\n")
overlaps = set()
for i in range(len(fabrics)):
    fabric = fabrics[i]
    fabric = fabric.split(" ")
    x, y = [int(k) for k in fabric[2][:-1].split(",")]
    w, h = [int(k) for k in fabric[3].split('x')]
    count = 0
    for j in range(len(fabrics)):
        if (i == j): continue
        fabric2 = fabrics[j]
        fabric2 = fabric2.split(" ")
        x2, y2 = [int(k) for k in fabric2[2][:-1].split(",")]
        w2, h2 = [int(k) for k in fabric2[3].split('x')]
        
        added = False
        for x3 in range(x, x + w):
            if (not (x2 <= x3 < x2 + w2)): continue
            for y3 in range(y, y + h):
                if (y2 <= y3 < y2 + h2):
                    added = True
                    break
            if (added): break
        if (not added): count += 1
    if (count == len(fabrics) - 1):
        print(fabrics[i].split(" ")[0])
        break
print(len(overlaps))
print(time.time() - start_time)