
from pymunk import Body, inf, init_pymunk, moment_for_poly, Poly, Space


class Physics(object):

    def __init__(self):
        self.space = None

    def init(self):
        init_pymunk()
        self.space = Space()
        self.space.resize_static_hash()
        self.space.resize_active_hash()

    def create_body(self, item):
        if item.static:
            mass = inf
            moment = inf
        else:
            mass = item.outline.area
            moment = moment_for_poly(mass, item.outline.verts)
        return Body(mass, moment)

    def create_shape(self, item):
        shape = Poly(item.body, item.outline.verts, (0, 0))
        shape.elasticity = 1.0
        shape.friction = 0.0
        return shape

    def add(self, item, x, y):
        item.body = self.create_body(item)
        item.body.position = x, y
        item.shape = self.create_shape(item)
        if item.static:
            self.space.add_static(item.shape)
        else:
            self.space.add(item.body)
            self.space.add(item.shape)

    def update(self):
        self.space.step(1)


