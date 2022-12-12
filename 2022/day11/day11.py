import time

##########
# PART 1 #
##########

# start_time = time.time()
# lines = open("input.txt", "r+").read().split("\n")
# monkey_items = []
# monkey_ops = []
# monkey_tests = []
# for i in range(len(lines)//7):
#     data = lines[7 * i + 1 : 7 * (i + 1) - 1]

#     items = []
#     for x in data[0][2:].split(" ")[2:]:
#         x = x.replace(",", "")
#         if (x != ""): items.append(int(x))
#     monkey_items.append(items)

#     op = data[1].split(" ")[-3:]
#     monkey_ops.append(op)
    
#     div_num = int(data[2][2:].split(" ")[-1])
#     pass_true = int(data[3][2:].split(" ")[-1])
#     pass_false = int(data[4][2:].split(" ")[-1])
#     test = [div_num, pass_true, pass_false]
#     monkey_tests.append(test)

# N = 20
# monkey_counts = [0 for k in range(len(monkey_items))]
# for _ in range(N):
#     for i in range(len(monkey_items)):
#         while (len(monkey_items[i]) != 0):
#             val = monkey_items[i].pop(0)
#             op = monkey_ops[i]
#             test = monkey_tests[i]

#             if (op[0] == "old"): a = val
#             else: a = int(op[0])
#             if (op[2] == "old"): b = val
#             else: b = int(op[2])
            
#             if (op[1] == "+"): val = (a + b) // 3
#             elif (op[1] == "-"): val = (a - b) // 3
#             else: val = (a * b) // 3
            
#             if (val % test[0] == 0): pass_to = test[1]
#             else: pass_to = test[2]
#             monkey_items[pass_to].append(val)
#             monkey_counts[i] += 1

# monkey_counts = sorted(monkey_counts)
# print(monkey_counts)
# print(monkey_counts[-1] * monkey_counts[-2])
# print(time.time() - start_time)

##########
# PART 2 #
##########

start_time = time.time()
lines = open("input.txt", "r+").read().split("\n")
monkey_items = []
monkey_ops = []
monkey_tests = []
for i in range(len(lines)//7):
    data = lines[7 * i + 1 : 7 * (i + 1) - 1]

    items = []
    for x in data[0][2:].split(" ")[2:]:
        x = x.replace(",", "")
        if (x != ""): items.append(int(x))
    monkey_items.append(items)

    op = data[1].split(" ")[-3:]
    monkey_ops.append(op)
    
    div_num = int(data[2][2:].split(" ")[-1])
    pass_true = int(data[3][2:].split(" ")[-1])
    pass_false = int(data[4][2:].split(" ")[-1])
    test = [div_num, pass_true, pass_false]
    monkey_tests.append(test)

N = 10000
monkey_counts = [0 for k in range(len(monkey_items))]
big_mod = 1
for i in range(len(monkey_items)): big_mod = (big_mod * monkey_tests[i][0])
for _ in range(N):
    for i in range(len(monkey_items)):
        op = monkey_ops[i]
        test = monkey_tests[i]
        while (len(monkey_items[i]) != 0):
            val = monkey_items[i].pop(0) % big_mod

            if (op[0] == "old"): a = val
            else: a = int(op[0]) % big_mod
            if (op[2] == "old"): b = val
            else: b = int(op[2]) % big_mod
            
            if (op[1] == "+"): val = (a + b) % big_mod
            elif (op[1] == "-"): val = (a - b) % big_mod
            else: val = (a * b) % big_mod
            
            if (val % test[0] == 0): pass_to = test[1]
            else: pass_to = test[2]
            monkey_items[pass_to].append(val)
            monkey_counts[i] += 1

monkey_counts = sorted(monkey_counts)
print(monkey_counts)
print(monkey_counts[-1] * monkey_counts[-2])
print(time.time() - start_time)