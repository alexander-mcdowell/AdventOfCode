##########
# PART 1 #
##########

import time

def recurse(player_hp, player_armor, player_mana, boss_hp, boss_damage, timers = (0, 0, 0), turn = 0):
    if (turn == 1):
        # Poison timer
        if (timers[0] != 0): boss_hp -= 3
        # Shield Timer
        if (timers[1] != 0): player_armor = 7
        else: player_armor = 0
        # Recharge Timer
        if (timers[2] != 0): player_mana += 101
        
        # Check if boss is dead
        if (boss_hp <= 0): return 0, True
        
        # Deal damage
        player_hp -= max(boss_damage - player_armor, 1)
        if (player_hp <= 0): return 0, False
        
        timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))
        turn = 0

    # Poison timer
    if (timers[0] != 0): boss_hp -= 3
    # Shield Timer
    if (timers[1] != 0): player_armor = 7
    else: player_armor = 0
    # Recharge Timer
    if (timers[2] != 0): player_mana += 101
    
    # Check if the boss is dead
    if (boss_hp <= 0): return 0, True
    
    timers = (max(timers[0] - 1, 0), max(timers[1] - 1, 0), max(timers[2] - 1, 0))

    options = []
    # Cast Magic Missile
    if (player_mana >= 53):
        expended, win = recurse(player_hp, player_armor, player_mana - 53, boss_hp - 4, boss_damage, timers, 1)
        if (win): options.append(expended + 53)

    # Cast Drain
    if (player_mana >= 73):
        expended, win = recurse(player_hp + 2, player_armor, player_mana - 73, boss_hp - 2, boss_damage, timers, 1)
        if (win): options.append(expended + 73)
    
    # Cast Poison
    if (player_mana >= 173 and timers[0] == 0):
        expended, win = recurse(player_hp, player_armor, player_mana - 173, boss_hp, boss_damage, (6, timers[1], timers[2]), 1)
        if (win): options.append(expended + 173)

    # Cast Shield
    if (player_mana >= 113 and timers[1] == 0):
        expended, win = recurse(player_hp, player_armor, player_mana - 113, boss_hp, boss_damage, (timers[0], 6, timers[2]), 1)
        if (win): options.append(expended + 113)

    # Cast Recharge
    if (player_mana >= 229 and timers[2] == 0):
        expended, win = recurse(player_hp, player_armor, player_mana - 229, boss_hp, boss_damage, (timers[0], timers[1], 5), 1)
        if (win): options.append(expended + 229)
    
    if (len(options) == 0): return 0, False
    else: return min(options), True

data = open("day22in.txt").read().split("\n")
boss_hp = int(data[0].replace("Hit Points: ", ""))
boss_damage = int(data[1].replace("Damage: ", ""))

start_time = time.time()
mana, win = recurse(50, 0, 500, boss_hp, boss_damage)
if (win): print(mana)
else: print("Player does not win.")
print(time.time() - start_time)