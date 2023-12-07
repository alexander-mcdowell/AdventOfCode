import time

##########
# PART 1 #
##########

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def is_stronger(h1, h2):
    for i in range(len(h1)):
        if (cards.index(h1[i]) > cards.index(h2[i])): return 1
        elif (cards.index(h1[i]) < cards.index(h2[i])): return -1
    return 0

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
groupings = [[] for _ in range(7)]
bids = {}
for line in data:
    hand, bid = line.split(" ")
    bids[hand] = int(bid)
    distinct = list(set(hand))

    if (len(distinct) == 1): groupings[0].append(hand)
    else:
        counts = sorted([hand.count(x) for x in distinct])
        if (counts == [1, 4]): groupings[1].append(hand)
        elif (counts == [2, 3]): groupings[2].append(hand)
        elif (counts == [1, 1, 3]): groupings[3].append(hand)
        elif (counts == [1, 2, 2]): groupings[4].append(hand)
        elif (counts == [1, 1, 1, 2]): groupings[5].append(hand)
        else: groupings[6].append(hand)
for i in range(7):
    # Insertion sort
    j = 1
    while j < len(groupings[i]):
        k = j
        while k != 0 and is_stronger(groupings[i][k], groupings[i][k - 1]) == -1:
            temp = groupings[i][k - 1]
            groupings[i][k - 1] = groupings[i][k]
            groupings[i][k] = temp
            k -= 1
        j += 1
rank = 1
total = 0
for i in range(6, -1, -1):
    for j in range(len(groupings[i])):
        total += bids[groupings[i][j]] * rank
        rank += 1
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

from itertools import combinations, product

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def is_stronger(h1, h2):
    for i in range(len(h1)):
        if (cards.index(h1[i]) > cards.index(h2[i])): return 1
        elif (cards.index(h1[i]) < cards.index(h2[i])): return -1
    return 0

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
groupings = [[] for _ in range(7)]
bids = {}
for line in data:
    hand, bid = line.split(" ")
    jack_indices = [i for i in range(len(hand)) if hand[i] == 'J']
    best = 6
    
    # No change
    distinct = list(set(hand))
    if (len(distinct) == 1): best = 0
    else:
        counts = sorted([hand.count(x) for x in distinct])
        if (counts == [1, 4]): best = 1
        elif (counts == [2, 3]): best = 2
        elif (counts == [1, 1, 3]): best = 3
        elif (counts == [1, 2, 2]): best = 4
        elif (counts == [1, 1, 1, 2]): best = 5
        else: best = 6
    
    # Modify jacks
    for r in range(1, hand.count('J') + 1):
        for comb in combinations(jack_indices, r):
            for perm in product(cards, repeat = r):
                hand2 = list(hand)
                for i in range(r): hand2[comb[i]] = perm[i]
                distinct = list(set(hand2))

                if (len(distinct) == 1): val = 0
                else:
                    counts = sorted([hand2.count(x) for x in distinct])
                    if (counts == [1, 4]): val = 1
                    elif (counts == [2, 3]): val = 2
                    elif (counts == [1, 1, 3]): val = 3
                    elif (counts == [1, 2, 2]): val = 4
                    elif (counts == [1, 1, 1, 2]): val = 5
                    else: val = 6
                if (val < best): best = val
    bids[hand] = int(bid)
    groupings[best].append(hand)
for i in range(7):
    # Insertion sort
    j = 1
    while j < len(groupings[i]):
        k = j
        while k != 0 and is_stronger(groupings[i][k], groupings[i][k - 1]) == -1:
            temp = groupings[i][k - 1]
            groupings[i][k - 1] = groupings[i][k]
            groupings[i][k] = temp
            k -= 1
        j += 1
rank = 1
total = 0
for i in range(6, -1, -1):
    for j in range(len(groupings[i])):
        total += bids[groupings[i][j]] * rank
        rank += 1
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")