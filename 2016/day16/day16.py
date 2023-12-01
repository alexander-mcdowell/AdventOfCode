import time

##########
# PART 1 #
##########

# start_time = time.time()
# s = open("input.txt").read().split("\n")[0]
# length = 272
# while len(s) < length:
#     a, b = s, s
#     b = b.replace('1', '2')
#     b = b.replace('0', '1')
#     b = b.replace('2', '0')
#     s = a + "0" + b[::-1]

# def compress(s):
#     if (len(s) % 2 == 1): return s
#     pairs = [s[2 * i : 2 * (i + 1)] for i in range(len(s)//2)]
#     s2 = ""
#     for pair in pairs:
#         if (pair[0] == pair[1]): s2 += "1"
#         else: s2 += "0"
#     return compress(s2)

# print(compress(s[:length]))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
s = open("input.txt").read().split("\n")[0]
length = 272
while len(s) < length:
    a, b = s, s
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    s = a + "0" + b[::-1]

def compress(s):
    if (len(s) % 2 == 1): return s
    pairs = [s[2 * i : 2 * (i + 1)] for i in range(len(s)//2)]
    s2 = ""
    for pair in pairs:
        if (pair[0] == pair[1]): s2 += "1"
        else: s2 += "0"
    return compress(s2)

print(compress(s[:length]))
print(time.time() - start_time)