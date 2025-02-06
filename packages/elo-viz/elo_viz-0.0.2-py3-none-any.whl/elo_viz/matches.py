import random

from elo_viz.constants import RESULT_DRAW, RESULT_WIN, RESULT_LOSS
from elo_viz.player import Player


class Match:
    def __init__(self, match_id: str, player1: Player, player2: Player):
        self.id = match_id
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.is_draw = False

    def pick_random_winner(self):
        random_number = random.randint(1, 100)
        if random_number <= 33:
            self.winner = self.player1.id
        elif 33 < random_number <= 66:
            self.is_draw = True
        else:
            self.winner = self.player2.id
        
        self.update_rating()

    def update_result(self, winner: int = None, is_draw: bool = False):
        if is_draw is True:
            self.is_draw = is_draw
        else:
            self.winner = winner

        self.update_rating()

    def update_rating(self):
        if self.is_draw is True:
            player1_result = RESULT_DRAW
            player2_result = RESULT_DRAW
        elif self.winner == self.player1.id:
            player1_result = RESULT_WIN
            player2_result = RESULT_LOSS
        elif self.winner == self.player2.id:
            player1_result = RESULT_LOSS
            player2_result = RESULT_WIN

        self.player1.update_rating(self.player2, result=player1_result)
        self.player2.update_rating(self.player1, result=player2_result)

    def display_result(self):
        if self.is_draw is True:
            print(self.player1.name, ' drew with ', self.player2.name)
        elif self.winner == self.player1.id:
            print(self.player1.name, ' won against ', self.player2.name)
        elif self.winner == self.player2.id:
            print(self.player2.name, ' won against ', self.player1.name)

    def to_dict(self):
        return {
            'id': self.id, 'player1': self.player1.to_dict(), 'player2': self.player2.to_dict(),
            'winner': self.winner, 'is_draw': self.is_draw
        }
