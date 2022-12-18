import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# cubes = set()
# for line in lines:
#     cubes.add(tuple([int(x) for x in line.split(",")]))
# SA = 0
# for cube in cubes:
#     for k in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
#         cube2 = (cube[0] + k[0], cube[1] + k[1], cube[2] + k[2])
#         if (cube2 not in cubes): SA += 1
# print(SA)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
cubes = set()
min_x, max_x, min_y, max_y, min_z, max_z = None, None, None, None, None, None
for line in lines:
    cubes.add(tuple([int(x) for x in line.split(",")]))
SA = 0
potential_pocket = set()
for cube in cubes:
    if (min_x == None or cube[0] < min_x): min_x = cube[0]
    if (max_x == None or cube[0] > max_x): max_x = cube[0]
    
    if (min_y == None or cube[1] < min_y): min_y = cube[1]
    if (max_y == None or cube[1] > max_y): max_y = cube[1]
    
    if (min_z == None or cube[2] < min_z): min_z = cube[2]
    if (max_z == None or cube[2] > max_z): max_z = cube[2]

    for k in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        cube2 = (cube[0] + k[0], cube[1] + k[1], cube[2] + k[2])
        if (cube2 not in cubes):
            SA += 1
            potential_pocket.add(cube2)

def fill(cube, true_pocket, x_bounds, y_bounds, z_bounds):
    if (cube in true_pocket): return set()
    pockets = set()
    
    queue = [cube]
    pockets = set()
    while len(queue) != 0:
        cube = queue.pop(0)
        # Found a cube outside of the boundary
        if (not (x_bounds[1] >= cube[0] >= x_bounds[0] and y_bounds[1] >= cube[1] >= y_bounds[0] and \
            z_bounds[1] >= cube[2] >= z_bounds[0])): return set()
        for k in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            cube2 = (cube[0] + k[0], cube[1] + k[1], cube[2] + k[2])
            if (cube2 not in cubes and cube2 not in pockets and cube2 not in queue): queue.append(cube2)
        pockets.add(cube)
    return pockets

true_pocket = set()
for x in potential_pocket:
    s = fill(x, true_pocket, (min_x, max_x), (min_y, max_y), (min_z, max_z))
    for y in s: true_pocket.add(y)

removed = 0
for cube in true_pocket:
    for k in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        cube2 = (cube[0] + k[0], cube[1] + k[1], cube[2] + k[2])
        if (cube2 in cubes):
            removed += 1

print(SA - removed)
print(time.time() - start_time)