import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# sensor_map = {}
# min_x, max_x = None, None
# for line in lines:
#     line = line.split(" ")
#     sensor, beacon = line[2:4], line[8:]
#     sensor_x, sensor_y = int(sensor[0][2:-1]), int(sensor[1][2:-1])
#     beacon_x, beacon_y = int(beacon[0][2:-1]), int(beacon[1][2:])
#     dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#     sensor_map[(sensor_x, sensor_y)] = [(beacon_x, beacon_y), dist]

#     if (min_x == None or sensor_x - dist < min_x): min_x = sensor_x - dist
#     if (beacon_x < min_x): min_x = beacon_x
#     if (max_x == None or sensor_x + dist > max_x): max_x = sensor_x + dist
#     if (beacon_x > max_x): max_x = beacon_x

# target_y = 2000000
# count = 0
# for x in range(min_x, max_x + 1):
#     valid = False
#     for sensor in sensor_map:
#         beacon, dist = sensor_map[sensor]
#         if ((x, target_y) != beacon and (abs(sensor[0] - x) + abs(sensor[1] - target_y)) <= dist):
#             valid = True
#             break
#     if (valid): count += 1
# print(count)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
sensor_map = {}
for line in lines:
    line = line.split(" ")
    sensor, beacon = line[2:4], line[8:]
    sensor_x, sensor_y = int(sensor[0][2:-1]), int(sensor[1][2:-1])
    beacon_x, beacon_y = int(beacon[0][2:-1]), int(beacon[1][2:])
    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    
    sensor_map[(sensor_x, sensor_y)] = [(beacon_x, beacon_y), dist]

end = False
N = 4000000
sensors_list = list(sensor_map.keys())
for i in range(len(sensor_map)):
    if (end): break
    sensor1, dist = sensors_list[i], sensor_map[sensors_list[i]][1]
    center_x, center_y = sensor1
    dist += 1
    for k in range(min(N - center_x, dist), -dist - 1, -1):
        x = center_x + k
        if (x < 0): break
        y1 = max(0, min(center_y + dist - abs(k), N))
        y2 = min(N, max(center_y - dist + abs(k), 0))

        for y in set([y1, y2]):
            valid = True
            for j in range(len(sensor_map)):
                sensor2, dist2 = sensors_list[j], sensor_map[sensors_list[j]][1]
                if ((abs(x - sensor2[0]) + abs(y - sensor2[1])) <= dist2):
                    valid = False
                    break
            if (valid):
                print(x, y, 4000000 * x + y)
                end = True
                break
        if (end): break
print(time.time() - start_time)