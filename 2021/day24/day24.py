##########
# PART 1 #
##########

# All blocks start with:
#   inp w
#   mul x 0
#   add x z
#   mod x 26
# Followed by "div z k1" where k1 = 1 or 26
# Followed by "add x <some number k2>"
# Then followed by:
#   eql x w
#   eql x 0
#   mul y 0
#   add y 25
#   mul y x
#   add y 1
#   mul z y
#   mul y 0
#   add y w
# Then followed by "add y <some number k3>"
# Then concluded with:
#   mul y x
#   add z y

# z[0] = 0
# z[n] = (z[n - 1] / k1) + (((z[n - 1] % 26) + k2) != d[n]) * (25 * (z[n - 1] / k1) + d[n] + k3)
# DNE = (((z[n - 1] % 26) + k2) != d[n])
# z[n] = (z[n - 1] / k1) + DNE * (25 * (z[n - 1] / k1) + d[n] + k3)

# If DNE = 0:
# d[n] = (z[n - 1] % 26) + k2
# z[n] = (z[n - 1] / k1)
# If DNE = 1:
# d[n] != (z[n - 1] % 26) + k2
# z[n] = 26 * (z[n - 1] / k1) + d[n] + k3

"""
1:
div z 1
add x 15
add y 13

2:
div z 1
add x 10
add y 16

3:
div z 1
add x 12
add y 2

4:
div z 1
add x 10
add y 8

5:
div z 1
add x 14
add y 11

6:
div z 26
add x -11
add y 6

7:
div z 1
add x 10
add y 12

8:
div z 26
add x -16
add y 2

9:
div z 26
add x -9
add y 2

10:
div z 1
add x 11
add y 15

11:
div z 26
add x -8
add y 1

12:
div z 26
add x -8
add y 10

13:
div z 26
add x -10
add y 14

14:
div z 26
add x -9
add y 10
"""

ks = [(1, 15, 13),
      (1, 10, 16),
      (1, 12, 2),
      (1, 10, 8),
      (1, 14, 11),
      (26, -11, 6),
      (1, 10, 12),
      (26, -16, 2),
      (26, -9, 2),
      (1, 11, 15),
      (26, -8, 1),
      (26, -8, 10),
      (26, -10, 14),
      (26, -9, 10)]

# If DNE = 0:
# d[n] = (z[n - 1] % 26) + k2
# z[n] = (z[n - 1] / k1)
# If DNE = 1:
# d[n] != (z[n - 1] % 26) + k2
# z[n] = 26 * (z[n - 1] / k1) + d[n] + k3

# Applying this procedure starting from z[0] and testing different DNE values yields:

# z[0] = 0

# z[1] = d[1] + 13
# d[1] != 15

# z[2] = 26 * d[1] + d[2] + 354
# d[2] != (d[1] + 13) % 26 + 10

# z[3] = 26^2 * d[1] + 26 * d[2] + d[3] + 9206
# d[3] != (d[2] + 16) % 26 + 12

# z[4] = 26^3 * d[1] + 26^2 * d[2] + 26 * d[3] + d[4] + 239364
# d[4] != (d[3] + 2) % 26 + 10

# z[5] = 26^4 * d[1] + 26^3 * d[2] + 26^2 * d[3] + 26 * d[4] + d[5] + 6223464
# d[5] != (d[4] + 8) % 26 + 14
