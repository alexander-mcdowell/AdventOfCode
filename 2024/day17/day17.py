import time
import sys

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
A = int(data[0].split(": ")[1])
B = int(data[1].split(": ")[1])
C = int(data[2].split(": ")[1])
program = [int(x) for x in data[4].split(": ")[1].split(",")]
i = 0
while i < len(program):
    op, param = program[i], program[i + 1]
    # adv
    if (op == 0):
        i += 2
        if (param == 7): continue
        if (param < 4): x = param
        elif (param == 4): x = A
        elif (param == 5): x = B
        else: x = C
        A //= pow(2, x)
    # bxl
    elif (op == 1):
        B = B ^ param
        i += 2
    # bst
    elif (op == 2):
        i += 2
        if (param == 7): continue
        if (param < 4): x = param
        elif (param == 4): x = A
        elif (param == 5): x = B
        else: x = C
        B = x % 8
    # jnz
    elif (op == 3):
        if (A == 0):
            i += 2
            continue
        else: i = param
    # bxc
    elif (op == 4):
        B = B ^ C
        i += 2
    # out
    elif (op == 5):
        i += 2
        if (param == 7): continue
        if (param < 4): x = param
        elif (param == 4): x = A
        elif (param == 5): x = B
        else: x = C
        print(x % 8, end = ",")
    # bdv
    elif (op == 6):
        i += 2
        if (param == 7): continue
        if (param < 4): x = param
        elif (param == 4): x = A
        elif (param == 5): x = B
        else: x = C
        B = A // pow(2, x)
    # cdv
    else:
        i += 2
        if (param == 7): continue
        if (param < 4): x = param
        elif (param == 4): x = A
        elif (param == 5): x = B
        else: x = C
        C = A // pow(2, x)
print()
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

# Program
# 2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0

def getOutput(A):
    output = []
    while True:
        B = A & 7              # B = last three digits of A
        B = B ^ 2              # invert 2nd digit of B
        C = (A >> B) & 7
        B = B ^ C
        B = B ^ 3              # invert first two digits of B
        output.append(B & 7)   # Print last 3 digits
        A = A >> 3             # Shift A over by 3 digits
        if (A == 0): break
    return output

# A = 0
# target = [5]
# for x in target[::-1]:
#     B = x ^ 3
    
#     A2 = A
#     B2 = B
#     C = 0
#     while True:
#         A = A2
#         B = B2
        
#         B = B ^ C
#         X = C << B
#         B = B ^ 2
#         A ^= B
#         if (A >= X ^ B and (A >> (B^2)) == C): break
#         C += 1

#     B = B ^ 2
#     print(A2, B, C)
#     A = A2 ^ B
# print("Min value for " + str(target) + ": " + str(A))
# print("Actual:", getOutput(A))