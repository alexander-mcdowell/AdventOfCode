##########
# PART 1 #
##########

"""
data = open("day2in.txt").read().split("\n")
total = 0
for dim in data:
    l, w, h = [int(x) for x in dim.split("x")]
    prod = [l * w, w * h, h * l]
    paper = 2 * (prod[0] + prod[1] + prod[2]) + min(prod)
    total += paper
print(total)
"""

##########
# PART 2 #
##########

data = open("day2in.txt").read().split("\n")
total = 0
for dim in data:
    l, w, h = [int(x) for x in dim.split("x")]
    semi_perim = [l + w, w + h, h + l]
    total += l * w * h + 2 * min(semi_perim)
print(total)