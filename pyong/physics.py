
from pymunk import init_pymunk, Space

class Physics(object):

    def __init__(self):
        self.space = None

    def init(self):
        init_pymunk()
        self.space = Space()
        self.space.resize_static_hash()
        self.space.resize_active_hash()

    def add(self, body, shape, x, y):
        body.position = x, y
        self.space.add(body)
        self.space.add(shape)

    def update(self):
        self.space.step(1)

