import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# particles = []
# for line in lines:
#     line = line.split(", ")
#     pos, vel, accel = line
#     pos = [int(x) for x in pos[3:-1].split(",")]
#     vel = [int(x) for x in vel[3:-1].split(",")]
#     accel = [int(x) for x in accel[3:-1].split(",")]
#     particles.append([pos, vel, accel])

# closest_counts = [0 for _ in range(len(particles))]
# while True:
#     closest, closest_dist = None, -1
#     for i in range(len(particles)):
#         particle = particles[i]
#         pos, vel, accel = particle
#         vel = [vel[j] + accel[j] for j in range(3)]
#         pos = [pos[j] + vel[j] for j in range(3)]
#         particles[i] = [pos, vel, accel]
#         dist = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
        
#         if (closest_dist == -1 or dist < closest_dist):
#             closest_dist = dist
#             closest = i
#     closest_counts[closest] += 1
#     if (max(closest_counts) == 1000):
#         print(closest)
#         break
# print(time.time() - start_time)

##########
# PART 2 #
##########

import math

# def intersect(a1, a2, v1, v2, p1, p2):
#     A = (a1 - a2)/2
#     B = v1 - v2
#     C = p1 - p2
#     if (A == 0):
#         if (B == 0): return [-1] if C == 0 else None
#         t = -C/B
#         if (t < 0): return None
#         return [t]
#     discrim = B * B - 4 * A * C
#     if (discrim < 0): return None
#     if (discrim == 0):
#         if (B > 0): return None
#         return [-B/(2 * A)]
#     t1, t2 = (-B + math.sqrt(discrim))/(2 * A), (-B - math.sqrt(discrim))/(2 * A)
#     if (t1 < 0 and t2 < 0): return None
#     if (t1 < 0): return [t2]
#     if (t2 < 0): return [t1]
#     return [t1, t2]

start_time = time.time()
lines = open("input.txt").read().split("\n")
particles = []
for line in lines:
    line = line.split(", ")
    pos, vel, accel = line
    pos = [int(x) for x in pos[3:-1].split(",")]
    vel = [int(x) for x in vel[3:-1].split(",")]
    accel = [int(x) for x in accel[3:-1].split(",")]
    particles.append([pos, vel, accel])

poses = []
collide = []
for i in range(len(particles)):
    particle = particles[i]
    pos, _, _ = particle
    if (pos in poses):
        collide.append(i)
        collide.append(poses.index(pos))
        poses.append(None)
    else: poses.append(pos)
for i in collide: particles[i] = None

for _ in range(1000):
    poses = []
    collide = []
    for i in range(len(particles)):
        particle = particles[i]
        if (particle == None):
            poses.append(None)
            continue
        pos, vel, accel = particle
        vel = [vel[j] + accel[j] for j in range(3)]
        pos = [pos[j] + vel[j] for j in range(3)]
        if (pos in poses):
            collide.append(i)
            collide.append(poses.index(pos))
            poses.append(None)
        else:
            particles[i] = [pos, vel, accel]
            poses.append(pos)
    for i in collide: particles[i] = None
print(len(particles) - particles.count(None))
print(time.time() - start_time)