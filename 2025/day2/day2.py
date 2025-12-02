import time

##########
# PART 1 #
##########

# start_time = time.time()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# count = 0
# for l in data:
#     for w in l.split(","):
#         if w=="": continue
#         x, y = w.split("-")
#         for z in range(int(x), int(y)+1):
#             s = str(z)
#             if (len(s)%2 == 1): continue
#             t = s[:len(s)//2]
#             if (s==t+t):
#                 count += z
# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read()
count = 0
for w in data.split(","):
    x, y = w.split("-")
    for z in range(int(x), int(y)+1):
        s = str(z)
        k = 2
        while True:
            if (k > len(s)): break
            if len(s)%k!=0:
                k += 1
                continue
            t = s[:len(s)//k]
            if (s==t*k):
                count += z
                break
            k += 1
print(count)
print(time.time() - start_time)