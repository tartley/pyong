from __future__ import division

class Controls(object):

    def __init__(self, bat):
        self.bat = bat

    def mouse_move(self, x, y, dx, dy):
        self.bat.body.apply_impulse((dx / 50, 0), (0, 0))

