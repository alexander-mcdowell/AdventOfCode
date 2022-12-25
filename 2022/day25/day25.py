##########
# PART 1 #
##########

import time
import math

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
S = 0
for line in lines:
    decimal = 0
    n = len(line)
    val = 0
    x = 1
    for i in range(n - 1, -1, -1):
        if (line[i] == '-'): val += x * -1
        elif (line[i] == '='): val += x * -2
        else: val += x * int(line[i])
        x *= 5
    S += val

def to_snafu(n):
    k = 5 ** int(math.log(n)/math.log(5))
    s = ""
    while k != 0:
        s += str(n//k)
        n %= k
        k //= 5
    t = ""
    carry = 0
    for i in range(len(s) - 1, -1, -1):
        x = int(s[i]) + carry
        if (x == 3):
            t = '=' + t
            carry = 1
        elif (x == 4):
            t = '-' + t
            carry = 1
        elif (x == 5):
            t = '0' + t
            carry = 1
        else:
            t = str(x) + t
            carry = 0
    if (carry != 0): t = str(carry) + t
    return t

print(to_snafu(S))
print(time.time() - start_time)

##########
# PART 2 #
##########