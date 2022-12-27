import time
import math

##########
# PART 1 #
##########

# import heapq

# # Linear programming solution
# def extract_max(max_t, costs):
#     max_bots = 1 + max_t//min(costs[0], costs[1], costs[2][0], costs[2][1], costs[3][0], costs[3][1])

#     best, best_state = 0, None

#     # Create the cost matrix, consisting of a minimum timestep and maximized resources to get to that particular combination
#     # of bots.
#     cost_matrix = {}
#     for a in range(1, max_bots):
#         for b in range(max_bots):
#             for c in range(max_bots):
#                 for d in range(max_bots): cost_matrix[(a, b, c, d)] = -1
#     cost_matrix[(1, 0, 0, 0)] = 1

#     pq = []
#     heapq.heappush(pq, (1, (1, 0, 0, 0), (0, 0, 0, 0)))
#     while len(pq) != 0:
#         # Choose the earliest timestep bot combiination
#         t, robots_chosen, resources_chosen = heapq.heappop(pq)

#         # Check next geode robot
#         if (robots_chosen[2] >= 1):
#             # Number of timesteps until sufficient resources are gathered.
#             dt1 = math.ceil((costs[3][0] - resources_chosen[0])/robots_chosen[0])
#             dt2 = math.ceil((costs[3][1] - resources_chosen[2])/robots_chosen[2])
#             dt = max(0, dt1, dt2) + 1

#             if (t + dt <= max_t):
#                 # Update resources accordingly
#                 resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[3][0],
#                               resources_chosen[1] + dt * robots_chosen[1],
#                               resources_chosen[2] + dt * robots_chosen[2] - costs[3][1],
#                               resources_chosen[3] + dt * robots_chosen[3])

#                 # Update robots accordingly
#                 robots2 = (robots_chosen[0], robots_chosen[1], robots_chosen[2], robots_chosen[3] + 1)

#                 if (max(robots2) < max_bots):
#                     if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
#                         cost_matrix[robots2] = t + dt
#                         #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
#                         heapq.heappush(pq, (t + dt, robots2, resources2))
                        
#                         resources2 = list(resources2)
#                         for k in range(4):
#                             resources2[k] += (max_t - t - dt + 1) * robots2[k]
#                         quantity = resources2[3]
#                         if (quantity > best):
#                             best = quantity
#                             best_state = (robots2, tuple(resources2))

#         # Check next obsidian robot
#         if (costs[3][1] > robots_chosen[2] and robots_chosen[1] >= 1):
#             # Number of timesteps until sufficient resources are gathered.
#             dt1 = math.ceil((costs[2][0] - resources_chosen[0])/robots_chosen[0])
#             dt2 = math.ceil((costs[2][1] - resources_chosen[1])/robots_chosen[1])
#             dt = max(0, dt1, dt2) + 1

#             if (t + dt <= max_t):
#                 # Update resources accordingly
#                 resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[2][0],
#                               resources_chosen[1] + dt * robots_chosen[1] - costs[2][1],
#                               resources_chosen[2] + dt * robots_chosen[2],
#                               resources_chosen[3] + dt * robots_chosen[3])

#                 # Update robots accordingly
#                 robots2 = (robots_chosen[0], robots_chosen[1], robots_chosen[2] + 1, robots_chosen[3])

#                 if (max(robots2) < max_bots):
#                     if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
#                         cost_matrix[robots2] = t + dt
#                         #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
#                         heapq.heappush(pq, (t + dt, robots2, resources2))
                        
#                         resources2 = list(resources2)
#                         for k in range(4):
#                             resources2[k] += (max_t - t - dt + 1) * robots2[k]
#                         quantity = resources2[3]
#                         if (quantity > best):
#                             best = quantity
#                             best_state = (robots2, tuple(resources2))
        
#         # Check next clay robot
#         if (costs[2][1] > robots_chosen[1]):
#             # Number of timesteps until sufficient resources are gathered.
#             dt = 1 + max(0, math.ceil((costs[1] - resources_chosen[0])/robots_chosen[0]))
#             if (t + dt <= max_t):
#                 # Update resources accordingly
#                 resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[1],
#                             resources_chosen[1] + dt * robots_chosen[1],
#                             resources_chosen[2] + dt * robots_chosen[2],
#                             resources_chosen[3] + dt * robots_chosen[3])

#                 # Update robots accordingly
#                 robots2 = (robots_chosen[0], robots_chosen[1] + 1, robots_chosen[2], robots_chosen[3])

