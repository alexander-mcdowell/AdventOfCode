##########
# PART 1 #
##########

# import time

# data = open("day22in.txt").read().split("\n")
# boss_hp = int(data[0].replace("Hit Points: ", ""))
# boss_damage = int(data[1].replace("Damage: ", ""))

# player_hp = 50
# player_armor = 0
# player_mana = 500

# start_time = time.time()
# best_spent = -1
# queue = [(player_hp, player_armor, player_mana, boss_hp, boss_damage, (0, 0, 0), 0, 0)]
# while len(queue) != 0:
#     player_hp, player_armor, player_mana, boss_hp, boss_damage, timers, turn, spent = queue.pop(0)
#     if (best_spent != -1 and spent >= best_spent): continue

#     if (turn == 1):
#         # Poison timer
#         if (timers[0] != 0): boss_hp -= 3
#         # Shield Timer
#         if (timers[1] != 0): player_armor = 7
#         else: player_armor = 0
#         # Recharge Timer
#         if (timers[2] != 0): player_mana += 101
        
#         # Check if boss is dead
#         if (boss_hp <= 0):
#             if (best_spent == -1 or spent < best_spent): best_spent = spent
        
#         # Deal damage
#         player_hp -= max(boss_damage - player_armor, 1)
#         if (player_hp <= 0): continue
        
#         timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))
#         turn = 0

#     # Poison timer
#     if (timers[0] != 0): boss_hp -= 3
#     # Shield Timer
#     if (timers[1] != 0): player_armor = 7
#     else: player_armor = 0
#     # Recharge Timer
#     if (timers[2] != 0): player_mana += 101
    
#     # Check if the boss is dead
#     if (boss_hp <= 0):
#         if (best_spent == -1 or spent < best_spent): best_spent = spent
    
#     timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))

#     options = []
#     # Cast Magic Missile
#     if (player_mana >= 53):
#         queue.append((player_hp, player_armor, player_mana - 53, boss_hp - 4, boss_damage, timers, 1, spent + 53))

#     # Cast Drain
#     if (player_mana >= 73):
#         queue.append((player_hp + 2, player_armor, player_mana - 73, boss_hp - 2, boss_damage, timers, 1, spent + 73))
    
#     # Cast Poison
#     if (player_mana >= 173 and timers[0] == 0):
#         queue.append((player_hp, player_armor, player_mana - 173, boss_hp, boss_damage, (6, timers[1], timers[2]), 1, spent + 173))

#     # Cast Shield
#     if (player_mana >= 113 and timers[1] == 0):
#         queue.append((player_hp, player_armor, player_mana - 113, boss_hp, boss_damage, (timers[0], 6, timers[2]), 1, spent + 113))

#     # Cast Recharge
#     if (player_mana >= 229 and timers[2] == 0):
#         queue.append((player_hp, player_armor, player_mana - 229, boss_hp, boss_damage, (timers[0], timers[1], 5), 1, spent + 229))

# print(best_spent)
# print(time.time() - start_time)

##########
# PART 2 #
##########

import time

data = open("day22in.txt").read().split("\n")
boss_hp = int(data[0].replace("Hit Points: ", ""))
boss_damage = int(data[1].replace("Damage: ", ""))

player_hp = 50
player_armor = 0
player_mana = 500

start_time = time.time()
best_spent = -1
stack = [(player_hp, player_armor, player_mana, boss_hp, boss_damage, (0, 0, 0), 0, 0)]
while len(stack) != 0:
    player_hp, player_armor, player_mana, boss_hp, boss_damage, timers, turn, spent = stack.pop(-1)
    if (best_spent != -1 and spent >= best_spent): continue

    if (turn == 1):
        # Poison timer
        if (timers[0] != 0): boss_hp -= 3
        # Shield Timer
        if (timers[1] != 0): player_armor = 7
        else: player_armor = 0
        # Recharge Timer
        if (timers[2] != 0): player_mana += 101
        
        # Check if boss is dead
        if (boss_hp <= 0):
            if (best_spent == -1 or spent < best_spent): best_spent = spent
            continue
        
        # Deal damage
        player_hp -= max(boss_damage - player_armor, 1)
        if (player_hp <= 0): continue
        
        timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))

    player_hp -= 1
    if (player_hp <= 0): continue

    # Poison timer
    if (timers[0] != 0): boss_hp -= 3
    # Shield Timer
    if (timers[1] != 0): player_armor = 7
    else: player_armor = 0
    # Recharge Timer
    if (timers[2] != 0): player_mana += 101
    
    # Check if the boss is dead
    if (boss_hp <= 0):
        if (best_spent == -1 or spent < best_spent): best_spent = spent
        continue
    
    timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))

    options = []
    # Cast Magic Missile
    if (player_mana >= 53):
        stack.append((player_hp, player_armor, player_mana - 53, boss_hp - 4, boss_damage, timers, 1, spent + 53))

    # Cast Drain
    if (player_mana >= 73):
        stack.append((player_hp + 2, player_armor, player_mana - 73, boss_hp - 2, boss_damage, timers, 1, spent + 73))
    
    # Cast Poison
    if (player_mana >= 173 and timers[0] == 0):
        stack.append((player_hp, player_armor, player_mana - 173, boss_hp, boss_damage, (6, timers[1], timers[2]), 1, spent + 173))

    # Cast Shield
    if (player_mana >= 113 and timers[1] == 0):
        stack.append((player_hp, player_armor, player_mana - 113, boss_hp, boss_damage, (timers[0], 6, timers[2]), 1, spent + 113))

    # Cast Recharge
    if (player_mana >= 229 and timers[2] == 0):
        stack.append((player_hp, player_armor, player_mana - 229, boss_hp, boss_damage, (timers[0], timers[1], 5), 1, spent + 229))

print(best_spent)
print(time.time() - start_time)