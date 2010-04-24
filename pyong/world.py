from gameitem import Bat, Ball, Wall
from glyph import Glyph
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

        self.physics.add(item, x, y)
        item.glyph = Glyph.from_item(item)
        
        self.items[World._next_id] = item
        World._next_id += 1

    def update(self):
        self.physics.update()
        for item in self.items.itervalues():
            item.update()


def populate(world):

    white = (1, 1, 1, 1)
    grey = (0.5, 0.5, 0.5, 1)

    wall = Wall(Rect(30, 1), grey)
    world.add(wall, 0, 9.5)

    wall = Wall(Rect(1, 25), grey)
    world.add(wall, -15, 0)

    wall = Wall(Rect(1, 25), grey)
    world.add(wall, +15, 0)

    ball = Ball(Rect(1, 1), white)
    world.add(ball, 0, 8.0)
    ball.body.apply_impulse((0, -0.15), (0, 0))

    world.bat = Bat(Rect(5, 1), white)
    world.add(world.bat, 0, -7.0)

