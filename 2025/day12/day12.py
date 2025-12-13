import timeit

##########
# PART 1 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
pieces = []
flag = False
count = 0
for l in data:
    if not flag and "x" in l: flag = True
    if flag:
        shape, piece_counts = l.split(": ")
        shape = tuple(int(x) for x in shape.split("x"))
        piece_counts = [int(x) for x in piece_counts.split(" ")]
        if 9*sum(piece_counts)<=shape[0]*shape[1]:
            count += 1
print(count)
print(timeit.default_timer() - start_time)