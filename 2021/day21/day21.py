##########
# PART 1 #
##########

"""
data = open("day21in.txt").read().split("\n")
player1 = int(data[0].split("Player 1 starting position: ")[1])
player1_score = 0
player2 = int(data[1].split("Player 2 starting position: ")[1])
player2_score = 0

counter = 1
turn = 0
rolls = 0
while (not (player1_score >= 1000 or player2_score >= 1000)):
    if (turn == 0):
        player1 = (player1 + counter) % 10
        if (player1 == 0): player1 += 10
    else:
        player2 = (player2 + counter) % 10
        if (player2 == 0): player2 += 10
    
    counter += 1
    if (counter == 101): counter = 1
    rolls += 1
    if (rolls % 3 == 0):
        if (turn == 0): player1_score += player1
        else: player2_score += player2
        turn = 1 - turn

print(rolls, player1_score, player2_score)
print(min(player1_score, player2_score) * rolls)
"""

##########
# PART 2 #
##########

def multiply(matrix, vector):
    # Multiply is a matrix-vector product but it also adds score distributions
    product = []
    count = 0
    for i in range(len(matrix)):
        k = sum(vector[i][1])
        if (k == vector[i][1][-1] and k > 0):
            product.append(vector[i])
            count += 1
            continue
        
        x = 0
        y = [0 for _ in range(22)]
        for j in range(len(matrix[i])):
            s = matrix[i][j] * vector[j][0]
            x += s
            if (s != 0):
                for k in range(22): y[k] += vector[j][1][k]
        product.append((x, y))
    return product, count == len(matrix)
        
data = open("day21in.txt").read().split("\n")
player1 = int(data[0].split("Player 1 starting position: ")[1])
player1 = [(0 if i != player1 else 1, [1] + [0 for _ in range(21)]) for i in range(10)]
player2 = int(data[1].split("Player 2 starting position: ")[1])
player2 = [(0 if i != player2 else 1, [1] + [0 for _ in range(21)]) for i in range(10)]

transition_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]

stop1, stop2 = False, False
while (not (stop1 and stop2)):
    if (not stop1):
        # Roll the dice three times to get a list of the universes for each possible position.
        for _ in range(3):
            player1, stop1 = multiply(transition_matrix, player1)
            if (stop1): break
        # Adjust scores.
        for i in range(len(player1)):
            if (player1[i][0] != 0):
                new_score = [0 for _ in range(22)]
                # Shift the score distribution for the ith position by i.
                # Anything at or above 21 simply gets added to 21 or stays at 21.
                for j in range(22):
                    k = j + (i + 1)
                    if (k < 21): new_score[k] = player1[i][1][j]
                    else: new_score[21] += player1[i][1][j]
                player1[i] = (player1[i][0], new_score)
    
    print("Player 1:")
    for x in player1:
        print(x)
    print()
    
    if (not stop2):
        # Do the same for player 2
        for _ in range(3):
            player2, stop2 = multiply(transition_matrix, player2)
            if (stop2): break 
        for i in range(len(player2)):
            if (player2[i][0] != 0):
                new_score = [0 for _ in range(22)]
                for j in range(22):
                    k = j + (i + 1)
                    if (k < 21): new_score[k] = player2[i][1][j]
                    else: new_score[21] += player2[i][1][j]
                player2[i] = (player2[i][0], new_score)
    
    print("Player 2:")
    for x in player2:
        print(x)
    print()

s1, s2 = 0, 0
for i in range(10):
    s1 += player1[i][1][-1]
    s2 += player2[i][1][-1]
print(s1, s2)

"""
def branch(player1_pos, player2_pos, player1_score, player2_score, turn, counter = 0):
    if (turn):
        if (player1_pos > 10): player1_pos %= 10
        if (counter == 3):
            player1_score += player1_pos
            counter = 0
            if (player1_score >= 21): return (1, 0)
            
            x, y = 0, 0
            for i in range(1, 4):
                kx, ky = branch(player1_pos, player2_pos + i, player2_score, player2_score, 1 - turn, counter + 1)
                x += kx
                y += ky
            return (x, y)
        else:
            x, y = 0, 0
            for i in range(1, 4):
                kx, ky = branch(player1_pos + i, player1_score, player2_pos, player2_score, turn, counter + 1)
                x += kx
                y += ky
            return (x, y)
    else:
        if (player2_pos > 10): player2_pos %= 10
        if (counter == 3):
            player2_score += player2_pos
            counter = 0
            if (player2_score >= 21): return (0, 1)
            
            x, y = 0, 0
            for i in range(1, 4):
                kx, ky = branch(player1_pos + i, player2_pos, player2_score, player2_score, 1 - turn, counter + 1)
                x += kx
                y += ky
            return (x, y)
        else:
            x, y = 0, 0
            for i in range(1, 4):
                kx, ky = branch(player1_pos, player1_score, player2_pos + i, player2_score, turn, counter + 1)
                x += kx
                y += ky
            return (x, y)

data = open("day21in.txt").read().split("\n")
player1 = int(data[0].split("Player 1 starting position: ")[1])
player2 = int(data[1].split("Player 2 starting position: ")[1])
player1_score, player2_score = 0, 0

print(branch(player1, player2, player1_score, player2_score, 0))
"""