import timeit

##########
# PART 1 #
##########

# start_time = timeit.default_timer()
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
# print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read()
count = 0
for w in data.split(","):
    x, y = w.split("-")
    for z in range(int(x), int(y)+1):
        s = str(z)
        for k in range(1, len(s)//2+1):
            t = s[:k]
            if (s==t*(len(s)//k)):
                count += z
                break
            k += 1
print(count)
print(timeit.default_timer() - start_time)