import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
for line in data:
    sequence = [int(x) for x in line.split(" ")]
    subsequences = [sequence.copy()]
    while True:
        sequence2 = [subsequences[-1][i] - subsequences[-1][i - 1] for i in range(1, len(subsequences[-1]))]
        subsequences.append(sequence2.copy())
        if (len(set(sequence2)) == 1): break
    final = subsequences[-1][-1]
    for i in range(len(subsequences) - 2, -1, -1): final += subsequences[i][-1]
    total += final
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
total = 0
for line in data:
    sequence = [int(x) for x in line.split(" ")]
    subsequences = [sequence.copy()]
    while True:
        sequence2 = [subsequences[-1][i] - subsequences[-1][i - 1] for i in range(1, len(subsequences[-1]))]
        subsequences.append(sequence2.copy())
        if (len(set(sequence2)) == 1): break
    final = subsequences[-1][0]
    for i in range(len(subsequences) - 2, -1, -1): final = subsequences[i][0] - final
    total += final
print(total)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")