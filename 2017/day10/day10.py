import time

##########
# PART 1 #
##########

# start_time = time.time()
# lengths = [int(x) for x in open("input.txt").read().split("\n")[0].split(",")]
# arr = list(range(256))
# pos = 0
# skip_size = 0
# for length in lengths:
#     subarray = []
#     i = pos
#     for _ in range(length):
#         subarray.append(arr[i])
#         i = (i + 1) % len(arr)
#     for j in range(length):
#         i = (i - 1) % len(arr)
#         arr[i] = subarray[j]
#     pos = (pos + length + skip_size) % len(arr)
#     skip_size += 1
# print(arr[0] * arr[1])
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lengths = [ord(x) for x in open("input.txt").read().split("\n")[0] if x != '']
lengths += [17, 31, 73, 47, 23]
arr = list(range(256))
pos = 0
skip_size = 0
for _ in range(64):
    for length in lengths:
        subarray = []
        i = pos
        for _ in range(length):
            subarray.append(arr[i])
            i = (i + 1) % len(arr)
        for j in range(length):
            i = (i - 1) % len(arr)
            arr[i] = subarray[j]
        pos = (pos + length + skip_size) % len(arr)
        skip_size += 1
s = ""
for i in range(16):
    val = 0
    for j in range(16 * i, 16 * (i + 1)):
        val ^= arr[j]
    h = hex(val)[2:]
    if (len(h) == 1): h = '0' + h
    s += h
print(s)
print(time.time() - start_time)