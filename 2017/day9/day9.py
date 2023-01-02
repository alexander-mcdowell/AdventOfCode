import time

##########
# PART 1 #
##########

# def score_group(group, this_score = 1):
#     if (len(group) == 0): return 0
#     if (group[0] == '{' and group[-1] == '}'):
#         s = ""
#         score = this_score
#         depth = 0
#         lasts = []
#         negated = False
#         negate_i = None
#         for i in range(1, len(group) - 1):
#             if (i == negate_i):
#                 negated = False
#                 negate_i = None
            
#             if (group[i] == ',' and depth == 0 and not negated):
#                 score += score_group(s, this_score + 1)
#                 s = ""
#             else:
#                 if (group[i] in ['{', '<'] and (len(lasts) == 0 or lasts[-1] != '<') and not negated):
#                     lasts.append(group[i])
#                     depth += 1
#                 elif (group[i] == '}' and lasts[-1] == '{' and not negated):
#                     lasts.pop(-1)
#                     depth -= 1
#                 elif (group[i] == '>' and lasts[-1] == '<' and not negated):
#                     lasts.pop(-1)
#                     depth -= 1
#                 elif (group[i] == '!'):
#                     negated = not negated
#                     negate_i = i + 2
#                 s += group[i]
#         if (s != ""): score += score_group(s, this_score + 1)
#         return score
#     else: return 0

# start_time = time.time()
# groups = open("input.txt").read().split("\n")
# score = 0
# for group in groups: 
#     score += score_group(group)
# print(score)
# print(time.time() - start_time)

##########
# PART 2 #
##########

def count_garbage(group):
    if (len(group) == 0): return 0
    if (group[0] == '{' and group[-1] == '}'):
        s = ""
        garbage = 0
        depth = 0
        lasts = []
        negated = False
        negate_i = None
        for i in range(1, len(group) - 1):
            if (i == negate_i):
                negated = False
                negate_i = None
            
            if (group[i] == ',' and depth == 0 and not negated):
                garbage += count_garbage(s)
                s = ""
            else:
                if (group[i] in ['{', '<'] and (len(lasts) == 0 or lasts[-1] != '<') and not negated):
                    lasts.append(group[i])
                    depth += 1
                elif (group[i] == '}' and lasts[-1] == '{' and not negated):
                    lasts.pop(-1)
                    depth -= 1
                elif (group[i] == '>' and lasts[-1] == '<' and not negated):
                    lasts.pop(-1)
                    depth -= 1
                elif (group[i] == '!'):
                    negated = not negated
                    negate_i = i + 2
                s += group[i]
        if (s != ""): garbage += count_garbage(s)
        return garbage
    elif (group[0] == '<' and group[-1] == '>'):
        s = ""
        garbage = 0
        i = 1
        while (i < len(group) - 1):
            if (group[i] == '!'): i += 2
            else:
                s += group[i]
                i += 1
        return len(s)
    else: return 0

start_time = time.time()
groups = open("input.txt").read().split("\n")
garbage = 0
for group in groups: 
    garbage += count_garbage(group)
print(garbage)
print(time.time() - start_time)