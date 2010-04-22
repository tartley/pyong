
from itertools import repeat

from pymunk import Body, Poly, moment_for_poly

from glyph import Glyph


class GameItem(object):

    def __init__(self, outline, color):
        self.outline = outline
        self.color = color
        self.itemid = None
        self._glyph = None
        self._body = None
        self._shape = None

    @property
    def x(self):
        if self._body:
            return self._body.position.x

    @property
    def y(self):
        if self._body:
            return self._body.position.y

    @property
    def angle(self):
        if self._body:
            return self._body.angle

    @property
    def glyph(self):
        if self._glyph is None:
            self._glyph = Glyph(
                self.outline.verts,
                repeat(self.color, len(self.outline.verts)),
                self.outline.indices)
        return self._glyph

    @property
    def body(self):
        if self._body is None:
            mass = self.outline.area
            self._body = Body(mass, moment_for_poly(mass, self.outline.verts))
        return self._body

    @property
    def shape(self):
        if self._shape is None:
            self._shape = Poly(self._body, self.outline.verts, (0, 0))
            self._shape.elasticity = 1.0
            self._shape.friction = 0.0
        return self._shape

