##########
# PART 1 #
##########

"""
def unpack(s):
    t, count_s = "", ""
    inside_p = False
    i = 0
    while (i < len(s)):
        if (inside_p):
            if (s[i] == ')'):
                s_len, freq = [int(x) for x in count_s.split('x')]
                t += (s[i + 1 : i + 1 + s_len] * freq)
                i += s_len + 1
                inside_p = False
                count_s = ""
                continue
            else: count_s += s[i]
        else:
            if (s[i] == '('): inside_p = True
            else: t += s[i]
        i += 1
    return t

s = open("day9in.txt").read().split("\n")[0]
decompressed = unpack(s)
print(len(decompressed))
"""

##########
# PART 2 #
##########

def unpack(s):
    length, count_s = 0, ""
    inside_p = False
    i = 0
    while (i < len(s)):
        if (inside_p):
            if (s[i] == ')'):
                s_len, freq = [int(x) for x in count_s.split('x')]
                length += (unpack(s[i + 1 : i + 1 + s_len]) * freq)
                i += s_len + 1
                inside_p = False
                count_s = ""
                continue
            else: count_s += s[i]
        else:
            if (s[i] == '('): inside_p = True
            else: length += 1
        i += 1
    return length

s = open("day9in.txt").read().split("\n")[0]
decompressed = unpack(s)
print(decompressed)