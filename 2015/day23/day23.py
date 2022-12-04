##########
# PART 1 #
##########

"""
instructions = open("day23in.txt").read().split("\n")
i = 0
registers = {}
while (i < len(instructions)):
    instruction = instructions[i].split(' ')
    if (instruction[0] == "hlf"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] //= 2
        i += 1
    elif (instruction[0] == "tpl"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] *= 3
        i += 1
    elif (instruction[0] == "inc"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] += 1
        i += 1
    elif (instruction[0] == "jmp"):
        i += int(instruction[1])
    elif (instruction[0] == "jie"):
        instruction[1] = instruction[1][:-1]
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        if (registers[instruction[1]] % 2 == 0): i += int(instruction[2])
        else: i += 1
    elif (instruction[0] == "jio"):
        instruction[1] = instruction[1][:-1]
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        if (registers[instruction[1]] == 1): i += int(instruction[2])
        else: i += 1
print(registers['b'])
"""

##########
# PART 2 #
##########

instructions = open("day23in.txt").read().split("\n")
i = 0
registers = {'a': 1}
while (i < len(instructions)):
    instruction = instructions[i].split(' ')
    if (instruction[0] == "hlf"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] //= 2
        i += 1
    elif (instruction[0] == "tpl"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] *= 3
        i += 1
    elif (instruction[0] == "inc"):
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        registers[instruction[1]] += 1
        i += 1
    elif (instruction[0] == "jmp"):
        i += int(instruction[1])
    elif (instruction[0] == "jie"):
        instruction[1] = instruction[1][:-1]
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        if (registers[instruction[1]] % 2 == 0): i += int(instruction[2])
        else: i += 1
    elif (instruction[0] == "jio"):
        instruction[1] = instruction[1][:-1]
        if (instruction[1] not in registers): registers[instruction[1]] = 0
        if (registers[instruction[1]] == 1): i += int(instruction[2])
        else: i += 1
print(registers['b'])