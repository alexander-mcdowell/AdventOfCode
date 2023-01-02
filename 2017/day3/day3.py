import time
import math

##########
# PART 1 #
##########

# # 17  16  15  14  13
# # 18   5   4   3  12
# # 19   6   1   2  11
# # 20   7   8   9  10
# # 21  22  23  24  25

# start_time = time.time()
# num = int(open("input.txt").read().split("\n")[0])
# k = int((math.sqrt(num) - 1)//2)
# lower = 2 * k + 1
# along = num - (lower * lower)
# x, y = k, -k
# # Location of num will be "along" units along the square with side length "lower + 1"
# if (along == 0): print(2 * k)
# else:
#     along -= 1
#     x += 1
#     i = 0

#     counter = 0
#     while (i < along):
#         if (counter == lower): break
#         counter += 1
#         i += 1
#         y += 1
#     counter = 0
#     while (i < along):
#         if (counter == (lower + 1)): break
#         counter += 1
#         i += 1
#         x -= 1
#     counter = 0
#     while (i < along):
#         if (counter == (lower + 1)): break
#         counter += 1
#         i += 1
#         y -= 1
#     counter = 0
#     while (i < along):
#         if (counter == (lower + 1)): break
#         counter += 1
#         i += 1
#         x += 1
    
#     print(abs(x) + abs(y))
# print(time.time() - start_time)

##########
# PART 2 #
##########

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

start_time = time.time()
num = int(open("input.txt").read().split("\n")[0])
n = 2
point_to_val = {(0, 0): 1}
while True:
    k = int((math.sqrt(n) - 1)//2)
    lower = 2 * k + 1
    along = n - (lower * lower)
    x, y = k, -k

    if (along != 0):
        along -= 1
        x += 1
        i = 0

        counter = 0
        while (i < along):
            if (counter == lower): break
            counter += 1
            i += 1
            y += 1
        counter = 0
        while (i < along):
            if (counter == (lower + 1)): break
            counter += 1
            i += 1
            x -= 1
        counter = 0
        while (i < along):
            if (counter == (lower + 1)): break
            counter += 1
            i += 1
            y -= 1
        counter = 0
        while (i < along):
            if (counter == (lower + 1)): break
            counter += 1
            i += 1
            x += 1

    S = 0
    for adj in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        dx, dy = adj
        if ((x + dx, y + dy) in point_to_val): S += point_to_val[(x + dx, y + dy)]
    point_to_val[(x, y)] = S
    
    if (S > num):
        print(S)
        break
    n += 1
print(time.time() - start_time)