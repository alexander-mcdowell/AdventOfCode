import timeit

##########
# PART 1 #
##########

# start_time = timeit.default_timer()
# f = open("input.txt", 'r')
# data = f.read().split("\n")
# matrix = []
# total = 0
# for l in data:
#     if l[0] in "*+":
#         j = 0
#         for op in l.split(" "):
#             if len(op)==0: continue
#             count = matrix[0][j]
#             for i in range(1, len(matrix)):
#                 if op=="*": count *= matrix[i][j]
#                 else: count += matrix[i][j]
#             total += count
#             j += 1
#         continue
#     row = []
#     for x in l.split(" "):
#         if len(x)==0: continue
#         row.append(int(x))
#     matrix.append(row)
# print(total)
# print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

def processOp(mode, length, j):
    count = None
    for k in range(length):
        x = 0
        # Read left-to-right because operations are commutative
        for i in range(len(data)-1):
            if (data[i][j+k] == " "): continue
            x = 10*x + int(data[i][j + k])

        if count==None: count = x
        else:
            if mode: count *= x
            else: count += x
    return count

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
j = 0
total = 0
op, op_len = None, 0
for c in data[len(data)-1]:
    if (c in "+*"):
        if op!=None:
            total += processOp(op, op_len, j)
            j += op_len + 1
        op = 0 if c=="+" else 1
        op_len = 0
    else: 
        op_len += 1
total += processOp(op, op_len+1, j)

print(total)
print(timeit.default_timer() - start_time)