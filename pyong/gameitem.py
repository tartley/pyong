
from itertools import repeat

from glyph import Glyph

class GameItem(object):

    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self._glyph = None
        self.x = None
        self.y = None
        self.angle = 0

    @property
    def glyph(self):
        if self._glyph is None:
            self._glyph = Glyph(
                self.shape.verts,
                repeat(self.color, len(self.shape.verts)),
                self.shape.indices)
        return self._glyph

