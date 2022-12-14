import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# grid = {}
# max_y = 0
# for line in lines:
#     points = line.split(" -> ")
#     for i in range(len(points) - 1):
#         src = [int(x) for x in points[i].split(",")]
#         dest = [int(x) for x in points[i+ 1].split(",")]
#         if (src[0] == dest[0]):
#             diff = -1 if (src[1] - dest[1]) > 0 else 1
#             for y in range(src[1], dest[1] + diff, diff):
#                 grid[(src[0], y)] = '#'
#         else:
#             diff = -1 if (src[0] - dest[0]) > 0 else 1
#             for x in range(src[0], dest[0] + diff, diff):
#                 grid[(x, src[1])] = '#'
#         if (src[1] > max_y): max_y = src[1]
#         if (dest[1] > max_y): max_y = dest[1]

# end = False
# count = 0
# while not end:
#     # Spawn sand
#     sand = [500, 0]

#     # Find place for sand
#     while True:
#         if (sand[1] == max_y):
#             end = True
#             break

#         if ((sand[0], sand[1] + 1) in grid):
#             if ((sand[0] - 1, sand[1] + 1) not in grid):
#                 sand[0] -= 1
#             elif ((sand[0] + 1, sand[1] + 1) not in grid):
#                 sand[0] += 1
#             else:
#                 grid[(sand[0], sand[1])] = 'o'
#                 count += 1
#                 break
#         sand[1] += 1

# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
grid = {}
max_y = 0
for line in lines:
    points = line.split(" -> ")
    for i in range(len(points) - 1):
        src = [int(x) for x in points[i].split(",")]
        dest = [int(x) for x in points[i+ 1].split(",")]
        if (src[0] == dest[0]):
            diff = -1 if (src[1] - dest[1]) > 0 else 1
            for y in range(src[1], dest[1] + diff, diff):
                grid[(src[0], y)] = '#'
        else:
            diff = -1 if (src[0] - dest[0]) > 0 else 1
            for x in range(src[0], dest[0] + diff, diff):
                grid[(x, src[1])] = '#'
        if (src[1] > max_y): max_y = src[1]
        if (dest[1] > max_y): max_y = dest[1]

end = False
count = 0
while not end:
    # Spawn sand
    sand = [500, 0]

    # Find place for sand
    while True:
        if (sand[1] == max_y + 1):
            grid[(sand[0], sand[1])] = 'o'
            count += 1
            break

        if ((sand[0], sand[1] + 1) in grid):
            if ((sand[0] - 1, sand[1] + 1) not in grid):
                sand[0] -= 1
            elif ((sand[0] + 1, sand[1] + 1) not in grid):
                sand[0] += 1
            else:
                grid[(sand[0], sand[1])] = 'o'
                count += 1
                if (sand[0] == 500 and sand[1] == 0):
                    end = True
                break
        sand[1] += 1

print(count)
print(time.time() - start_time)