import uuid
from random import randint, choice
from typing import List
from elo_viz.constants import DEFAULT_RATING, CHESS_PLAYERS
from elo_viz.player import Player
from elo_viz.rating import Rating
from elo_viz.matches import Match

class Elo:

    def __init__(self, players: List[Player], verbose=False):
        self.players = players
        self.matches = []
        self.verbose = verbose

    def add_player(self, player: Player):
        self.players.append(player)

    def random_match(self):
        p1 = choice(self.players)
        p2 = p1
        while p1 == p2:
            p2 = choice(self.players)
        m = self.match(p1, p2)
        m.display_result()
        self.matches.append(m.to_dict())

    def match(self, p1: Player, p2: Player):
        match = Match(match_id=uuid.uuid4().hex, player1=p1, player2=p2)
        match.pick_random_winner()
        return match

    def print_ranks(self):
        print()
        s = sorted(self.players, key=lambda a: a.rating, reverse=True)
        for i, player in enumerate(s):
            print(i+1, player)


class EloChess:

    def __init__(self, players):
        if players > 100:
            players = 100
        self.players = [Player(uuid.uuid4().hex, CHESS_PLAYERS[i][0], CHESS_PLAYERS[i][2]) for i in range(players)]
        self.matches = []
        self.output_match = True

    def random_match(self):
        p1 = choice(self.players)
        p2 = p1
        while p1 == p2:
            p2 = choice(self.players)
        m = self.match(p1, p2)
        m.display_result()
        self.matches.append(m.to_dict())

    def match(self, p1: Player, p2: Player):
        match = Match(match_id=uuid.uuid4().hex, player1=p1, player2=p2)
        match.pick_random_winner()
        return match

    def print_ranks(self):
        print()
        s = sorted(self.players, key=lambda a: a.rating, reverse=True)
        for i, player in enumerate(s):
            print(i+1, player)


def main():
    e = EloChess(30)
    fast = True
    e.output_match = not fast
    matches = 0
    total_matches_to_simulate = 100
    while 1:
        matches += 1
        e.random_match()
        if fast and (matches % 100000):
            continue
        e.print_ranks()
        if matches > total_matches_to_simulate:
            break


if __name__ == '__main__':
    main()
