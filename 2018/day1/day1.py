import time

##########
# PART 1 #
##########

# start_time = time.time()
# shifts = open("input.txt").read().split("\n")
# print(sum([int(shift) for shift in shifts]))
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
shifts = [int(shift) for shift in open("input.txt").read().split("\n")]
freq_list = set()
freq = 0
i = 0
while True:
    freq += shifts[i]
    if (freq in freq_list):
        print(freq)
        break
    freq_list.add(freq)
    i = (i + 1) % len(shifts)
print(time.time() - start_time)