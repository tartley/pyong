from __future__ import division

class Rect(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def verts(self):
        return [
            (-self.width/2, -self.height/2),
            (+self.width/2, -self.height/2),
            (+self.width/2, +self.height/2),
            (-self.width/2, +self.height/2),
        ]
        
    @property
    def indices(self):
        return [(0, 2, 1), (2, 0, 3)]

    @property
    def area(self):
        return self.width * self.height

