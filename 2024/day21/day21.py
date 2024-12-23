import time

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")

# # A state takes the form (i1, j1, i2, j2, i3, j3, i4, j4)
# # (i1, j1) is the position of the number robot
# # (i2, j2) is the position of the first direction robot
# # (i3, j3) is the position of the second direction robot
# # (i4, j4) is the position of my number controller

# # Return none if out of bounds
# def get_state(u, action, i = 3):
#     if (action == 'A'):
#         if (i == 0): return None
        
#     else:
#         v = list(u)
#         v[2 * i] += action[0]
#         v[2 * i + 1] += action[1]
#         if (i != 0 and not (0 <= v[2 * i] < 2 and 0 <= v[2 * i + 1] < 3 and (v[2 * i], v[2 * i + 1]) != (0, 0))): return None
#         if (i == 0 and not (0 <= v[2 * i] < 4 and 0 <= v[2 * i + 1] < 3 and (v[2 * i], v[2 * i + 1]) != (3, 0))): return None
#     return tuple(v)

# # Dijkstra's
# def dijkstra(start_pos):
#     dists = {}
#     prevs = {}
#     dists[start_pos] = 0
#     stack = [start_pos]
#     while len(stack) != 0:
#         u_val, best_i = -1, 0
#         for i in range(len(stack)):
#             v = stack[i]
#             if (u_val==-1 or dists[v] < u_val):
#                 best_i = i
#                 u_val = dists[v]
#         u = stack.pop(best_i)
        
#         # action = left, right, up, down, or activate
        
#         # Action on first direction robot
#         for k in range(4):
#             action = [(0, 1), (-1, 0), (0, -1), (1, 0), 'A'][k]
#             v = get_state(u, action)
#             if (v == None): continue

#             # Check if best
#             x = u_val + 1
#             if (v not in dists or x < dists[v]):
#                 dists[v] = x
#                 prevs[v] = u
#                 stack.append(v)
#     return dists, prevs

# def code_to_pos(c):
#     if (c == '0'): return (3, 1)
#     if (c == 'A'): return (3, 2)
#     x = int(c)
#     y = (x-1)//3
#     # Remaining pointers must be on A
#     return (2 - y, (x-1)%3, 0, 2, 0, 2, 0, 2)

# start_pos = (3, 2, 0, 2, 0, 2, 0, 2)
# end_pos = code_to_pos('9')
# print(end_pos)
# #dists, prevs = dijkstra(start_pos)
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")

print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")