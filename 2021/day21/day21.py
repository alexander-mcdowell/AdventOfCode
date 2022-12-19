import time

##########
# PART 1 #
##########

# data = open("day21in.txt").read().split("\n")
# player1 = int(data[0].split("Player 1 starting position: ")[1])
# player1_score = 0
# player2 = int(data[1].split("Player 2 starting position: ")[1])
# player2_score = 0

# counter = 1
# turn = 0
# rolls = 0
# while (not (player1_score >= 1000 or player2_score >= 1000)):
#     if (turn == 0):
#         player1 = (player1 + counter) % 10
#         if (player1 == 0): player1 += 10
#     else:
#         player2 = (player2 + counter) % 10
#         if (player2 == 0): player2 += 10
    
#     counter += 1
#     if (counter == 101): counter = 1
#     rolls += 1
#     if (rolls % 3 == 0):
#         if (turn == 0): player1_score += player1
#         else: player2_score += player2
#         turn = 1 - turn

# print(rolls, player1_score, player2_score)
# print(min(player1_score, player2_score) * rolls)

##########
# PART 2 #
##########

def N1(pos1, score1, pos2, score2):
    win_dict = {}
    win_dict2 = {}
    
    def roll1(pos1, score1, pos2, score2, counter):        
        if (counter == 3):
            score1_prime = score1 + pos1
            
            if ((pos1, score1_prime, pos2, score2) in win_dict):
                return win_dict[(pos1, score1_prime, pos2, score2)]
            
            if (score1_prime >= 21): wins = 1
            else: wins = roll2(pos1, score1_prime, pos2, score2, 0)
            win_dict[(pos1, score1_prime, pos2, score2)] = wins
            return wins

        wins = 0
        for k in range(1, 4):
            pos1_prime = pos1 + k
            pos1_prime = pos1_prime if pos1_prime <= 10 else pos1_prime - 10
            wins += roll1(pos1_prime, score1, pos2, score2, counter + 1)
        return wins

    def roll2(pos1, score1, pos2, score2, counter):
        if (counter == 3):
            score2_prime = score2 + pos2
            
            if ((pos1, score1, pos2, score2_prime) in win_dict2):
                return win_dict2[(pos1, score1, pos2, score2_prime)]
            
            wins = 0
            if (score2_prime < 21): wins = roll1(pos1, score1, pos2, score2_prime, 0)
            win_dict2[(pos1, score1, pos2, score2_prime)] = wins
            return wins

        wins = 0
        for k in range(1, 4):
            pos2_prime = pos2 + k
            pos2_prime = pos2_prime if pos2_prime <= 10 else pos2_prime - 10
            wins += roll2(pos1, score1, pos2_prime, score2, counter + 1)
        return wins
    
    return roll1(pos1, score1, pos2, score2, 0)

def N2(pos1, score1, pos2, score2):
    win_dict = {}
    win_dict2 = {}
    
    def roll1(pos1, score1, pos2, score2, counter):        
        if (counter == 3):
            score1_prime = score1 + pos1
            
            if ((pos1, score1_prime, pos2, score2) in win_dict):
                return win_dict[(pos1, score1_prime, pos2, score2)]
            
            wins = 0
            if (score1_prime < 21): wins = roll2(pos1, score1_prime, pos2, score2, 0)
            win_dict[(pos1, score1_prime, pos2, score2)] = wins
            return wins

        wins = 0
        for k in range(1, 4):
            pos1_prime = pos1 + k
            pos1_prime = pos1_prime if pos1_prime <= 10 else pos1_prime - 10
            wins += roll1(pos1_prime, score1, pos2, score2, counter + 1)
        return wins

    def roll2(pos1, score1, pos2, score2, counter):
        if (counter == 3):
            score2_prime = score2 + pos2
            
            if ((pos1, score1, pos2, score2_prime) in win_dict2):
                return win_dict2[(pos1, score1, pos2, score2_prime)]
            
            if (score2_prime >= 21): wins= 1
            else: wins = roll1(pos1, score1, pos2, score2_prime, 0)
            win_dict2[(pos1, score1, pos2, score2_prime)] = wins
            return wins

        wins = 0
        for k in range(1, 4):
            pos2_prime = pos2 + k
            pos2_prime = pos2_prime if pos2_prime <= 10 else pos2_prime - 10
            wins += roll2(pos1, score1, pos2_prime, score2, counter + 1)
        return wins
    
    return roll1(pos1, score1, pos2, score2, 0)

start_time = time.time()
data = open("day21in.txt").read().split("\n")
player1 = int(data[0].split("Player 1 starting position: ")[1])
player2 = int(data[1].split("Player 2 starting position: ")[1])
print(max(N1(player1, 0, player2, 0), N2(player1, 0, player2, 0)))
print(time.time() - start_time)