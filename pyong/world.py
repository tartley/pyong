from gameitem import GameItem
from shapes import Rect

class World(object):

    _next_id = 0

    def __init__(self):
        self.items = {}

    def add(self, item, x, y):
        item.x, item.y = x, y
        self.items[World._next_id] = item
        World._next_id += 1

def populate(world):

    white = (1, 1, 1, 0.5)

    ball = GameItem(Rect(1, 1), white)
    world.add(ball, 0, 0)

    bat = GameItem(Rect(5, 1), white)
    world.add(bat, 0, -7)

