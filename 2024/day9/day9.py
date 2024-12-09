import time
import math

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = list(f.read().split("\n")[0])
data_num = 0
blocks, free = [], []
mode = 0
n = 0
for x in data:
    if (mode == 0):
        blocks.append([data_num for _ in range(int(x))])
        data_num += 1
    else:
        free.append(int(x))
    n += int(x)
    mode = 1 - mode

mode = 0
id, rev_id = 0, n - 1
block_i, free_i = 0, 0
total = 0
while id <= rev_id:
    if (mode == 0):
        for x in blocks[block_i]:
            total += id * x
            #print(0, id, rev_id, x)
            id += 1
            if (id > rev_id): break
        block_i += 1
    else:
        for _ in range(free[free_i]):
            x = blocks[-1].pop()
            if (len(blocks[-1]) == 0):
                blocks.pop(-1)
                rev_id -= free.pop(-1)
            #print(1, id, rev_id, x)
            total += id * x
            id += 1
            rev_id -= 1
            if (id > rev_id): break
        free_i += 1
    mode = 1 - mode
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = list(f.read().split("\n")[0])
data_num = 0

# blocks stores the index the block occurs on and its length for each block number
# free stores the number of free spaces for each free block
blocks, free = [], []
block_ids = []
id_to_block = {}
mode = 0
n = 0
for x in data:
    # add new block
    if (mode == 0):
        blocks.append((n, int(x)))
        id_to_block[n] = (data_num, int(x))
        data_num += 1
        block_ids.append(n)
    # add new free space
    else:
        free.append(int(x))
    n += int(x)
    mode = 1 - mode

total = 0
free_i = 0
keep_i = 0
id = 0
mode = 0
used = set()
arr = list(range(len(blocks)))
while keep_i<len(block_ids):
    # try to pick up a block and move into a free space
    if (mode == 1):
        to_free = free[free_i]
        j = len(arr) - 1
        while j != 0 and to_free != 0:
            data_num = arr[j]
            # make sure it's not a block we've kept
            if (data_num in used): break
            # move the block into position
            l = blocks[data_num][1]
            
            if (l <= to_free):
                to_free -= l
                # (id + (id + 1) + ... + (id + l)) * data_num
                # data_num * ((id + l)*(id + l + 1) - (id - 1)*id)//2
                if (id != 0): count = ((id + l - 1) * (id + l) - (id - 1)*id) // 2
                else: count = (l * (l - 1)) // 2
                total += count * data_num
                id += l
                used.add(data_num)
                arr.pop(j)
            j -= 1
        free_i += 1
    # keep the nearest block
    else:
        id = block_ids[keep_i]
        data_num, l = id_to_block[id]
        # make sure it's not a block we've moved before
        if (data_num not in used):
            used.add(data_num)
            # (id + (id + 1) + ... + (id + l)) * data_num
            # data_num * ((id + l)*(id + l + 1) - (id - 1)*id)//2
            if (id != 0): count = ((id + l - 1) * (id + l) - (id - 1)*id) // 2
            else: count = (l * (l - 1)) // 2
            total += count * data_num
        id += l
        keep_i += 1
    mode = 1 - mode
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()