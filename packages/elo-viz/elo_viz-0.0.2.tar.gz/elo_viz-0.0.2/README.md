# Overview
Elo python package to simulate matches between players, and compare their elo ratings after each match, and visualize them. You can use it to simulate rankings of Chess players.

# Installation

Install using pip:

```text
$ pip install elo-viz
```

or with [Poetry](https://python-poetry.org/):

```text
$ poetry add elo-viz
```

# Usage
### Create Players
```py
import uuid
from elo_viz import Match, Player

magnus_carlsen = Player(id=uuid.uuid4().hex, name='Magnus Carlsen', rating=2833)
hou_yifan = Player(id=uuid.uuid4().hex, name='Hou Yifan', rating=2633)
gukesh_d = Player(id=uuid.uuid4().hex, name='Gukesh Dommaraju', rating=2777)
divya_d = Player(id=uuid.uuid4().hex, name='Divya Deshmukh', rating=2490)
```

### Setup Matches
```py
m1 = Match(match_id=uuid.uuid4().hex, player1=magnus_carlsen, player2=gukesh_d)
m1.update_result(winner=magnus_carlsen.id)
```

### Check results
```py
print(m1.player1)
```
Output
```log
Player: Magnus Carlsen Rating: Rating: 2883.0 Win %: 100.0
```

# Requirements
- Python >= 3.13

The version of the base environment I had installed poetry in.

Will update this so that any Python 3 version will work.
