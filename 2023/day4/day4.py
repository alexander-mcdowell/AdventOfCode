import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
total = 0
for game in data:
    matched = False
    id, nums = game.split(": ")
    target, card = nums.split(" | ")
    target = [int(x) for x in target.split(" ") if x != '']
    card = [int(x) for x in card.split(" ") if x != '']
    matches = 0
    for x in card:
        if (x in target): matches += 1
    if (matches != 0): total += 2**(matches-1)
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

cards = [1 for _ in range(len(data))]
i = 1
for game in data:
    matched = False
    id, nums = game.split(": ")
    target, card = nums.split(" | ")
    target = [int(x) for x in target.split(" ") if x != '']
    card = [int(x) for x in card.split(" ") if x != '']
    matches = 0
    for x in card:
        if (x in target): matches += 1
    for j in range(i + 1, i + matches + 1): cards[j - 1] += cards[i - 1]
    i += 1
print(sum(cards))
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")
f.close()