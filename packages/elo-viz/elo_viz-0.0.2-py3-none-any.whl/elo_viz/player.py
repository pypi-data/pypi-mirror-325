from elo_viz.constants import RESULT_DRAW, RESULT_WIN, RESULT_LOSS, DEFAULT_RATING
from elo_viz.rating import Rating, calculate_rating


class Player:
    def __init__(self, id: str, name: str, rating: int = DEFAULT_RATING, variability: float = 1.0):
        self.id = id
        self.name = name
        self.rating = Rating(rating)
        self.variability = variability
        self.matches = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def update_rating(self, opponent, result):

        if result not in [RESULT_WIN, RESULT_LOSS, RESULT_DRAW]:
            raise ValueError("Incorrect value for result parameter!")

        self.matches += 1

        self.rating = calculate_rating(self.rating, opponent.rating, result)
        self.wins += 1 if result == RESULT_WIN else 0
        self.losses += 1 if result == RESULT_LOSS else 0
        self.draws += 1 if result == RESULT_DRAW else 0

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'rating': float(self.rating),
            'matches': self.matches, 'wins': self.wins, 'losses': self.losses, 'draws': self.draws
        }

    def __str__(self):
        if self.matches:
            win_percentage = self.wins / self.matches * 100
        else:
            win_percentage = 0
        return "Player: {name} Rating: {rating} Win %: {win_percentage}".format(
            name=self.name, rating=self.rating, win_percentage=win_percentage
        )

    def __eq__(self, other):
        return self.id == other.id
