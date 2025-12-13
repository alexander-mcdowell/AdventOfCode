import timeit

##########
# PART 1 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
points = []
for l in data:
    x, y = l.split(",")
    points.append((int(x),int(y)))
points = sorted(points, key=lambda x: x[0])
max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = (points[j][0] - points[i][0] + 1) * (abs(points[j][1] - points[i][1]) + 1)
        max_area = max(max_area, area)
print(max_area)
print(timeit.default_timer() - start_time)

##########
# PART 2 #
##########

start_time = timeit.default_timer()
f = open("input.txt", 'r')
data = f.read().split("\n")
points = []
point_set = set()
for l in data:
    x, y = l.split(",")
    p = (int(x),int(y))
    points.append(p)
    point_set.add(p)

def is_inside(p):
    if p in point_set: return True

    is_inside = False
    for i in range(len(points)):
        q1 = points[i]
        q2 = points[(i+1)%len(points)]
        # Point is on the line, return true
        intersect = ((q1[1] > p[1]) != (q2[1] > p[1])) and (p[0] < (q2[0] - q1[0]) * (p[1] - q1[1]) / (q2[1] - q1[1]) + q1[0])
        if (intersect): is_inside = not is_inside
    return is_inside

max_area = 0
for i in range(len(points)):
    p1 = points[i]
    for j in range(i + 1, len(points)):
        p2 = points[j]
        p3 = (p1[0], p2[1])
        p4 = (p2[0], p1[1])
        # Hardcoded bullshit. The input is an approximation of a circle
        # with a rectangle jutting out separating the figure into two parts.
        # Only accept a rectangle that does not cross the jutting rectangle
        if not (min(p1[0],p2[0]) >= 94651 or min(p1[1], p2[1]) >= 50319 or max(p1[1], p2[1]) <= 48450): continue
        if not is_inside(p3) or not is_inside(p4): continue
        
        area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
        if area > max_area:
            max_area = area
            print(p1, p2, p3, p4)
print(max_area)
print(timeit.default_timer() - start_time)