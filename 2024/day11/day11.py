import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
state = [int(x) for x in f.read().split("\n")[0].split(" ")]
N = 25
for _ in range(N):
    new_state = []
    for x in state:
        if (x == 0): new_state.append(1)
        else:
            s = str(x)
            l = len(s)
            if (l % 2 == 0):
                new_state.append(int(s[:l//2]))
                new_state.append(int(s[l//2:]))
            else: new_state.append(x * 2024)
    state = new_state
print(len(state))
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
f = open("input.txt", 'r')
state = [int(x) for x in f.read().split("\n")[0].split(" ")]
state_freqs = {}
for x in state:
    if (x not in state_freqs): state_freqs[x] = 1
    else: state_freqs[x] += 1

N = 75
state = state_freqs
for i in range(N):
    new_state = {}
    for x in state:
        if (x == 0):
            if (1 not in new_state): new_state[1] = state[x]
            else: new_state[1] += state[x]
        else:
            s = str(x)
            l = len(s)
            if (l % 2 == 0):
                y = int(s[:l//2])
                if (y not in new_state): new_state[y] = state[x]
                else: new_state[y] += state[x]
                
                y = int(s[l//2:])
                if (y not in new_state): new_state[y] = state[x]
                else: new_state[y] += state[x]
            else:
                y = x * 2024
                if (y not in new_state): new_state[y] = state[x]
                else: new_state[y] += state[x]
    state = new_state
count = 0
for x in state:
    count += state[x]
print(count)
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")