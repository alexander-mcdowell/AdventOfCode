import time

##########
# PART 1 #
##########

# start_time = time.time()
# instructions = open("input.txt").read().split("\n")
# registers = {}
# inst_counter = 0
# last_played = None
# while inst_counter < len(instructions):
#     inst = instructions[inst_counter]
#     inst = inst.split(" ")
#     if (inst[0] == "snd"):
#         try:
#             last_played = int(inst[1])
#         except Exception as _:
#             last_played = registers[inst[1]]
#         inst_counter += 1
#     elif (inst[0] == "set"):
#         try:
#             registers[inst[1]] = int(inst[2])
#         except Exception as _:
#             if (inst[2] not in registers): registers[inst[2]] = 0
#             registers[inst[1]] = registers[inst[2]]
#         inst_counter += 1
#     elif (inst[0] == "add"):
#         if (inst[1] not in registers): registers[inst[1]] = 0
#         try:
#             registers[inst[1]] += int(inst[2])
#         except Exception as _:
#             if (inst[2] not in registers): registers[inst[2]] = 0
#             registers[inst[1]] += registers[inst[2]]
#         inst_counter += 1
#     elif (inst[0] == "mul"):
#         if (inst[1] not in registers): registers[inst[1]] = 0
#         try:
#             registers[inst[1]] *= int(inst[2])
#         except Exception as _:
#             if (inst[2] not in registers): registers[inst[2]] = 0
#             registers[inst[1]] *= registers[inst[2]]
#         inst_counter += 1
#     elif (inst[0] == "mod"):
#         if (inst[1] not in registers): registers[inst[1]] = 0
#         try:
#             registers[inst[1]] %= int(inst[2])
#         except Exception as _:
#             registers[inst[1]] %= registers[inst[2]]
#         inst_counter += 1
#     elif (inst[0] == "rcv"):
#         try:
#             a = int(inst[1])
#         except Exception as _:
#             a = registers[inst[1]]
#         if (a != 0):
#             print(last_played)
#             break
#         inst_counter += 1
#     else:
#         try:
#             a = int(inst[1])
#         except Exception as _:
#             if (inst[1] not in registers): registers[inst[1]] = 0
#             a = registers[inst[1]]
#         if (a > 0):
#             try:
#                 b = int(inst[2])
#             except Exception as _:
#                 if (inst[2] not in registers): registers[inst[2]] = 0
#                 b = registers[inst[2]]
#             inst_counter += b
#         else: inst_counter += 1
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
instructions = open("input.txt").read().split("\n")

receive1, receive2 = [], []
registers1, registers2 = {'p': 0}, {'p': 1}
inst_counter1, inst_counter2 = 0, 0
count = 0
while True:
    should_end = True
    while inst_counter1 < len(instructions):
        inst = instructions[inst_counter1]
        inst = inst.split(" ")
        if (inst[0] == "snd"):
            try:
                to_send = int(inst[1])
            except Exception as _:
                to_send = registers1[inst[1]]
            receive2.append(to_send)
            should_end = False
            inst_counter1 += 1
        elif (inst[0] == "set"):
            try:
                registers1[inst[1]] = int(inst[2])
            except Exception as _:
                if (inst[2] not in registers1): registers1[inst[2]] = 0
                registers1[inst[1]] = registers1[inst[2]]
            inst_counter1 += 1
            should_end = False
        elif (inst[0] == "add"):
            if (inst[1] not in registers1): registers1[inst[1]] = 0
            try:
                registers1[inst[1]] += int(inst[2])
            except Exception as _:
                if (inst[2] not in registers1): registers1[inst[2]] = 0
                registers1[inst[1]] += registers1[inst[2]]
            inst_counter1 += 1
            should_end = False
        elif (inst[0] == "mul"):
            if (inst[1] not in registers1): registers1[inst[1]] = 0
            try:
                registers1[inst[1]] *= int(inst[2])
            except Exception as _:
                if (inst[2] not in registers1): registers1[inst[2]] = 0
                registers1[inst[1]] *= registers1[inst[2]]
            inst_counter1 += 1
            should_end = False
        elif (inst[0] == "mod"):
            if (inst[1] not in registers1): registers1[inst[1]] = 0
            try:
                registers1[inst[1]] %= int(inst[2])
            except Exception as _:
                registers1[inst[1]] %= registers1[inst[2]]
            inst_counter1 += 1
            should_end = False
        elif (inst[0] == "rcv"):
            if (len(receive1) == 0): break
            registers1[inst[1]] = receive1.pop(0)
            inst_counter1 += 1
            should_end = False
        else:
            try:
                a = int(inst[1])
            except Exception as _:
                if (inst[1] not in registers1): registers1[inst[1]] = 0
                a = registers1[inst[1]]
            if (a > 0):
                try:
                    b = int(inst[2])
                except Exception as _:
                    if (inst[2] not in registers1): registers1[inst[2]] = 0
                    b = registers1[inst[2]]
                inst_counter1 += b
            else: inst_counter1 += 1
            should_end = False
    
    while inst_counter2 < len(instructions):
        inst = instructions[inst_counter2]
        inst = inst.split(" ")
        if (inst[0] == "snd"):
            try:
                to_send = int(inst[1])
            except Exception as _:
                to_send = registers2[inst[1]]
            receive1.append(to_send)
            inst_counter2 += 1
            should_end = False
            count += 1
        elif (inst[0] == "set"):
            try:
                registers2[inst[1]] = int(inst[2])
            except Exception as _:
                if (inst[2] not in registers2): registers2[inst[2]] = 0
                registers2[inst[1]] = registers2[inst[2]]
            inst_counter2 += 1
            should_end = False
        elif (inst[0] == "add"):
            if (inst[1] not in registers2): registers2[inst[1]] = 0
            try:
                registers2[inst[1]] += int(inst[2])
            except Exception as _:
                if (inst[2] not in registers1): registers2[inst[2]] = 0
                registers2[inst[1]] += registers2[inst[2]]
            inst_counter2 += 1
            should_end = False
        elif (inst[0] == "mul"):
            if (inst[1] not in registers2): registers2[inst[1]] = 0
            try:
                registers2[inst[1]] *= int(inst[2])
            except Exception as _:
                if (inst[2] not in registers2): registers2[inst[2]] = 0
                registers2[inst[1]] *= registers2[inst[2]]
            inst_counter2 += 1
            should_end = False
        elif (inst[0] == "mod"):
            if (inst[1] not in registers2): registers2[inst[1]] = 0
            try:
                registers2[inst[1]] %= int(inst[2])
            except Exception as _:
                registers2[inst[1]] %= registers2[inst[2]]
            inst_counter2 += 1
            should_end = False
        elif (inst[0] == "rcv"):
            if (len(receive2) == 0): break
            registers2[inst[1]] = receive2.pop(0)
            inst_counter2 += 1
            should_end = False
        else:
            try:
                a = int(inst[1])
            except Exception as _:
                if (inst[1] not in registers2): registers2[inst[1]] = 0
                a = registers2[inst[1]]
            if (a > 0):
                try:
                    b = int(inst[2])
                except Exception as _:
                    if (inst[2] not in registers2): registers2[inst[2]] = 0
                    b = registers2[inst[2]]
                inst_counter2 += b
            else: inst_counter2 += 1
            should_end = False
    
    if (should_end): break

print(count)
print(time.time() - start_time)