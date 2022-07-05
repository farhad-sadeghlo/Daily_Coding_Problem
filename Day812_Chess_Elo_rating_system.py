D = 400
K = 32
import math


class Elo:

    def __init__(self, player_A_ratio, player_B_ratio, ifAiswinner):

        self.Ra = int(player_A_ratio)
        self.Rb = int(player_B_ratio)
        self.winner = int(ifAiswinner)

    @property
    def probability(self):
        if self.winner == 1:
            return 1 / (1 + math.pow(10, ((self.Rb - self.Ra) / D)))
        elif self.winner == 0:
            return 1 / (1 + math.pow(10, ((self.Ra - self.Rb) / D)))

    @property
    def get_rating(self):

        if self.winner == 1:
            self.Ra = self.Ra + K * (1 - self.probability)
            self.Rb = self.Rb + K * (0 - self.probability)
            return f'Player A wins and the new rating for player A is {self.Ra} and for player B is {self.Rb}'

        elif self.winner == 0:
            self.Ra = self.Ra + K * (0 - self.probability)
            self.Rb = self.Rb + K * (1 - self.probability)
            return f'Player B wins and the new rating for player A is {self.Ra} and player B is {self.Rb}'
