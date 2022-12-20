##########
# PART 1 #
##########

"""
import numpy as np

# Prime sieve courtesy of stack overflow https://stackoverflow.com/a/2068548
def sieve(n):
    primes = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if primes[i]:
            k=3*i+1|1
            primes[       k*k//3     ::2*k] = False
            primes[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(primes)[0][1:]+1)|1)]

def factor(n, primes):
    factors, powers = [], []
    for p in primes:
        if (p > n): break
        power = 0
        while (n % p == 0):
            n //= p
            power += 1
        if (power > 0):
            factors.append(p)
            powers.append(power)
    return factors, powers

def divisor_sum(factors, powers):
    # The divisor sum of a number n with factorization n = (p1)^(k1) * (p2)^(k2) * (p3)^(k3) * ...
    # is (1 + p1 + p1^2 + ... + p1^k1) * (1 + p2 + p2^2 + ... + p2^k2) * ...
    # This is because expanding this out yields every possible product of the powers of the prime factors.
    # We then use the geometric sum formula for 1 + r + r^2 + r^3 + ... + r^n = (r^(n + 1) - 1) / (r - 1)
    # to simplify the formula.
    
    ds = 1
    for i in range(len(factors)):
        ds *= (factors[i] ** (powers[i] + 1) - 1) // (factors[i] - 1)
    return ds

threshold = int(open("day20in.txt").read().split("\n")[0])
primes = sieve(10 ** 7)

house_num = 10 ** 5
while (True):
    f, p = factor(house_num, primes)
    x = divisor_sum(f, p)
    if (10 * x >= threshold):
        print(house_num)
        break
    house_num += 1
"""

##########
# PART 2 #
##########

import time
from sympy import factorint

def f(n):
    fm = factorint(n)
    factors = [x for x in fm]
    powers = [fm[x] for x in fm]
    arr = len(fm) * [0]
    S = 0
    while True:
        m = 1
        for i in range(len(factors)):
            m *= pow(factors[i], arr[i])
        if (n <= 50 * m): S += m
        
        i = 0
        while i < len(fm):
            arr[i] += 1
            if (arr[i] > powers[i]): arr[i] = 0
            else: break
            i += 1
        if (i == len(powers)): break
    return 11 * S

start_time = time.time()
threshold = int(open("day20in.txt").read().split("\n")[0])
N = 10 ** 6
for n in range(1, N + 1):
    val = f(n)
    if (val >= threshold):
        print(n)
        break
print(time.time() - start_time)