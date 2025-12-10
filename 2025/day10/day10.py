##########
# PART 1 #
##########

import timeit
from collections import deque

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
total_presses = 0
for l in data:
    split_data = l.split(" ")
    buttons = []
    for i in range(len(split_data)-1):
        if i == 0:
            target = tuple(0 if c=="." else 1 for c in split_data[i][1:-1])
        else:
            buttons.append([int(x) for x in split_data[i][1:-1].split(",")])
    
    queue = deque()
    queue.append([0, tuple(0 for _ in range(len(target)))])
    seen = set()
    best = None
    while len(queue) != 0:
        presses, state = queue.popleft()
        if state==target:
            best = presses
            break

        seen.add(state)
        for button in buttons:
            new_state = [x for x in state]
            for i in button: new_state[i] = 1-state[i]
            new_state = tuple(new_state)
            if new_state not in seen:
                queue.append([presses + 1, new_state])
    total_presses += best

print(total_presses)    
print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

from scipy.optimize import milp, LinearConstraint
import numpy as np

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
total_presses = 0
for l in data:
    split_data = l.split(" ")
    joltage_requirements = np.asarray([int(x) for x in split_data[-1][1:-1].split(",")])
    num_buttons = len(split_data)-2
    button_matrix = np.zeros((len(joltage_requirements), num_buttons))
    
    for i in range(1, len(split_data)-1):
        for x in split_data[i][1:-1].split(","):
            button_matrix[int(x)][i-1] = 1

    button_matrix = np.asarray(button_matrix)
    c = np.asarray([1 for _ in range(num_buttons)])
    constraint = LinearConstraint(button_matrix, joltage_requirements, joltage_requirements)
    
    result = milp(c, integrality=1, constraints=constraint)
    total_presses += round(result.fun)

print(total_presses)    
print(timeit.default_timer() - start_time)