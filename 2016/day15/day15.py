##########
# PART 1 #
##########

"""
data = open("day15in.txt").read().split("\n")
discs = []
for line in data:
    line = line.split(" ")
    discs.append((int(line[3]), int(line[11][:-1])))

# Naive approach
time = 0
while (True):
    valid = True
    for i in range(len(discs)):
        if ((time + i + 1 + discs[i][1]) % discs[i][0] != 0):
            valid = False
            break
    if (valid):
        print(time)
        break
    time += 1
"""

##########
# PART 2 #
##########

data = open("day15in.txt").read().split("\n")
discs = []
for line in data:
    line = line.split(" ")
    discs.append((int(line[3]), int(line[11][:-1])))
discs.append((11, 0))

# The naive approach still works, but here is a better solution:
# Each of the discs is a set of modular equations.
# Disc 1: (time + pos1 + 1) % positions1 = 0
# Disc 2: (time + pos2 + 2) % positions2 = 0
# Disc 3: (time + pos3 + 3) % positions3 = 0
# and so on...

# Rearranging:
# Disc 1: time % positions1 = (-pos1 - 1) % positions1
# Disc 2: time % positions2 = (-pos2 - 1) % positions2
# Disc 3: time % positions3 = (-pos3 - 1) % positions3
# and so on...
# We are trying to find the value time that satisfies all of these modular equations.
# To do this, we can use the Chinese Remainder Theorem.

# For the following n equations:
# x = a1 % m1
# x = a2 % m2
# x = a3 % m3
# ...
# x = a[n] % m[n]
# The solution x is x = (a1 * b1 * b1_inv + a2 * b2 * b2_inv + ... a[n] * b[n] * b1[n]_inv) % M
# Where M = m1 * m2 * m3 * ... * m[n], b[i] = M / m[i], and b[i]_inv = (b[i]^-1) mod m[i]

# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def euclid_gcd(a, b):
    if (a == 0): return (b, 0, 1)
    else:
        g, y, x = euclid_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inv(a, m):
    g, x, _ = euclid_gcd(a, m)
    if (g != 1): return None
    return x % m

M = 1
for x in discs: M *= x[0]
a, b, b_inv = [], [], []
for i in range(len(discs)):
    a.append(-((i + 1) + discs[i][1]) % discs[i][0])
    b.append(M // discs[i][0])
    b_inv.append(mod_inv(b[-1], discs[i][0]))
time = 0
for i in range(len(discs)): time += a[i] * b[i] * b_inv[i]
time %= M
print(time)