import time

##########
# PART 1 #
##########

start_time = time.time()
f = open("input.txt", 'r')
data = f.read().split("\n")
rules = {}
i = 0
while i < len(data):
    line = data[i]
    if (line == ""):
        i += 1
        break
    rule_name, rule = line.split("{")
    rule = rule[:-1].split(",")
    for j in range(len(rule)):
        x = rule[j]
        if ('>' in x):
            condition, target = x.split(":")
            variable, val = condition.split(">")
            val = int(val)
            y = (variable, 0, val, target)
            rule[j] = y
        elif ('<' in x):
            condition, target = x.split(":")
            variable, val = condition.split("<")
            val = int(val)
            y = (variable, 1, val, target)
            rule[j] = y
        else: rule[j] = x
    rules[rule_name] = rule
    i += 1

variables = {}
total = 0
while i < len(data):
    vars = data[i][1:-1].split(",")
    for v in vars:
        name, value = v.split("=")
        value = int(value)
        variables[name] = value
    curr = 'in'
    while curr not in ['A', 'R']:
        found = False
        for clause in rules[curr][:-1]:
            x, y = variables[clause[0]], clause[2]
            if ((clause[1] == 0 and x > y) or (clause[1] == 1 and x < y)):
                found = True
                curr = clause[-1]
                break
        if (not found): curr = rules[curr][-1]
    if (curr == 'A'):
        for v in variables: total += variables[v]
    i += 1
print(total)
print("Part 1 finished in " + str(time.time() - start_time) + " seconds.")

##########
# PART 2 #
##########

start_time = time.time()
# Reverse rule dictionary:
# target rule --> [(source rule, condition), ...]
reverse_rule = {}
for source_rule in rules:
    negated = []
    for x in rules[source_rule]:
        if (type(x) == tuple):
            target_rule = x[3]
            condition = negated + [(x[0], x[1], x[2])]
            # 2 --> <=, 3 --> >=
            negated.append((x[0], x[1] + 2, x[2]))
        else:
            target_rule = x
            condition = negated
        if (target_rule not in reverse_rule): reverse_rule[target_rule] = []
        reverse_rule[target_rule].append((source_rule, condition))

def backtrack(source, target, curr = []):
    if (source == target):
        # Restrictions maps every variable to a lower and upper bound (inclusive)
        restrictions = {v: [1, 4000] for v in variables}
        for condition in curr:
            l, u = 1, 4000
            # >
            if (condition[1] == 0): l = condition[2] + 1
            # <
            elif (condition[1] == 1): u = condition[2] - 1
            # <=
            elif (condition[1] == 2): u = condition[2]
            # >=
            else: l = condition[2]
            
            old_l, old_u = restrictions[condition[0]]
            temp = [max(old_l, l), min(old_u, u)]
            if (temp[0] > temp[1]): return 0
            restrictions[condition[0]] = temp
        total = 1
        for v in variables:
            restrict = restrictions[v]
            total *= restrict[1] - restrict[0] + 1
        return total

    if (source not in reverse_rule): return 0
    total = 0
    for x in reverse_rule[source]:
        total += backtrack(x[0], target, curr + x[1])
    return total

print(backtrack('A', 'in'))  
print("Part 2 finished in " + str(time.time() - start_time) + " seconds.")