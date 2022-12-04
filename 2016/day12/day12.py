##########
# PART 1 #
##########

"""
day12 = open("day12in.txt").read().split("\n")
instructions = []
for inst in day12: instructions.append(inst.split(" "))

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
line_counter = 0
while (line_counter < len(instructions)):
    inst = instructions[line_counter]
    if (inst[0] == "cpy"):
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
print(registers['a'])
"""

##########
# PART 2 #
##########

# You could probably deassemble the sample input to more efficiently solve the problem.

day12 = open("day12in.txt").read().split("\n")
instructions = []
for inst in day12: instructions.append(inst.split(" "))

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
line_counter = 0
while (line_counter < len(instructions)):
    inst = instructions[line_counter]
    if (inst[0] == "cpy"):
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
print(registers['a'])