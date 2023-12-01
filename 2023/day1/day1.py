import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
x = 0
for s in data:
    first, last = None, None
    found_first = False
    for c in s:
        if ord('1') <= ord(c) <= ord('9'):
            if (found_first): last = c
            else:
                first = c
                last = c
            found_first = True
    if (first != None):x += int(first + last)
print(x)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

f = open("input.txt", 'r')
data = f.read().split("\n")
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
x = 0
for s in data:
    first, last = None, None
    first_index, last_index = len(s), -1
    found_first = False
    i = 0
    for c in s:
        if ord('1') <= ord(c) <= ord('9'):
            if (found_first):
                last = c
                last_index = i
            else:
                first = c
                last = c
                first_index = i
                last_index = i
            found_first = True
        i += 1
    i = 1
    for t in nums:
        s2 = s
        j = 0
        while t in s2:
            j += s2.index(t)
            s2 = s2[s2.index(t) + len(t):]
            if (j < first_index):
                first = str(i)
                first_index = j
            if (j > last_index):
                last = str(i)
                last_index = j
            j += len(t)
        i += 1
    if (first != None): x += int(first + last)
print(x)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()