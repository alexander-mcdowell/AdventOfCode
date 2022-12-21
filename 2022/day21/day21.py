import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# mapping = {}
# variables = []
# for line in lines:
#     var, eq = line.split(": ")
#     eq = eq.split(" ")
#     try:
#         val = int(eq[0])  
#         mapping[var] = val
#     except Exception as _:
#         mapping[var] = eq
        
# def compute(key, mapping):
#     if (type(mapping[key]) == int): return mapping[key]
#     var1, op, var2 = mapping[key]
#     return int(eval(str(compute(var1, mapping)) + op + str(compute(var2, mapping))))

# print(compute("root", mapping))
# print(time.time() - start_time)

##########
# PART 2 #
##########

import math

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
mapping = {}
variables = []
for line in lines:
    var, eq = line.split(": ")
    eq = eq.split(" ")
    try:
        val = (int(eq[0]), 1)
        mapping[var] = val
    except Exception as _:
        mapping[var] = eq
        
def compute(key, mapping):
    if (type(key) == tuple): return key
    if (type(mapping[key]) == tuple): return mapping[key]
    var1, op, var2 = mapping[key]
    compute_var1, compute_var2 = compute(var1, mapping), compute(var2, mapping)
    if (op == "+"):
        numer = compute_var1[0] * compute_var2[1] + compute_var2[0] * compute_var1[1]
        denom = compute_var1[1] * compute_var2[1]
        g = math.gcd(numer, denom)
        return_val = (numer//g, denom//g)
    elif (op == "-"):
        numer = compute_var1[0] * compute_var2[1] - compute_var2[0] * compute_var1[1]
        denom = compute_var1[1] * compute_var2[1]
        g = math.gcd(numer, denom)
        return_val = (numer//g, denom//g)
    elif (op == "*"):
        numer = compute_var1[0] * compute_var2[0]
        denom = compute_var1[1] * compute_var2[1]
        g = math.gcd(numer, denom)
        return_val = (numer//g, denom//g)
    else:
        numer = compute_var1[0] * compute_var2[1]
        denom = compute_var1[1] * compute_var2[0]
        g = math.gcd(numer, denom)
        return_val = (numer//g, denom//g)
    return return_val

mapping["humn"] = (0, 1)
var1, _, var2 = mapping["root"]
y1 = compute(var1, mapping)
target = compute(var2, mapping)

mapping["humn"] = (1, 1)
y2 = compute(var1, mapping)

numer = y2[0] * y1[1] - y1[0] * y2[1]
denom = y2[1] * y1[1]
g = math.gcd(numer, denom)
m = (numer//g, denom//g)

numer = (target[0] * y1[1] - y1[0] * target[1]) * m[1]
denom = target[1] * y1[1] * m[0]
g = math.gcd(numer, denom)
num = (numer//g, denom//g)

print(num[0]/num[1])

print(time.time() - start_time)