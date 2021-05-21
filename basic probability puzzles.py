# Basic Probability Puzzles #1
# Objective
# In this challenge, we practice calculating probability.
# Task
# In a single toss of 2 fair (evenly-weighted) 6-sided dice, find the probability of that their sum will be at most 9.
# Output Format
# In the editor below, submit your answer in the form of an irreducible fraction , where  and  are both integers.
# Your answer should resemble something like:
# 3/4
from fractions import Fraction

def target_sum (n):
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6]
    count = 0
    for i in range(6):
        for j in range(6):
            if a[i] + a[j] > n:
                count += 1
    prob = 1- (count * 1 / 6 * 1 / 6)
    fraction_prob = Fraction(prob).limit_denominator(100)
    return fraction_prob
print(target_sum(9))


