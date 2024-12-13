import time
# import numpy as np

# ##########
# # PART 1 #
# ##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# A = [[0, 0], [0, 0]]
# B = []
# count = 0
# total = 0
# for l in data:
#     if (l == ""):
#         A, B = np.asarray(A), np.asarray(B)
#         X = np.dot(np.linalg.inv(A), B.T)
#         valid = True
#         for x in X:
#             if (abs(x - round(x)) > 1e-9):
#                 valid = False
#                 break
#         if (valid): total += 3*X[0] + X[1]
#         A = [[0, 0], [0, 0]]
#         B = []
#         count = 0
#     elif ('+' in l):
#         s = l.split(",")
#         y = int(s[1].split('+')[1])
#         x = int(s[0].split("+")[-1])
#         A[0][count] = x
#         A[1][count] = y
#         count += 1
#     else:
#         s = l.split(",")
#         y = int(s[1].split('=')[1])
#         x = int(s[0].split("=")[-1])
#         B += [x, y]
# print(int(total))
# print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
A = [[0, 0], [0, 0]]
B = []

count = 0
total = 0
for l in data:
    if (l == ""):
        det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        A_inv = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
        X = [A_inv[0][0] * B[0] + A_inv[0][1] * B[1], A_inv[1][0] * B[0] + A_inv[1][1] * B[1]]
        #print(A, B, X[0]/det, X[1]/det)
        if (X[0] % det == 0 and X[1] % det == 0): total += (3*X[0] + X[1])//det
        A = [[0, 0], [0, 0]]
        B = []
        count = 0
    elif ('+' in l):
        s = l.split(",")
        y = int(s[1].split('+')[1])
        x = int(s[0].split("+")[-1])
        A[0][count] = x
        A[1][count] = y
        count += 1
    else:
        s = l.split(",")
        y = int(s[1].split('=')[1])
        x = int(s[0].split("=")[-1])
        B += [x + 10000000000000, y + 10000000000000]
print(int(total))
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")