#                 if (max(robots2) < max_bots):
#                     if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
#                         cost_matrix[robots2] = t + dt
#                         #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
#                         heapq.heappush(pq, (t + dt, robots2, resources2))

#                         resources2 = list(resources2)
#                         for k in range(4):
#                             resources2[k] += (max_t - t - dt + 1) * robots2[k]
#                         quantity = resources2[3]
#                         if (quantity > best):
#                             best = quantity
#                             best_state = (robots2, tuple(resources2))

#         # Check next ore robot
#         if (max(costs[3][0], costs[2][0], costs[1], costs[0]) > robots_chosen[0]):
#             # Number of timesteps until sufficient resources are gathered.
#             dt = 1 + max(0, math.ceil((costs[0] - resources_chosen[0])/robots_chosen[0]))
#             if (t + dt <= max_t):
#                 # Update resources accordingly
#                 resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[0],
#                             resources_chosen[1] + dt * robots_chosen[1],
#                             resources_chosen[2] + dt * robots_chosen[2],
#                             resources_chosen[3] + dt * robots_chosen[3])

#                 # Update robots accordingly
#                 robots2 = (robots_chosen[0] + 1, robots_chosen[1], robots_chosen[2], robots_chosen[3])

#                 if (max(robots2) < max_bots):
#                     if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
#                         cost_matrix[robots2] = t + dt
#                         #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
#                         heapq.heappush(pq, (t + dt, robots2, resources2))

#                         resources2 = list(resources2)
#                         for k in range(4):
#                             resources2[k] += (max_t - t - dt + 1) * robots2[k]
#                         quantity = resources2[3]
#                         if (quantity > best):
#                             best = quantity
#                             best_state = (robots2, tuple(resources2))
#     return best, best_state

# start_time = time.time()
# blueprints = open("input.txt", "r+").read().split("\n")
# sum_quality = 0
# i = 1
# T = 24
# for blueprint in blueprints:
#     blueprint = blueprint.split(" ")
#     ore_cost = int(blueprint[6])
#     clay_cost = int(blueprint[12])
#     obsidian_cost = (int(blueprint[18]), int(blueprint[21]))
#     geode_cost = (int(blueprint[27]), int(blueprint[30]))

#     score, state = extract_max(T, [ore_cost, clay_cost, obsidian_cost, geode_cost])
#     print([ore_cost, clay_cost, obsidian_cost, geode_cost])
#     print(state)
#     sum_quality += i * score
#     print(i, sum_quality)
#     print()
#     i += 1
# print(sum_quality)
# print(time.time() - start_time)

##########
# PART 2 #
##########

