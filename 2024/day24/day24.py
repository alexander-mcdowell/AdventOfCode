import time

# ##########
# # PART 1 #
# ##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
variables = {}
rules = {}
outputs = {}
mode = 0
for l in data:
    if (l == ""): mode = 1 - mode
    elif (mode == 0):
        var, val = l.split(": ")
        val = int(val)
        variables[var] = val
    else:
        s, z = l.split(" -> ")
        x, op, y = s.split(" ")
        rules[z] = (x, op, y)
        variables[z] = -1
        outputs[z] = -1

i = 0
unassigned = [x for x in variables if variables[x] == -1]

def evaluate(z):
    global unassigned, rules, variables
    if (variables[z] != -1): return variables[z]
    x, op, y = rules[z]
    if (op == 'AND'): z_val = evaluate(x) & evaluate(y)
    elif (op == 'OR'): z_val = evaluate(x) | evaluate(y)
    else: z_val = evaluate(x) ^ evaluate(y)
    outputs[z] = z_val
    variables[z] = z_val
    unassigned.remove(z)
    return z_val

while len(unassigned) != 0: evaluate(unassigned[0])
total = 0
for x in sorted(outputs, reverse=True):
    if (x[0] == 'z'): total = 2 * total + outputs[x]
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

# ##########
# # PART 2 #
# ##########

# Full Adder
# A + B + C_in = S with carry C_out
# X1 = A XOR B
# S = X1 XOR C_in
# X2 = X1 AND C_in
# X3 = A AND B
# C_out = X2 OR X3

# S = (A XOR B) XOR C_in
# C_out = ((A XOR B) AND C_in) OR (A AND B)

# Problems found:

# z05 ('y05', 'AND', 'x05') ==> z05 and dkr swapped
# x05 XOR y05 = hdc, hdc XOR gcs = dkr, gcs is likely carry so dkr and z05 are swapped

# z15 ('sth', 'AND', 'bhw') ==> z15 and htp swapped
# sth is in_carry and bhw is X1, this tracks since x15 XOR y15 = bhw
# bhw XOR sth = htp
# x15 AND y15 = hhb and hbb OR htp = mqr so mqr is out_carry and htp is the sum.
# htp and z15 are swapped

# z20 ('qfj', 'OR', 'mqg') ==> z20 and hhh swapped
# mvv AND fvm = qfj so qfj is X2. x20 AND y20 = mqg so mqg is X3
# x20 XOR y20 = mvv so mvv is X1
# mvv XOR fvm = hhh so z20 and hhh are swapped

swaps = [('z05', 'dkr'), ('z15', 'htp'), ('z20', 'hhh'), ('rhv', 'ggk')]
swap_dict = {}
for x in swaps:
    swap_dict[x[0]] = x[1]
    swap_dict[x[1]] = x[0]

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
variables = {}
rules = {}
outputs = {}
mode = 0
for l in data:
    if (l == ""): mode = 1 - mode
    elif (mode == 0):
        var, val = l.split(": ")
        val = int(val)
        variables[var] = val
    else:
        s, z = l.split(" -> ")
        x, op, y = s.split(" ")
        if (z in swap_dict): z = swap_dict[z]
        rules[z] = (x, op, y)
        variables[z] = -1
        outputs[z] = -1

i = 0
unassigned = [x for x in variables if variables[x] == -1]
u = 'x34'
variables[u] = 1 - variables[u]

# x36 flip causes problems
# x36 XOR y36 = rhv, ggk XOR hpg -> z36 so rhv and ggk are swapped?

def evaluate(z):
    global unassigned, rules, variables
    if (variables[z] != -1): return variables[z]
    x, op, y = rules[z]
    if (op == 'AND'): z_val = evaluate(x) & evaluate(y)
    elif (op == 'OR'): z_val = evaluate(x) | evaluate(y)
    else: z_val = evaluate(x) ^ evaluate(y)
    outputs[z] = z_val
    variables[z] = z_val
    unassigned.remove(z)
    return z_val

while len(unassigned) != 0: evaluate(unassigned[0])
total = 0
x_str = "".join([str(variables[x]) for x in sorted(variables, reverse=True) if x[0] == 'x'])
y_str = "".join([str(variables[y]) for y in sorted(variables, reverse=True) if y[0] == 'y'])
z_str = "".join([str(outputs[z]) for z in sorted(variables, reverse=True) if z[0] == 'z'])
print(int(x_str, 2) + int(y_str, 2) == int(z_str, 2))
print(" " + x_str, int(x_str, 2))
print(" " + y_str, int(y_str, 2))
print(z_str, int(z_str, 2))
print(bin(int(x_str, 2) + int(y_str, 2))[2:], int(x_str, 2) + int(y_str, 2))
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

swapped = []
for x in swaps: swapped.append(x[0]); swapped.append(x[1])
print(",".join(sorted(swapped)))