'''
BounceGame
'''

from time import time
from game_base import Actor, Arena, Ball, Ghost, Turtle


class BounceGame:
    def __init__(self):
        self._arena = Arena((480, 360))
        Ball(self._arena, (40, 80))
        Ball(self._arena, (80, 40))
        Ghost(self._arena, (220, 80))
        self._hero = Turtle(self._arena, (80, 80))
        self._start = time()
        self._playtime = 20

    def arena(self) -> Arena:
        return self._arena

    def hero(self) -> Turtle:
        return self._hero

    def game_over(self) -> bool:
        return self._hero.lives() == 0

    def game_won(self) -> bool:
        return time() - self._start > self._playtime

    def remaining_time(self) -> int:
        return int(self._start + self._playtime - time())
