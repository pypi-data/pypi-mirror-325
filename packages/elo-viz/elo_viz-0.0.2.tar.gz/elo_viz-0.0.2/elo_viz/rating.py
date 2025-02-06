from elo_viz.constants import EloConstant, DEFAULT_RATING, RESULT_TO_SCORE


class Rating:
    def __init__(self, value=None):
        if value is None:
            value = DEFAULT_RATING
        self.value = float(value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __eq__(self, other):
        return float(self) == float(other)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __add__(self, other):
        self.value += other
        return self

    def __sub__(self, other):
        self.value -= other
        return self

    def __str__(self):
        return "Rating: {}".format(str(self.value))

    # def __repr__(self):
    #     return "Rating(value={})".format(str(self.value))


def calculate_expected_score(rating1: Rating, rating2: Rating) -> float:
    expected_score = 1 / (1 + 10 ** ((float(rating2) - float(rating1)) / 400))
    return expected_score


def calculate_rating_from_expected_score(rating: Rating, expected_score: float, result: str) -> Rating:
    score = RESULT_TO_SCORE[result]
    rating += EloConstant.K * (score - expected_score)
    return rating


def calculate_rating(rating1: Rating, rating2: Rating, result: str) -> Rating:
    expected_score = calculate_expected_score(rating1, rating2)
    rating1 = calculate_rating_from_expected_score(
        rating1, expected_score, result)
    return rating1
