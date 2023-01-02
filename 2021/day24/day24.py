##########
# PART 1 #
##########

import time

# inp w
# mul x 0   w=w, x=0, y=0, z=z
# add x z   w=w, x=z, y=0, z=z
# mod x 26  w=w, x=(z%26), y=0, z=z
# div z 1   w=w, x=(z%26), y=0, z=z                               (either 1 or 26)
# add x 15  w=w, x=(z%26)+15, y=0, z=z                            (arbitrary constant)
# eql x w   w=w, x=((z%26)+15)==w, y=0, z=z
# eql x 0   w=w, x=(((z%26)+15)==w)==0, y=0, z=z
# mul y 0   w=w, x=(((z%26)+15)==w)==0, y=0, z=z
# add y 25  w=w, x=(((z%26)+15)==w)==0, y=25, z=z
# mul y x   w=w, x=(((z%26)+15)==w)==0, y=25x, z=z
# add y 1   w=w, x=(((z%26)+15)==w)==0, y=25x+1, z=z
# mul z y   w=w, x=(((z%26)+15)==w)==0, y=25x+1, z=z*(25x+1)
# mul y 0   w=w, x=(((z%26)+15)==w)==0, y=0, z=z*(25x+1)
# add y w   w=w, x=(((z%26)+15)==w)==0, y=w, z=z*(25x+1)
# add y 13  w=w, x=(((z%26)+15)==w)==0, y=w+13, z=z*(25x+1)       (arbitrary constant)
# mul y x   w=w, x=(((z%26)+15)==w)==0, y=x(w+13), z=z*(25x+1)
# add z y   w=w, x=(((z%26)+15)==w)==0, y=x(w+13), z=z*(25x+1)+x(w+13)

# x = 0: z = z/1 or z/26
# x = 1: z = (z/1 or z/26)*26 + w + <constant>

# start_time = time.time()
# lines = open("day24in.txt").read().split("\n")

# a_list = [15, 10, 12, 10, 14, -11, 10, -16, -9, 11, -8, -8, -10, -9]
# b_list = [13, 16, 2, 8, 11, 6, 12, 2, 2, 15, 1, 10, 14, 10]
# z_divide = [1, 1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 26, 26, 26]

# def find(i, z, a_list, b_list, z_divide):
#       val = z % 26 + a_list[i]
#       if (z_divide[i] == 26):
#             # x = 0:
#             if (not (1 <= val <= 9)): return None
#             w = val
#             z //= 26
#             if (i == 13):
#                   if (z == 0): return [str(w)]
#                   else: return None
#             else:
#                   temp = find(i + 1, z, a_list, b_list, z_divide)
#                   if (temp == None): return None
#                   return [str(w)] + temp
#       else:
#             # x = 1:
#             for w in range(9, 0, -1):
#                   if (val == w): continue
#                   z_next = 26 * z + w + b_list[i]
#                   temp = find(i + 1, z_next, a_list, b_list, z_divide)
#                   if (temp == None): continue
#                   return [str(w)] + temp
#             return None

# print("".join(find(0, 0, a_list, b_list, z_divide)))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("day24in.txt").read().split("\n")

a_list = [15, 10, 12, 10, 14, -11, 10, -16, -9, 11, -8, -8, -10, -9]
b_list = [13, 16, 2, 8, 11, 6, 12, 2, 2, 15, 1, 10, 14, 10]
z_divide = [1, 1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 26, 26, 26]

def find(i, z, a_list, b_list, z_divide):
      val = z % 26 + a_list[i]
      if (z_divide[i] == 26):
            # x = 0:
            if (not (1 <= val <= 9)): return None
            w = val
            z //= 26
            if (i == 13):
                  if (z == 0): return [str(w)]
                  else: return None
            else:
                  temp = find(i + 1, z, a_list, b_list, z_divide)
                  if (temp == None): return None
                  return [str(w)] + temp
      else:
            # x = 1:
            for w in range(1, 10):
                  if (val == w): continue
                  z_next = 26 * z + w + b_list[i]
                  temp = find(i + 1, z_next, a_list, b_list, z_divide)
                  if (temp == None): continue
                  return [str(w)] + temp
            return None

print("".join(find(0, 0, a_list, b_list, z_divide)))
print(time.time() - start_time)