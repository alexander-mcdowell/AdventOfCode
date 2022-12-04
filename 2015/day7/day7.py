##########
# PART 1 #
##########

"""
import numpy as np

data = open("day7in.txt").read().split("\n")
var_map = {}

while (len(data) != 0):
    inst = data.pop(0)
    operation, dest = inst.split(" -> ")
    
    try:
        try:
            # Integer assignment
            var_map[dest] = int(operation)
        except Exception as _:
            operation = operation.split(" ")
            
            # Direct variable assignment
            if (len(operation) == 1):
                arg = var_map[operation[0]]
                var_map[dest] = arg
            # NOT
            elif (len(operation) == 2):
                try:
                    arg = int(operation[1])
                except Exception as _:
                    arg = var_map[operation[1]]
                var_map[dest] = np.array([~arg], dtype = "uint16")[0]
            # Other
            elif (len(operation) == 3):
                # Parse arguments
                try:
                    arg1 = int(operation[0])
                except Exception as _:
                    arg1 = var_map[operation[0]]
                try:
                    arg2 = int(operation[2])
                except Exception as _:
                    arg2 = var_map[operation[2]]

                if (operation[1] == "AND"): var_map[dest] = np.array([arg1 & arg2], dtype = "uint16")[0]
                elif (operation[1] == "OR"): var_map[dest] = np.array([arg1 | arg2], dtype = "uint16")[0]
                elif (operation[1] == "LSHIFT"): var_map[dest] = np.array([arg1 << arg2], dtype = "uint16")[0]
                elif (operation[1] == "RSHIFT"): var_map[dest] = np.array([arg1 >> arg2], dtype = "uint16")[0]
    except Exception as _:
        data.append(inst)

print(var_map["a"])
"""

##########
# PART 1 #
##########

import numpy as np

data = open("day7in.txt").read().split("\n")
instruct = [x for x in data]
var_map = {}

# First pass
while (len(instruct) != 0):
    inst = instruct.pop(0)
    operation, dest = inst.split(" -> ")
    
    try:
        try:
            # Integer assignment
            var_map[dest] = int(operation)
        except Exception as _:
            operation = operation.split(" ")
            
            # Direct variable assignment
            if (len(operation) == 1):
                arg = var_map[operation[0]]
                var_map[dest] = arg
            # NOT
            elif (len(operation) == 2):
                try:
                    arg = int(operation[1])
                except Exception as _:
                    arg = var_map[operation[1]]
                var_map[dest] = np.array([~arg], dtype = "uint16")[0]
            # Other
            elif (len(operation) == 3):
                # Parse arguments
                try:
                    arg1 = int(operation[0])
                except Exception as _:
                    arg1 = var_map[operation[0]]
                try:
                    arg2 = int(operation[2])
                except Exception as _:
                    arg2 = var_map[operation[2]]

                if (operation[1] == "AND"): var_map[dest] = np.array([arg1 & arg2], dtype = "uint16")[0]
                elif (operation[1] == "OR"): var_map[dest] = np.array([arg1 | arg2], dtype = "uint16")[0]
                elif (operation[1] == "LSHIFT"): var_map[dest] = np.array([arg1 << arg2], dtype = "uint16")[0]
                elif (operation[1] == "RSHIFT"): var_map[dest] = np.array([arg1 >> arg2], dtype = "uint16")[0]
    except Exception as _:
        instruct.append(inst)

a_final = var_map["a"]

instruct = [x for x in data]
var_map = {}

# Second pass
while (len(instruct) != 0):
    inst = instruct.pop(0)
    operation, dest = inst.split(" -> ")
    
    try:
        try:
            # Integer assignment
            if (dest == "b"): var_map["b"] = a_final
            else: var_map[dest] = int(operation)
        except Exception as _:
            operation = operation.split(" ")
            
            # Direct variable assignment
            if (len(operation) == 1):
                arg = var_map[operation[0]]
                var_map[dest] = arg
            # NOT
            elif (len(operation) == 2):
                try:
                    arg = int(operation[1])
                except Exception as _:
                    arg = var_map[operation[1]]
                var_map[dest] = np.array([~arg], dtype = "uint16")[0]
            # Other
            elif (len(operation) == 3):
                # Parse arguments
                try:
                    arg1 = int(operation[0])
                except Exception as _:
                    arg1 = var_map[operation[0]]
                try:
                    arg2 = int(operation[2])
                except Exception as _:
                    arg2 = var_map[operation[2]]

                if (operation[1] == "AND"): var_map[dest] = np.array([arg1 & arg2], dtype = "uint16")[0]
                elif (operation[1] == "OR"): var_map[dest] = np.array([arg1 | arg2], dtype = "uint16")[0]
                elif (operation[1] == "LSHIFT"): var_map[dest] = np.array([arg1 << arg2], dtype = "uint16")[0]
                elif (operation[1] == "RSHIFT"): var_map[dest] = np.array([arg1 >> arg2], dtype = "uint16")[0]
    except Exception as _:
        instruct.append(inst)

print(var_map["a"])