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

data = open("day22in.txt").read().split("\n")

total_on = 0
cuboids = []
for inst in data:
    inst_type, inst = inst.split(" ")
    x_range, y_range, z_range = inst.split(",")
    xlow, xhigh = [int(x) for x in x_range.replace("x=", "").split("..")]
    ylow, yhigh = [int(y) for y in y_range.replace("y=", "").split("..")]
    zlow, zhigh = [int(z) for z in z_range.replace("z=", "").split("..")]
    
    xside, yside, zside = xhigh - xlow + 1, yhigh - ylow + 1, zhigh - zlow + 1
    corner = (xlow, ylow, zlow)

print(total_on)