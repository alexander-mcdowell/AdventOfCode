##########
# PART 1 #
##########

data = open("day25in.txt").read().split("\n")[0].split(" ")
target = (int(data[-3][:-1]), int(data[-1][:-1]))
N = sum(target)
grid = [[0 for _ in range(N - 1)] for _ in range(N - 1)]
grid[0][0] = 20151125

last = grid[0][0]
end = False
for n in range(3, N + 1):
    for i in range(n - 1, 0, -1):
        j = n - i
        grid[i - 1][j - 1] = (last * 252533) % 33554393
        last = grid[i - 1][j - 1]
        if (i == target[0] and j == target[1]):
            end = True
            break
    if (end): break
print(last)

##########
# PART 2 #
##########

# There is no puzzle for part 2.