##########
# PART 1 #
##########

# import time

# start_time = time.time()
# line = open("input.txt").read().strip().split(" ")
# players, final = int(line[0]), int(line[-2])
# arr = [0]
# marble = 1
# i = 0
# scores = [0 for _ in range(players)]
# player_counter = 0
# while marble <= final:
#     if (marble % 23 == 0):
#         scores[player_counter] += marble
#         j = i
#         for _ in range(7): j = (j - 1) % len(arr)
#         scores[player_counter] += arr.pop(j)
#         i = j % len(arr)
#     else:
#         dest = (i + 1) % len(arr)
#         arr.insert(dest + 1, marble)
#         i = dest + 1
#     marble += 1
#     player_counter = (player_counter + 1) % players
# print(max(scores))
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

start_time = time.time()
line = open("input.txt").read().strip().split(" ")
players, final = int(line[0]), 100 * int(line[-2])

root = Node(0, None, None)
root.prev = root
root.next = root
iter = root

marble = 1
scores = [0 for _ in range(players)]
player_counter = 0
while marble <= final:
    if (marble % 23 == 0):
        scores[player_counter] += marble
        iter2 = iter
        for _ in range(7): iter2 = iter2.prev
        
        val = iter2.val
        scores[player_counter] += val
        iter2.next.prev = iter2.prev
        iter2.prev.next = iter2.next
        
        iter = iter2.next
    else:
        iter = iter.next
        insert = Node(marble, iter, iter.next)
        iter.next.prev = insert
        iter.next = insert
        iter = iter.next
    marble += 1
    player_counter = (player_counter + 1) % players
print(max(scores))
print(time.time() - start_time)