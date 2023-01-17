###############
# PARTS 1 & 2 #
###############

import time

start_time = time.time()
lines = open("input.txt").read().split("\n")
particles = []
for line in lines:
    line = line.split("> ")
    posx, posy = [int(x) for x in line[0][10:].split(", ")]
    velx, vely = [int(x) for x in line[1][10:-1].split(", ")]
    particles.append([posx, posy, velx, vely])

max_t = 100000
for t in range(1, max_t + 1):
    min_x, max_x, min_y, max_y = -1, -1, -1, -1
    for i in range(len(particles)):
        posx, posy, velx, vely = particles[i]
        posx += velx
        posy += vely
        particles[i] = [posx, posy, velx, vely]
        if (min_x == -1 or posx < min_x): min_x = posx
        if (max_x == -1 or posx > max_x): max_x = posx
        if (min_y == -1 or posy < min_y): min_y = posy
        if (max_y == -1 or posy > max_y): max_y = posy

    if (max_y - min_y <= 15):
        print("Time: ", t, (min_x, max_x, min_y, max_y))
        dx = max_x - min_x
        dy = max_y - min_y
        grid = [['.' for _ in range(dx + 1)] for _ in range(dy + 1)]
        for particle in particles:
            grid[particle[1] - min_y][particle[0] - min_x] = '#'
        for row in grid: print(''.join(row))
        break
print(time.time() - start_time)