from gameitem import GameItem
from physics import Physics
from shapes import Rect

class World(object):

    _next_id = 0

    def __init__(self):
        self.items = {}
        self.physics = Physics()

    def init(self):
        self.physics.init()

    def add(self, item, x, y):
        item.itemid = World._next_id

        self.physics.add(item.body, item.shape, x, y)
        
        self.items[World._next_id] = item
        World._next_id += 1

    def update(self):
        self.physics.update()


def populate(world):

    white = (1, 1, 1, 0.5)

    ball = GameItem(Rect(1, 1), white)
    world.add(ball, 0, 9.5)
    ball.body.apply_impulse((0, -0.15), (0, 0))

    world.bat = GameItem(Rect(5, 1), white)
    world.add(world.bat, 0, -8.5)

