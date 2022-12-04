##########
# PART 1 #
##########

"""
data = open("day3in.txt").read().split("\n")
triangles = 0
for triangle in data:
    triangle = triangle.split(" ")
    while (True):
        try:
            triangle.remove('')
        except ValueError as _: break
    a, b, c = [int(x) for x in triangle]
    # Should be greater than or equal to but I don't get to write the problems.
    if ((a + b) > c and (a + c) > b and (b + c) > a): triangles += 1
print(triangles)
"""

##########
# PART 2 #
##########

# Read the data as sets of three numbers in three columns:
# Example:
#
# A1, B1, C1
# A2, B2, C2
# A3, B3, C3
# A4, B4, C4
# A5, B5, C5
# A6, B6, C6
# 
# (A1, A2, A3) form a triangle, (A4, A5, A6) form a triangle, (B1, B2, B3) form a triangle, etc.

data = open("day3in.txt").read().split("\n")
triangles = 0
for i in range(0, len(data) - 2, 3):
    row_set = []
    for k in range(3):
        row = data[i + k].split(" ")
        while (True):
            try:
                row.remove('')
            except ValueError as _: break
        row_set.append([int(x) for x in row])
    for col_num in range(3):
        a, b, c = [row_set[k][col_num] for k in range(3)]
        if ((a + b) > c and (a + c) > b and (b + c) > a): triangles += 1
print(triangles)