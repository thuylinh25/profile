# https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem
# cách 1
import random
from itertools import accumulate

test_cases = int(input())

class Dice:
    def __init__(self, prob):
        self.prob = prob
        self.move = 0
        self.num_prob = [float(n) for n in self.prob.split(",")]
        self.num_prob = list(accumulate(self.num_prob))

    def Roll(self):
        roll = random.random()
        if roll <= self.num_prob[0]:
            self.move = 1
        elif self.num_prob[0] < roll <= self.num_prob[1]:
            self.move = 2
        elif self.num_prob[1] < roll <= self.num_prob[2]:
            self.move = 3
        elif self.num_prob[2] < roll <= self.num_prob[3]:
            self.move = 4
        elif self.num_prob[3] < roll <= self.num_prob[4]:
            self.move = 5
        else:
            self.move = 6
        return self.move


class Board:
    def __init__(self, l_move, s_move, position):
        self.board = [n for n in range(0, 101)]
        self.l_move = [n.split(",") for n in l_move.split(" ")]
        self.s_move = [n.split(",") for n in s_move.split(" ")]
        self.l_dict = {}
        self.position = self.board[position]
        self.end_game = False
        for pack in self.l_move:
            self.l_dict[int(pack[0])] = int(pack[1])
        self.s_dict = {}
        for pack in self.s_move:
            self.s_dict[int(pack[0])] = int(pack[1])
        self.board = [self.l_dict.get(n, n) for n in self.board]
        self.board = [self.s_dict.get(n, n) for n in self.board]

    def Win(self):
        self.end_game = True

    def Move(self, move):
        if self.position + move > 100:
            pass
        elif self.position + move == 100:
            self.Win()
        else:
            self.position += move
        self.position = self.board[self.position]

for _ in range(test_cases):
    lst1 = []
    prob1 = input()
    no_of_ladders, no_of_snakes = map(int, input().split(","))
    l1_move = input()
    s1_move = input()
    for _ in range(5000):
        board = Board(l1_move, s1_move, 1)
        dice = Dice(prob1)
        turn = 0
        while not board.end_game:
            if turn > 1000:
                turn = 1000
                break
            else:
                turn += 1
                board.Move(dice.Roll())
        lst1.append(turn)
    print(round(sum(lst1)/5000))

# Cách 2
import random
def roll(massDist):
    randRoll = random.random() # in [0,1)
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1
T=int(input())
for x in range(0,T):
    sampleMassDist = [float(a) for a in input().split(",")]
    no_of_ladders,no_of_snakes=map(int,input().split(","))
    ladders=[a.split(",") for (a) in input().split()]
    ladder_start=[]
    ladder_end=[]
    for i in ladders:
        ladder_start.append(int(i[0]))
        ladder_end.append(int(i[1]))
    snakes=[a.split(",") for (a) in input().split()]
    snake_start=[]
    snake_end=[]
    for i in snakes:
        snake_start.append(int(i[0]))
        snake_end.append(int(i[1]))
    moves_result=[]
    total=0


    for j in range(5000):
        moves=0
        start=1
        win=True
        while win:
            dice_result=roll(sampleMassDist)
            if not(start+dice_result>100):
                start+=dice_result
            moves+=1
            if start in ladder_start:
                start=ladder_end[ladder_start.index(start)]
            if start in snake_start:
                start=snake_end[snake_start.index(start)]
            if start==100:
                win=False
                total+=1
            if moves==1000:
                break
        moves_result.append(moves)
    print(round(sum(moves_result)/5000))