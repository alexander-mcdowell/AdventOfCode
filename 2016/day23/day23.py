##########
# PART 1 #
##########

"""
data = open("day23in.txt").read().split("\n")
instructions = []
for inst in data: instructions.append(inst.split(" "))

registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
line_counter = 0
while (line_counter < len(instructions)):
    inst = instructions[line_counter]
    if (inst[0] == "cpy"):
        if (type(inst[2]) == str):
            try: registers[inst[2]] = int(inst[1])
            except Exception as _: registers[inst[2]] = registers[inst[1]]
        line_counter += 1
    elif (inst[0] == "inc"):
        registers[inst[1]] += 1
        line_counter += 1
    elif (inst[0] == "dec"):
        registers[inst[1]] -= 1
        line_counter += 1
    elif (inst[0] == "jnz"):
        try: arg1 = int(inst[1])
        except Exception as _: arg1 = registers[inst[1]]
        try:  arg2 = int(inst[2])
        except Exception as _: arg2 = registers[inst[2]]

        if (arg1 != 0): line_counter += arg2
        else: line_counter += 1
    elif (inst[0] == "tgl"):
        try: arg = int(inst[1])
        except Exception as _: arg = registers[inst[1]]
        
        if (line_counter + arg < len(instructions)):
            toggled = instructions[line_counter + arg]
            if (len(toggled) == 2):
                if (toggled[0] == "inc"): instructions[line_counter + arg][0] = "dec"
                else: instructions[line_counter + arg][0] = "inc"
            elif (len(toggled) == 3):
                if (toggled[0] == "jnz"): instructions[line_counter + arg][0] = "cpy"
                else: instructions[line_counter + arg][0] = "jnz"
        line_counter += 1
print(registers['a'])
"""

##########
# PART 2 #
##########

# After testing inputs, the program appears to compute the factorial of the value in 'a' plus 73 * 90.

# 12
# 12 * 11 = 132
# 12 * 11 * 10 = 1320
# 12 * 11 * 10 * 9 = 11880
# 12 * 11 * 10 * 9 * 8 = 95040
# 12 * 11 * 10 * 9 * 8 * 7 = 665280
# 12 * 11 * 10 * 9 * 8 * 7 * 6 = 3991680
# ...

# Code used.
"""
data = open("day23in.txt").read().split("\n")
instructions = []
for inst in data: instructions.append(inst.split(" "))

registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
line_counter = 0
while (line_counter < len(instructions)):
    #if (line_counter == 11): print(registers['a'])
    inst = instructions[line_counter]
    print(line_counter, inst, registers)
    if (inst[0] == "cpy"):
        if (type(inst[2]) == str):
            try: registers[inst[2]] = int(inst[1])
            except Exception as _: registers[inst[2]] = registers[inst[1]]
        line_counter += 1
    elif (inst[0] == "inc"):
        registers[inst[1]] += 1
        line_counter += 1
    elif (inst[0] == "dec"):
        registers[inst[1]] -= 1
        line_counter += 1
    elif (inst[0] == "mul"):
        try:  arg = int(inst[2])
        except Exception as _: arg = registers[inst[2]]
        registers[inst[1]] *= arg
        line_counter += 1
    elif (inst[0] == "jnz"):
        try: arg1 = int(inst[1])
        except Exception as _: arg1 = registers[inst[1]]
        try:  arg2 = int(inst[2])
        except Exception as _: arg2 = registers[inst[2]]

        if (arg1 != 0): line_counter += arg2
        else: line_counter += 1
    elif (inst[0] == "tgl"):
        try: arg = int(inst[1])
        except Exception as _: arg = registers[inst[1]]
        
        if (line_counter + arg < len(instructions)):
            toggled = instructions[line_counter + arg]
            if (len(toggled) == 2):
                if (toggled[0] == "inc"): instructions[line_counter + arg][0] = "dec"
                else: instructions[line_counter + arg][0] = "inc"
            elif (len(toggled) == 3):
                if (toggled[0] == "jnz"): instructions[line_counter + arg][0] = "cpy"
                else: instructions[line_counter + arg][0] = "jnz"
        line_counter += 1
print(registers['a'])
"""