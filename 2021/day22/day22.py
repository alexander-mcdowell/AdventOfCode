##########
# PART 1 #
##########

"""
data = open("day22in.txt").read().split("\n")
cubes = {}

for inst in data:
    inst_type, inst = inst.split(" ")
    x_range, y_range, z_range = inst.split(",")
    xlow, xhigh = [int(x) for x in x_range.replace("x=", "").split("..")]
    ylow, yhigh = [int(y) for y in y_range.replace("y=", "").split("..")]
    zlow, zhigh = [int(z) for z in z_range.replace("z=", "").split("..")]
    
    if (abs(xlow) > 50 or abs(xhigh) > 50 or abs(ylow) > 50 or abs(yhigh) > 50
        or abs(zlow) > 50 or abs(zhigh) > 50): continue
    
    for x in range(xlow, xhigh + 1):
        for y in range(ylow, yhigh + 1):
            for z in range(zlow, zhigh + 1):
                cube = (x, y, z)
                if (inst_type == "on"): cubes[cube] = True
                if (inst_type == "off" and cube in cubes): cubes[cube] = False

total_on = 0
for x in cubes:
    if (cubes[x]): total_on += 1
print(total_on)
"""

##########
# PART 2 #
##########

import time

start_time = time.time()
data = open("day22in.txt").read().split("\n")

def intersection(cuboid1, cuboid2):
    intersect = []
    for i in range(3):
        # No intersection
        if (cuboid1[i][0] > cuboid2[i][1] or cuboid1[i][1] < cuboid2[i][0]): return None
        intersect.append((max(cuboid1[i][0], cuboid2[i][0]), min(cuboid1[i][1], cuboid2[i][1])))
    return intersect

def exclude(cuboid, exclusion):
    # Assume that the entire region to exlcude lies within cuboid
    includes_across_dim = []
    for i in range(3):
        include = []
        if (cuboid[i][0] < exclusion[i][0]): include.append((cuboid[i][0], exclusion[i][0] - 1))
        if (cuboid[i][1] > exclusion[i][1]): include.append((exclusion[i][1] + 1, cuboid[i][1]))
        includes_across_dim.append(include + [exclusion[i]])

    included = []
    for x in includes_across_dim[0]:
        for y in includes_across_dim[1]:
            for z in includes_across_dim[2]:
                if (x != exclusion[0] or y != exclusion[1] or z != exclusion[2]): included.append([x, y, z])
    return included

def volume(cuboid):
    v = 1
    for i in range(3): v *= (cuboid[i][1] - cuboid[i][0]) + 1
    return v

disjoint_on = []
for inst in data:
    inst_type, inst = inst.split(" ")
    x_range, y_range, z_range = inst.split(",")
    xlow, xhigh = [int(x) for x in x_range.replace("x=", "").split("..")]
    ylow, yhigh = [int(y) for y in y_range.replace("y=", "").split("..")]
    zlow, zhigh = [int(z) for z in z_range.replace("z=", "").split("..")]
    cuboid = [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]

    if (inst_type == "on"):
        on_stack = [cuboid]
        while len(on_stack) != 0:
            cuboid = on_stack.pop(0)
    
            if (len(disjoint_on) == 0):
                disjoint_on.append(cuboid)
                continue
        
            # Check if there is any intersection between this "on" cuboid and any other cuboid already on
            flag = True
            for cuboid2 in disjoint_on:
                intersect = intersection(cuboid, cuboid2)
                if (intersect == None): continue

                # Remove the intersection from this "on" cuboid and try again with each newly formed cuboid
                flag = False
                after_exclude = exclude(cuboid, intersect)
                for cuboid3 in after_exclude: on_stack.insert(0, cuboid3)
                break
            if (flag): disjoint_on.append(cuboid)
    else:
        disjoint_off = [cuboid]
        while len(disjoint_off) != 0:
            off_cuboid = disjoint_off.pop(0)
            i = 0

            # Check if there is any intersection between this "off" cuboid and any "on" cuboid
            while i != len(disjoint_on):
                on_cuboid = disjoint_on[i]
                intersect = intersection(on_cuboid, off_cuboid)
                if (intersect != None):
                    disjoint_on.pop(i)
                    # Remove the intersection from this "on" cuboid and add all of the newly formed cuboids
                    after_exclude = exclude(on_cuboid, intersect)
                    for cuboid in after_exclude: disjoint_on.insert(i, cuboid)
                    # Remove the intersection from this "off" cuboid and try removal again with each newly formed off cuboid
                    after_exclude = exclude(off_cuboid, intersect)
                    for cuboid in after_exclude: disjoint_off.insert(0, cuboid)
                    break
                i += 1

total_on = 0
for cuboid in disjoint_on:
    #print(cuboid)
    total_on += volume(cuboid)
print(total_on)
print(time.time() - start_time)