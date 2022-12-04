##############
# PART 1 & 2 #
##############

# Solved by hand using the following model.
# Player: 100 hp, x damage, y armor
# Boss (Puzzle Input): 103 hp, 9 damage, 2 armor

# To minimize, we find the cost-combination such that:
# 103/(x - 2) <= 100/(9 - y)
# Simplifying: 11.27 <= x + 1.03y
# After testing damage-armor-cost combinations, we get (x, y) = (9, 2), cost = 121

# To maximize. we use a similar inequality, this time with 11.27 > x + 1.03y
# After testing damage-armor-cost combinations, we get (x, y) = (7, 4), cost = 201