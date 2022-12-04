##########
# PART 1 #
##########

"""
data = open("day8in.txt").read().split("\n")
total = 0
for s in data:
    chars = len(s)
    string_chars = 0
    i = 1
    while (i < len(s) - 2):
        string_chars += 1
        if (s[i] == "\\"):
            if (s[i + 1] == "\\" or s[i + 1] == '\"'): i += 2
            elif (s[i + 1] == "x"): i += 4
        else: i += 1
    if (i < len(s) - 1): string_chars += 1
    
    total += chars - string_chars
            
print(total)
"""

##########
# PART 2 #
##########

data = open("day8in.txt").read().split("\n")
total = 0
for s in data:
    chars = len(s)
    string_chars = 6
    for i in range(1, len(s) - 1):
        string_chars += 1
        if (s[i] in ["\\", '\"']): string_chars += 1
    total += string_chars - chars

print(total)