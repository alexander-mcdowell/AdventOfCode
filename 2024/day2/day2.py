import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
safes = 0
for line in data:
    arr = [int(x) for x in line.split(" ")]
    
    valid = True
    if (len(arr) == 1):
        safes += 1
        continue
    
    if (arr[1] == arr[0]): continue
    init_diff = arr[1] - arr[0]
    if (abs(init_diff) > 3): continue
    
    for i in range(2, len(arr)):
        if (arr[i] == arr[i-1]):
            valid = False
            break
        diff = arr[i] - arr[i - 1]
        if (abs(diff) > 3 or diff * init_diff < 0):
            valid = False
            break
    if (valid): safes += 1
print(safes)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

def is_valid(x):
    if (len(x) == 1): return True
    if (x[1] == x[0]): return False
    inc = x[1] > x[0]
    if (abs(x[1] - x[0]) > 3): return False
    for i in range(2, len(x)):
        diff = abs(x[i] - x[i - 1])
        cond = diff>3 or x[i] == x[i-1] or (inc and x[i] < x[i-1]) or (not inc and x[i] > x[i-1])
        if (cond): return False
    return True

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
safes = 0
for line in data:
    arr = [int(x) for x in line.split(" ")]
    # Check if change needs to be made
    if (not is_valid(arr)):
        for j in range(len(arr)):
            arr2 = arr[:j] + arr[j+1:]
            if (is_valid(arr2)):
                safes += 1
                break
    else: safes += 1
print(safes)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()