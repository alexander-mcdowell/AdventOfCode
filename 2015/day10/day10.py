##########
# PART 1 #
##########

"""
data = open("day10in.txt").read().split("\n")[0]
s = data
for _ in range(40):
    new_string = ""
    char, count = None, 0
    for i in range(len(s)):
        if (count == 0):
            char = s[i]
            count = 1
        else:
            if (s[i] == char):
                count += 1
            else:
                new_string += str(count) + str(char)
                char, count = s[i], 1
    new_string += str(count) + str(char)
    s = new_string
print(len(s))
"""

##########
# PART 2 #
##########

data = open("day10in.txt").read().split("\n")[0]
s = data
for _ in range(50):
    new_string = ""
    char, count = None, 0
    for i in range(len(s)):
        if (count == 0):
            char = s[i]
            count = 1
        else:
            if (s[i] == char):
                count += 1
            else:
                new_string += str(count) + str(char)
                char, count = s[i], 1
    new_string += str(count) + str(char)
    s = new_string
print(len(s))