import random
import numpy as np
import matplotlib.pyplot as plt


ladders = [(32,62), (42,68), (12,98)]
snakes = [(95,13), (97,25), (93,37), (79,27), (75,19), (49,47), (67,17)]
trans = ladders + snakes

trans_matrix = np.zeros((101,101))
for i in range (1,101):
    trans_matrix[i-1,i] = 0.32
    trans_matrix[i-1,i+1:i+2] = 0.32
    trans_matrix[i - 1, i + 2:i + 3] = 0.12
    trans_matrix[i - 1, i + 3:i + 4] = 0.04
    trans_matrix[i - 1, i + 4:i + 5] = 0.07
    trans_matrix[i - 1, i + 5:i + 6] = 0.13

print(trans_matrix)

# for (i1,i2) in trans:
#     print(trans_matrix[i1,i2])
#     prob_dice = [0.32,0.32,0.12,0.04,0.07,0.13]
#     iw = np.where(trans_matrix[:,i1]>0)
#     trans_matrix[:,i1] = 0
#     trans_matrix[iw,i2] += 1/6
# print(trans_matrix[iw,i2])
    # trans_matrix[iw,i2] += random.choice(prob_dice)

position = np.zeros(101)
position [0]= 1

n,P = 0, []
cumulative_prob = 0
while cumulative_prob < 0.99999:
    n +=1
    position = position.dot(trans_matrix)
    P.append(position[100])
    cumulative_prob += P[-1]
mode = np.argmax(P)+1
# print(cumulative_prob)
print(mode)
#
# fig, ax = plt.subplots()
# ax.plot(np.linspace(1,n,n), P, 'g-', lw=2, alpha=0.6, label='Markov')
# ax.set_xlabel('Number of moves')
# ax.set_ylabel('Probability of winning')
#
# plt.show()
# def simulate_game (rseed=None, max_roll=6):
#     rand = Random(rseed)
#     position = 0
#     turns = 0
#     while position < 100:
#         turns += 1
#         roll = rand.randint(1, max_roll)
#         if position + roll > 100:
#             continue
#         position += roll
#         position = ladder_snakes.get(position, position)
#     return turns
# simulate_game(3)

