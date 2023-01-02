import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# grid = []
# start_col = None
# for i in range(len(lines)):
#     if (i == 0):
#         row = []
#         for j in range(len(lines[0])):
#             if (lines[0][j] != ' '):
#                 start_col = j
#             row.append(lines[0][j])
#         grid.append(row)
#     else: grid.append(list(lines[i]))

# RIGHT = 0
# DOWN = 1
# LEFT = 2
# UP = 3

# pos = (0, start_col)
# direction = DOWN
# s = ""
# while True:
#     # Change direction
#     if (grid[pos[0]][pos[1]] == '+'):
#         adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         adj_list[(direction + 2) % 4] = None
#         for i in range(4):
#             if (adj_list[i] == None): continue
#             adj = adj_list[i]
#             if (0 <= pos[0] + adj[0] < len(grid) and 0 <= pos[1] + adj[1] < len(grid[0])):
#                 pos2 = (pos[0] + adj[0], pos[1] + adj[1])
#                 if (grid[pos2[0]][pos2[1]] != ' '):
#                     # Assume only one correct direction to go
#                     direction = i
#                     break
#     # Maintain current direction
#     if (ord('A') <= ord(grid[pos[0]][pos[1]]) <= ord('Z')): s += grid[pos[0]][pos[1]]
#     adj = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
#     if (0 <= pos[0] + adj[0] < len(grid) and 0 <= pos[1] + adj[1] < len(grid[0]) and grid[pos[0]][pos[1]] != ' '):
#         pos = (pos[0] + adj[0], pos[1] + adj[1])
#     else: break
# print(s)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
grid = []
start_col = None
for i in range(len(lines)):
    if (i == 0):
        row = []
        for j in range(len(lines[0])):
            if (lines[0][j] != ' '):
                start_col = j
            row.append(lines[0][j])
        grid.append(row)
    else: grid.append(list(lines[i]))

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

pos = (0, start_col)
direction = DOWN
steps = 0
while True:
    # Change direction
    if (grid[pos[0]][pos[1]] == '+'):
        adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        adj_list[(direction + 2) % 4] = None
        for i in range(4):
            if (adj_list[i] == None): continue
            adj = adj_list[i]
            if (0 <= pos[0] + adj[0] < len(grid) and 0 <= pos[1] + adj[1] < len(grid[0])):
                pos2 = (pos[0] + adj[0], pos[1] + adj[1])
                if (grid[pos2[0]][pos2[1]] != ' '):
                    # Assume only one correct direction to go
                    direction = i
                    break
    # Maintain current direction
    adj = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
    if (0 <= pos[0] + adj[0] < len(grid) and 0 <= pos[1] + adj[1] < len(grid[0]) and grid[pos[0]][pos[1]] != ' '):
        pos = (pos[0] + adj[0], pos[1] + adj[1])
        steps += 1
    else: break
print(steps)
print(time.time() - start_time)