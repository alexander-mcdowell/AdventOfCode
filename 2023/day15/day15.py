import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
text = f.read().split("\n")[0]
total = 0
for word in text.split(","):
    current_value = 0
    for c in word:
        current_value += ord(c)
        current_value = 17 * current_value % 256
    total += current_value
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
labels = [set() for _ in range(256)]
label_index = {}
items = [[] for _ in range(256)]
for word in text.split(","):
    if ('-' in word):
        label = word.split('-')[0]
        mode = True
    else:
        label, num = word.split('=')
        num = int(num)
        mode = False
    
    current_value = 0
    for c in label:
        current_value += ord(c)
        current_value = 17 * current_value % 256

    if (mode):
        if (label not in labels[current_value]): continue
        items[current_value].pop(label_index[label])
        labels[current_value].remove(label)
        for i in range(label_index[label], len(items[current_value])): label_index[items[current_value][i][0]] -= 1
        label_index.pop(label)
    else:
        if (label in label_index):
            items[current_value][label_index[label]] = (label, num)
        else:
            labels[current_value].add(label)
            label_index[label] = len(items[current_value])
            items[current_value].append((label, num))
power = 0
for i in range(1, 257):
    for j in range(1, len(items[i - 1]) + 1): power += i * j * items[i - 1][j - 1][1]
print(power)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")