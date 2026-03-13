import abc
import random


class Player(abc.ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        x, y = self.position
        dx, dy = move

        new_position = (x + dx, y + dy)
        self.position = new_position
        self.path.append(new_position)

        return new_position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [
            (0, 1),   # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0)    # right
        ]

    def level_up(self):
        self.moves.extend([
            (1, 1),    # up-right
            (1, -1),   # down-right
            (-1, 1),   # up-left
            (-1, -1)   # down-left
        ])