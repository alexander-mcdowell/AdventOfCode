import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# registers = {}
# for line in lines:
#     var1, op1, offset, _, var2, op2, compare = line.split(" ")
#     offset = int(offset)
    
#     if (var1 not in registers): registers[var1] = 0
#     if (var2 not in registers): registers[var2] = 0

#     if (eval(str(registers[var2]) + op2 + compare)):
#         if (op1 == "inc"): registers[var1] += offset
#         else: registers[var1] -= offset
# print(max([registers[k] for k in registers]))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
registers = {}
best = None
for line in lines:
    var1, op1, offset, _, var2, op2, compare = line.split(" ")
    offset = int(offset)
    
    if (var1 not in registers): registers[var1] = 0
    if (var2 not in registers): registers[var2] = 0

    if (eval(str(registers[var2]) + op2 + compare)):
        if (op1 == "inc"): registers[var1] += offset
        else: registers[var1] -= offset
    
    if (best == None or registers[var1] > best): best = registers[var1]
print(best)
print(time.time() - start_time)