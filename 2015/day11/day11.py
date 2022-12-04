##########
# PART 1 #
##########

data = open("day11in.txt").read().split("\n")[0]
password = list(data)
while (True):
    rule1, rule2 = False, True
    pairs_counter = {}
    for i in range(len(password)):
        if (i < len(password) - 2):
            if (ord(password[i + 1]) - ord(password[i]) == 1 and ord(password[i + 2]) - ord(password[i + 1]) == 1):
                rule1 = True
        if (i < len(password) - 1):
            if (password[i] == password[i + 1]):
                if (i >= len(password) - 2 or (i < len(password) - 2 and password[i + 1] != password[i + 2])):
                    s = password[i] + password[i + 1]
                    if (s not in pairs_counter): pairs_counter[s] = 0
                    pairs_counter[s] += 1

        if (password[i] in ['i', 'o', 'l']):
            rule2 = False
            break
    
    rule3 = len(pairs_counter) >= 2
    if (rule1 and rule2 and rule3):
        print("".join(password))
        break
    
    # Increment password
    end = True
    for i in range(len(password) - 1, -1, -1):
        if (password[i] == 'z'): password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            end = False
            break
    if (end): break

########## 
# PART 2 #
##########

# Solution to part 1 still works but using the incremented output of a single pass of the sample input.