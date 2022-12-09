import time

##########
# PART 1 #
##########

# start_time = time.time()
# grid = {}
# lines = open("input.txt", "r+").read().split("\n")
# head_pos = [0, 0]
# tail_pos = [0, 0]
# for inst in lines:
#     direction, count = inst.split(" ")
#     if (direction == "R"): kx, ky = 1, 0
#     elif (direction == "L"): kx, ky = -1, 0
#     elif (direction == "U"): kx, ky = 0, 1
#     else: kx, ky = 0, -1
#     for _ in range(int(count)):
#         last_head_pos = [x for x in head_pos]
#         head_pos = [head_pos[0] + kx, head_pos[1] + ky]
#         if ((head_pos[0] - tail_pos[0]) ** 2 + (head_pos[1] - tail_pos[1]) ** 2 > 2):
#             tail_pos = last_head_pos
#         t = tuple(tail_pos)
#         if (t not in grid): grid[t] = 1
# s = 0
# for x in grid: s += grid[x]
# print(s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
N = 10
grid = {}
lines = open("input.txt", "r+").read().split("\n")
head_pos = [0, 0]
tails_pos = [[0, 0] for _ in range(N - 1)]
for inst in lines:
    direction, count = inst.split(" ")
    if (direction == "R"): kx, ky = 1, 0
    elif (direction == "L"): kx, ky = -1, 0
    elif (direction == "U"): kx, ky = 0, 1
    else: kx, ky = 0, -1
    for _ in range(int(count)):
        head_pos = [head_pos[0] + kx, head_pos[1] + ky]
        if ((head_pos[0] - tails_pos[0][0]) ** 2 + (head_pos[1] - tails_pos[0][1]) ** 2 > 2):
            tails_pos[0][0] = head_pos[0] - kx
            tails_pos[0][1] = head_pos[1] - ky
        for i in range(N - 2):
            dx, dy = tails_pos[i][0] - tails_pos[i + 1][0], tails_pos[i][1] - tails_pos[i + 1][1]
            if (dx ** 2 + dy ** 2 > 2):
                # Same column
                if (tails_pos[i][0] == tails_pos[i + 1][0]):
                    # Up
                    if (dy > 0): tails_pos[i + 1][1] += 1
                    # Down
                    else: tails_pos[i + 1][1] -= 1
                # Same row
                elif (tails_pos[i][1] == tails_pos[i + 1][1]):
                    # Right
                    if (dx > 0): tails_pos[i + 1][0] += 1
                    # Left
                    else: tails_pos[i + 1][0] -= 1
                # Diagonal:
                else:
                    if (dx > 0): tails_pos[i + 1][0] += 1
                    else: tails_pos[i + 1][0] -= 1
                    if (dy > 0): tails_pos[i + 1][1] += 1
                    else: tails_pos[i + 1][1] -= 1
                    
        t = tuple(tails_pos[N - 2])
        if (t not in grid): grid[t] = 1
s = 0
for x in grid: s += grid[x]
print(s)
print(time.time() - start_time)