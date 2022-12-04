##########
# PART 1 #
##########

"""
data = open("day1in.txt").read().split("\n")[0]
stack = []
for c in data:
    if (c == ")" and (len(stack) > 0 and stack[-1] == "(")): stack.pop(-1)
    else: stack.append(c)
print(stack.count("(") - stack.count(")"))
"""

##########
# PART 2 #
##########

data = open("day1in.txt").read().split("\n")[0]
stack = []
floor = 0
for i in range(len(data)):
    c = data[i]
    if (floor < 0):
        print(i)
        break
    if (c == ")" and (len(stack) > 0 and stack[-1] == "(")): floor -= 1
    else:
        if (c == ")"): floor -= 1
        else: floor += 1
        stack.append(c)