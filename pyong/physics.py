
from pymunk import (
    Body, DampedRotarySpring, inf, init_pymunk, moment_for_poly, Poly, Space,
)


class PhysicsWorld(object):

    def __init__(self):
        self.space = None

    def init(self):
        init_pymunk()
        self.space = Space()
        self.space.gravity = (0, -0.002)
        self.space.resize_static_hash()
        self.space.resize_active_hash()


    def add(self, item, position, static):
        item.body.position = position
        if static:
            self.space.add_static(item.shape)
        else:
            self.space.add(item.body)
            self.space.add(item.shape)
            if item.rest_angle_spring:
                self.space.add(item.rest_angle_spring)


    def update(self, items):
        for item in items.itervalues():
            item.physics.update()

        self.space.step(1)


class PhysicsItem(object):

    def __init__(self, item):
        self.item = item
        self.body = self.create_body()
        self.shape = self.create_shape()
        self.rest_angle_spring = self.create_rest_angle_spring()

    def create_body(self):
        if self.item.static:
            mass = moment = inf
        else:
            mass = self.item.geometry.area
            moment = moment_for_poly(mass, self.item.geometry.verts)
        body = Body(mass, moment)
        return body

    def create_shape(self):
        shape = Poly(self.body, self.item.geometry.verts, (0, 0))
        shape.elasticity = 1.0
        shape.friction = 0.0
        return shape

    def create_rest_angle_spring(self):
        if self.item.rest_angle is not None:
            return DampedRotarySpring(
                self.body, Body(inf, inf), self.item.rest_angle, 2, 0.2)

    def apply_impulse(self, i):
        self.body.apply_impulse(i, (0, 0))

    def set_rest_angle(self, a):
        self.rest_angle_spring.rest_angle = a

    def update(self):
        self.body.reset_forces()

        if self.item.rest_y is not None:
            self.body.apply_impulse(
                (0, (self.item.rest_y - self.body.position[1]) * 0.1), (0, 0))

        if self.item.friction > 0:
            self.body.apply_impulse(
                -self.body.velocity * self.item.friction, (0, 0))

