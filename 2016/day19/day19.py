##########
# PART 1 #
##########

"""
# This happens to be the Josephus Problem, where the solution was described in this Numberphile video.
# https://www.youtube.com/watch?v=uCsD3ZGzMgE

# If we look at the first couple cases where n = total number of elves and f(n) returns the winner at the end:
# n  | f(n)
# ---------
# 1  | 1
# 2  | 1
# 3  | 3
# 4  | 1
# 5  | 3
# 6  | 5
# 7  | 7
# 8  | 1
# 9  | 3
# 10 | 5
# 11 | 7
# 12 | 9
# 13 | 11
# 14 | 13
# 15 | 15
# 16 | 1

# For powers of two, 1 is always the winner. After a power of two, we list the odd numbers until we reach a
# power of 2.

# f(n) = the (1 + n - largest power of two less than n)th odd number.

import math

num = int(open("day19in.txt").read().split("\n")[0])
largest_power = 2 ** int(math.log(num, 2))
winner = 2 * (1 + num - largest_power) - 1
print(winner)
"""

##########
# PART 2 #
##########

# This is a variant of the Josephus problem, so we can list out test cases like before.

# n  | f(n)
# ---------
# 1  | 1

# 2  | 1
# 3  | 3

# 4  | 1
# 5  | 2
# 6  | 3
# 7  | 5
# 8  | 7
# 9  | 9

# 10 | 1
# 11 | 2
# 12 | 3
# 13 | 4
# 14 | 5
# 15 | 6
# 16 | 7
# 17 | 8
# 18 | 9
# 19 | 11
# 20 | 13
# 21 | 15
# 22 | 17
# 23 | 19
# 24 | 21
# 25 | 23
# 26 | 25
# 27 | 27

# 28 | 1
# 29 | 2
# 30 | 3
# 31 | 4
# 32 | 5

# It looks like the procedure is to find the power of three just less than the number, then list
# out the numbers starting at (number - power of three) until you reach that power of three.
# Then you list out n odd numbers after that power of three until you reach the next power of three
# where n is the power of three less than the number.

import math

nums = open("day19in.txt").read().split("\n")
for n in nums:
    n = int(n)
    if (n == 1):
        print(1, 1)
        continue
    power_of_three = 3 ** (int(math.log(n) / math.log(3)))
    answer = n - power_of_three
    if (answer == 0):
        print(n, power_of_three)
    elif (answer <= power_of_three):
        print(n, answer)
    else:
        answer = power_of_three + 2 * (n - 2 * power_of_three)
        print(n, answer)

"""
# Brute force code
for n in nums:
    circle = list(range(1, int(n) + 1))
    i = 0
    l = len(circle)
    while (l != 1):
        j = (i + (l//2)) % l
        circle.pop(j)
        l -= 1
        if (j >= i): i = (i + 1) % l
        else: i %= l
    print(n, circle[0])
"""