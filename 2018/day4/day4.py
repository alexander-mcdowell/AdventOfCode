import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt").read().split("\n")
# guard_data = {}
# month_map = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}
# time_to_verbose = {}
# for line in lines:
#     date, info = line[:18], line[19:]
#     date, t = date[1:-1].split(" ")
#     y, m, d = [int(x) for x in date.split('-')]
#     t = [int(x) for x in t.split(":")]
#     t2 = 24 * 60 * month_map[m] + + 24 * 60 * d + t[0] * 60 + t[1]
#     time_to_verbose[t2] = (y, m, d, t)
#     guard_data[t2] = info.split(" ")
# guard_data = {t: guard_data[t] for t in sorted(guard_data)}

# temp = 0
# count = 0
# guard_id = None
# guard_times = {}
# guard_sleep = {}
# for t in guard_data:
#     info = guard_data[t]
#     if (info[-1] == 'shift'):
#         if (guard_id != None):
#             if (guard_id not in guard_times): guard_times[guard_id] = 0
#             guard_times[guard_id] += count
#         guard_id = int(info[1][1:])
#         count = 0
#     elif (info[-1] == 'asleep'):
#         temp = t
#     else:
#         asleep = t - temp
#         interval = (temp % 60, (t - 1) % 60)
#         if (guard_id not in guard_sleep): guard_sleep[guard_id] = [interval]
#         else: guard_sleep[guard_id].append(interval)
#         count += asleep
# if (guard_id not in guard_times): guard_times[guard_id] = 0
# guard_times[guard_id] += count

# best, best_guard = 0, 0
# for guard in guard_times:
#     if (guard_times[guard] > best):
#         best = guard_times[guard]
#         best_guard = guard
# best, best_time = 0, 0
# for t in range(60):
#     count = 0
#     for interval in guard_sleep[best_guard]:
#         if (interval[0] <= t <= interval[1]): count += 1
#     if (count > best):
#         best = count
#         best_time = t
# print(best_guard * best_time)
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt").read().split("\n")
guard_data = {}
month_map = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}
time_to_verbose = {}
guard_ids = set()
for line in lines:
    date, info = line[:18], line[19:]
    date, t = date[1:-1].split(" ")
    y, m, d = [int(x) for x in date.split('-')]
    t = [int(x) for x in t.split(":")]
    t2 = 24 * 60 * month_map[m] + + 24 * 60 * d + t[0] * 60 + t[1]
    time_to_verbose[t2] = (y, m, d, t)
    info = info.split(" ")
    guard_data[t2] = info
    if (info[0] == "Guard"): guard_ids.add(int(info[1][1:]))
guard_data = {t: guard_data[t] for t in sorted(guard_data)}

temp = 0
guard_id = None
guard_sleep = {}
for t in guard_data:
    info = guard_data[t]
    if (info[-1] == 'shift'):
        guard_id = int(info[1][1:])
        if (guard_id not in guard_sleep): guard_sleep[guard_id] = []
    elif (info[-1] == 'asleep'):
        temp = t
    else:
        asleep = t - temp
        interval = (temp % 60, (t - 1) % 60)
        guard_sleep[guard_id].append(interval)
        
best_count, best_time, best_guard = 0, 0, 0
for guard in guard_ids:
    best, best2 = 0, 0
    for t in range(60):
        count = 0
        for interval in guard_sleep[guard]:
            if (interval[0] <= t <= interval[1]): count += 1
        if (count > best):
            best = count
            best2 = t
    if (best > best_count):
        best_count = best
        best_time = best2
        best_guard = guard
print(best_guard * best_time)
print(time.time() - start_time)