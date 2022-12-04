##########
# PART 1 #
##########

"""
data = open("day10in.txt").read().split("\n")
instructions = []
for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "value"):
        # Type 0 == give value
        instructions.append((0, int(inst[1]), int(inst[5])))
    elif (inst[0] == "bot"):
        # Type 1 == give low and high to output
        if (inst[5] == "output" and inst[10] == "output"):
            instructions.append((1, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 2 == give low to output and high to robot
        elif (inst[5] == "output" and inst[10] != "output"):
            instructions.append((2, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 3 == give low to robot and high to output
        elif (inst[5] != "output" and inst[10] == "output"):
            instructions.append((3, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 4 == give low and high to robots
        else:
            instructions.append((4, int(inst[1]), int(inst[6]), int(inst[11])))
bots = {}
outputs = {}
low_val, high_val = 17, 61
while (len(instructions) != 0):
    inst = instructions.pop(0)
    if (inst[0] == 0):
        if (inst[2] not in bots): bots[inst[2]] = []
        bots[inst[2]] = sorted(bots[inst[2]] + [inst[1]])
    else:
        if (inst[1] in bots and len(bots[inst[1]]) == 2):
            if (inst[2] not in bots): bots[inst[2]] = []
            if (inst[3] not in bots): bots[inst[3]] = []
            
            if (bots[inst[1]][0] == low_val and bots[inst[1]][1] == high_val):
                print(inst[1])
                break
            
            if (inst[0] == 1):
                outputs[inst[2]] = bots[inst[1]][0]
                outputs[inst[3]] = bots[inst[1]][1]
            elif (inst[0] == 2):
                outputs[inst[2]] = bots[inst[1]][0]
                bots[inst[3]] = sorted(bots[inst[3]] + [bots[inst[1]][1]])
            elif (inst[0] == 3):
                bots[inst[2]] = sorted(bots[inst[2]] + [bots[inst[1]][0]])
                outputs[inst[3]] = bots[inst[1]][1]
            else:
                bots[inst[2]] = sorted(bots[inst[2]] + [bots[inst[1]][0]])
                bots[inst[3]] = sorted(bots[inst[3]] + [bots[inst[1]][1]])
            bots[inst[1]] = []
        else: instructions.append(inst)
"""

##########
# PART 2 #
##########

data = open("day10in.txt").read().split("\n")
instructions = []
for inst in data:
    inst = inst.split(" ")
    if (inst[0] == "value"):
        # Type 0 == give value
        instructions.append((0, int(inst[1]), int(inst[5])))
    elif (inst[0] == "bot"):
        # Type 1 == give low and high to output
        if (inst[5] == "output" and inst[10] == "output"):
            instructions.append((1, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 2 == give low to output and high to robot
        elif (inst[5] == "output" and inst[10] != "output"):
            instructions.append((2, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 3 == give low to robot and high to output
        elif (inst[5] != "output" and inst[10] == "output"):
            instructions.append((3, int(inst[1]), int(inst[6]), int(inst[11])))
        # Type 4 == give low and high to robots
        else:
            instructions.append((4, int(inst[1]), int(inst[6]), int(inst[11])))
bots = {}
outputs = {}
low_val, high_val = 17, 61
while (len(instructions) != 0):
    inst = instructions.pop(0)
    if (inst[0] == 0):
        if (inst[2] not in bots): bots[inst[2]] = []
        bots[inst[2]] = sorted(bots[inst[2]] + [inst[1]])
    else:
        if (inst[1] in bots and len(bots[inst[1]]) == 2):
            if (inst[2] not in bots): bots[inst[2]] = []
            if (inst[3] not in bots): bots[inst[3]] = []
            
            if (inst[0] == 1):
                outputs[inst[2]] = bots[inst[1]][0]
                outputs[inst[3]] = bots[inst[1]][1]
            elif (inst[0] == 2):
                outputs[inst[2]] = bots[inst[1]][0]
                bots[inst[3]] = sorted(bots[inst[3]] + [bots[inst[1]][1]])
            elif (inst[0] == 3):
                bots[inst[2]] = sorted(bots[inst[2]] + [bots[inst[1]][0]])
                outputs[inst[3]] = bots[inst[1]][1]
            else:
                bots[inst[2]] = sorted(bots[inst[2]] + [bots[inst[1]][0]])
                bots[inst[3]] = sorted(bots[inst[3]] + [bots[inst[1]][1]])
            bots[inst[1]] = []
        else: instructions.append(inst)
print(outputs[0] * outputs[1] * outputs[2])