# Linear programming solution
def extract_max(max_t, costs, max_bots):
    best, best_state = 0, None

    # Create the cost matrix, consisting of a minimum timestep and maximized resources to get to that particular combination
    # of bots.
    cost_matrix = {}
    for a in range(1, max_bots):
        for b in range(max_bots):
            for c in range(max_bots):
                for d in range(max_bots): cost_matrix[(a, b, c, d)] = -1
    cost_matrix[(1, 0, 0, 0)] = 1

    stack = [(1, (1, 0, 0, 0), (0, 0, 0, 0))]
    while len(stack) != 0:
        # Choose the earliest timestep bot combiination
        t, robots_chosen, resources_chosen = stack.pop(-1)
        if (t > cost_matrix[robots_chosen]): continue
        # Check next geode robot
        flag = True
        
        if (robots_chosen[2] >= 1):
            # Number of timesteps until sufficient resources are gathered.
            dt1 = math.ceil((costs[3][0] - resources_chosen[0])/robots_chosen[0])
            dt2 = math.ceil((costs[3][1] - resources_chosen[2])/robots_chosen[2])
            dt = max(0, dt1, dt2) + 1
            
            if (t + dt <= max_t):
                # Update resources accordingly
                resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[3][0],
                              resources_chosen[1] + dt * robots_chosen[1],
                              resources_chosen[2] + dt * robots_chosen[2] - costs[3][1],
                              resources_chosen[3] + dt * robots_chosen[3])

                # Update robots accordingly
                robots2 = (robots_chosen[0], robots_chosen[1], robots_chosen[2], robots_chosen[3] + 1)

                if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
                    if (dt == 1): flag = False
                    cost_matrix[robots2] = t + dt
                    #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
                    stack.append((t + dt, robots2, resources2))
                    
                    resources2 = list(resources2)
                    for k in range(4):
                        resources2[k] += (max_t - t - dt + 1) * robots2[k]
                    quantity = resources2[3]
                    if (quantity > best):
                        best = quantity
                        best_state = (robots2, tuple(resources2))
        if (flag):

            # Check next obsidian robot
            if (costs[3][1] > robots_chosen[2] and robots_chosen[1] >= 1):
                # Number of timesteps until sufficient resources are gathered.
                dt1 = math.ceil((costs[2][0] - resources_chosen[0])/robots_chosen[0])
                dt2 = math.ceil((costs[2][1] - resources_chosen[1])/robots_chosen[1])
                dt = max(0, dt1, dt2) + 1

                if (t + dt <= max_t):
                    # Update resources accordingly
                    resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[2][0],
                                resources_chosen[1] + dt * robots_chosen[1] - costs[2][1],
                                resources_chosen[2] + dt * robots_chosen[2],
                                resources_chosen[3] + dt * robots_chosen[3])

                    # Update robots accordingly
                    robots2 = (robots_chosen[0], robots_chosen[1], robots_chosen[2] + 1, robots_chosen[3])

                    if (max(robots2) < max_bots):
                        if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
                            cost_matrix[robots2] = t + dt
                            #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
                            stack.append((t + dt, robots2, resources2))
                            
                            resources2 = list(resources2)
                            for k in range(4):
                                resources2[k] += (max_t - t - dt + 1) * robots2[k]
                            quantity = resources2[3]
                            if (quantity > best):
                                best = quantity
                                best_state = (robots2, tuple(resources2))
            
            # Check next clay robot
            if (costs[2][1] > robots_chosen[1]):
                # Number of timesteps until sufficient resources are gathered.
                dt = 1 + max(0, math.ceil((costs[1] - resources_chosen[0])/robots_chosen[0]))
                if (t + dt <= max_t):
                    # Update resources accordingly
                    resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[1],
                                resources_chosen[1] + dt * robots_chosen[1],
                                resources_chosen[2] + dt * robots_chosen[2],
                                resources_chosen[3] + dt * robots_chosen[3])

                    # Update robots accordingly
                    robots2 = (robots_chosen[0], robots_chosen[1] + 1, robots_chosen[2], robots_chosen[3])

                    if (max(robots2) < max_bots):
                        if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
                            cost_matrix[robots2] = t + dt
                            #print("Chosen", t + dt, robots2, resources2, "from", t, robots_chosen, resources_chosen)
                            stack.append((t + dt, robots2, resources2))

                            resources2 = list(resources2)
                            for k in range(4):
                                resources2[k] += (max_t - t - dt + 1) * robots2[k]
                            quantity = resources2[3]
                            if (quantity > best):
                                best = quantity
                                best_state = (robots2, tuple(resources2))

            # Check next ore robot
            if (max(costs[3][0], costs[2][0], costs[1], costs[0]) > robots_chosen[0]):
                # Number of timesteps until sufficient resources are gathered.
                dt = 1 + max(0, math.ceil((costs[0] - resources_chosen[0])/robots_chosen[0]))
                if (t + dt <= max_t):
                    # Update resources accordingly
                    resources2 = (resources_chosen[0] + dt * robots_chosen[0] - costs[0],
                                resources_chosen[1] + dt * robots_chosen[1],
                                resources_chosen[2] + dt * robots_chosen[2],
                                resources_chosen[3] + dt * robots_chosen[3])

                    # Update robots accordingly
                    robots2 = (robots_chosen[0] + 1, robots_chosen[1], robots_chosen[2], robots_chosen[3])

                    if (max(robots2) < max_bots):
                        if (cost_matrix[robots2] == -1 or t + dt <= cost_matrix[robots2]):
                            cost_matrix[robots2] = t + dt
                            stack.append((t + dt, robots2, resources2))

                            resources2 = list(resources2)
                            for k in range(4):
                                resources2[k] += (max_t - t - dt + 1) * robots2[k]
                            quantity = resources2[3]
                            if (quantity > best):
                                best = quantity
                                best_state = (robots2, tuple(resources2))
    return best, best_state

start_time = time.time()
blueprints = open("input.txt", "r+").read().split("\n")
sum_quality = 1
T = 32
for blueprint in blueprints[:3]:
    blueprint = blueprint.split(" ")
    ore_cost = int(blueprint[6])
    clay_cost = int(blueprint[12])
    obsidian_cost = (int(blueprint[18]), int(blueprint[21]))
    geode_cost = (int(blueprint[27]), int(blueprint[30]))

    quantity, state = extract_max(T, [ore_cost, clay_cost, obsidian_cost, geode_cost], 12)
    print([ore_cost, clay_cost, obsidian_cost, geode_cost])
    print(state)
    print()
    sum_quality *= quantity
print(sum_quality)
print(time.time() - start_time)