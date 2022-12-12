import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# adj_matrix, cost_matrix = {}, {}
# start_pos, end_pos = None, None
# n, m = len(lines), len(lines[0])
# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         if (lines[i][j] == "S"): start_pos = (i, j)
#         elif (lines[i][j] == "E"): end_pos = (i, j)
#         for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             if ((n > i + k[0] >= 0) and (m > j + k[1] >= 0)):
#                 flag = False
#                 if (lines[i][j] == "S"):
#                     flag = lines[i + k[0]][j + k[1]] == "a"
#                 elif (lines[i + k[0]][j + k[1]] == "E"):
#                     flag = (ord('z') - ord(lines[i][j])) <= 1
#                 else:
#                     flag = (ord(lines[i + k[0]][j + k[1]]) - ord(lines[i][j])) <= 1
#                 if (flag):
#                     if ((i, j) not in adj_matrix):
#                         adj_matrix[(i, j)] = []
#                         cost_matrix[(i, j)] = -1
#                     if (ord(lines[i + k[0]][j + k[1]]) <= ord(lines[i][j]) and (i + k[0], j + k[1]) not in adj_matrix):
#                         adj_matrix[(i + k[0], j + k[1])] = []
#                         cost_matrix[(i +k[0], j + k[1])] = -1
#                     adj_matrix[(i, j)].append((i + k[0], j + k[1]))
# adj_matrix[end_pos] = []
# cost_matrix[start_pos] = 0
# cost_matrix[end_pos] = -1
# print(start_pos, end_pos)

# # Dijkstra's Algorithm
# pq = [(start_pos, 0)]
# while len(pq) != 0:
#     u, cost, best_i = None, -1, 0
#     for i in range(len(pq)):
#         node = pq[i]
#         if (cost == -1 or node[1] < cost):
#             u, cost, best_i = node[0], node[1], i
#     pq.pop(best_i)
    
#     for v in adj_matrix[u]:
#         if (cost_matrix[v] == -1 or cost + 1 < cost_matrix[v]):
#             cost_matrix[v] = cost + 1
#             pq.append((v, cost + 1))
# print(cost_matrix[end_pos])
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
adj_matrix, cost_matrix = {}, {}
start_pos, end_pos = [], None
n, m = len(lines), len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (lines[i][j] in ["S", "a"]): start_pos.append((i, j))
        elif (lines[i][j] == "E"): end_pos = (i, j)
        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if ((n > i + k[0] >= 0) and (m > j + k[1] >= 0)):
                flag = False
                if (lines[i][j] == "S"):
                    flag = lines[i + k[0]][j + k[1]] == "a"
                elif (lines[i + k[0]][j + k[1]] == "E"):
                    flag = (ord('z') - ord(lines[i][j])) <= 1
                else:
                    flag = (ord(lines[i + k[0]][j + k[1]]) - ord(lines[i][j])) <= 1
                if (flag):
                    if ((i, j) not in adj_matrix):
                        adj_matrix[(i, j)] = []
                        cost_matrix[(i, j)] = -1
                    if (ord(lines[i + k[0]][j + k[1]]) <= ord(lines[i][j]) and (i + k[0], j + k[1]) not in adj_matrix):
                        adj_matrix[(i + k[0], j + k[1])] = []
                        cost_matrix[(i +k[0], j + k[1])] = -1
                    adj_matrix[(i, j)].append((i + k[0], j + k[1]))
adj_matrix[end_pos] = []
cost_matrix[end_pos] = -1
best = 100000000000000000

for sp in start_pos:
    cost_matrix_copy = {x: cost_matrix[x] for x in cost_matrix}
    cost_matrix[sp] = 0

    # Dijkstra's Algorithm
    pq = [(sp, 0)]
    while len(pq) != 0:
        u, cost, best_i = None, -1, 0
        for i in range(len(pq)):
            node = pq[i]
            if (cost == -1 or node[1] < cost):
                u, cost, best_i = node[0], node[1], i
        pq.pop(best_i)
        if (cost == -1): break
        
        for v in adj_matrix[u]:
            if (cost_matrix_copy[v] == -1 or cost + 1 < cost_matrix_copy[v]):
                cost_matrix_copy[v] = cost + 1
                pq.append((v, cost + 1))
    shortest = cost_matrix_copy[end_pos]
    if (shortest != -1 and shortest < best):
        best = shortest
print(best)
print(time.time() - start_time)