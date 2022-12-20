import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# arr = []
# counts = {}
# for line in lines:
#     val = int(line)
#     if (val not in counts): counts[val] = 0
#     counts[val] += 1
#     arr.append((val, counts[val]))

# def sign(x): return 1 if x > 0 else -1

# counts2 = {}
# for line in lines:
#     val = int(line)
#     if (val == 0): continue
    
#     if (val not in counts2): counts2[val] = 0
#     counts2[val] += 1

#     i = arr.index((val, counts2[val]))
#     j = (i + sign(val)) % (len(arr))
#     for _ in range(abs(val)):
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
#         i = j
#         j = (i + sign(val)) % (len(arr))
#     #print(val, arr) 

# S = 0
# zero_index = arr.index((0, 1))
# for shift in [1000, 2000, 3000]:
#     S += arr[(zero_index + shift) % len(arr)][0]
# print(S)
# print(time.time() - start_time)

##########
# PART 2 #
##########

key = 811589153
N = 10

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
arr = []
counts = {}
for line in lines:
    val = key * int(line)
    if (val not in counts): counts[val] = 0
    counts[val] += 1
    arr.append((val, counts[val]))

def sign(x): return 1 if x > 0 else -1

for _ in range(N):
    counts2 = {}
    for line in lines:
        val = key * int(line)
        if (val == 0): continue
        
        if (val not in counts2): counts2[val] = 0
        counts2[val] += 1

        i = arr.index((val, counts2[val]))
        j = (i + (val) % (len(arr) - 1)) % (len(arr))
        arr.insert(j + 1, (val, counts2[val]))
        arr.pop((j < i) + i)

S = 0
zero_index = arr.index((0, 1))
for shift in [1000, 2000, 3000]:
    S += arr[(zero_index + shift) % len(arr)][0]
print(S)
print(time.time() - start_time)