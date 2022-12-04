##########
# PART 1 #
##########

data = open("day25in.txt").read().split("\n")
instructions = []
for inst in data: instructions.append(inst.split(" "))

a = 1
while (True):
    print(a)
    registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    line_counter = 0
    last = -1
    while (line_counter < len(instructions)):
        inst = instructions[line_counter]
        if (line_counter == last): break
        last = line_counter
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
    a += 1
print(a)

##########
# PART 2 #
##########

# There is no puzzle for part 2.