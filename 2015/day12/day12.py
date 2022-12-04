##########
# PART 1 #
##########

"""
data = open("day12in.txt").read().split("\n")[0]
total = 0
add_num = False
for x in data:
    if (add_num):
        try:
            if (x != "-"): int(x)
            s += x
        except Exception as _:
            total += 0 if s == "" else int(s)
            s = ""
            add_num = False
    if (not add_num and x in [":", ",", "["]):
        add_num = True
        s = ""
print(total)
"""

##########
# PART 2 #
##########

data = open("day12in.txt").read().split("\n")[0]
# The magic of eval
json = eval(data)
total = 0

def get_sum(json):
    total = 0
    for x in json:
        if (type(x) == int): total += x
        elif (type(x) == list): total += get_sum(x)
        elif (type(x) == type({})):
            vals = [x[y] for y in x]
            if ("red" not in vals): total += get_sum(vals)
    return total

print(get_sum(json))