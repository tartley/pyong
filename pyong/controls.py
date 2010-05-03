from __future__ import division

from pyglet.window import key
from pyglet.window.mouse import LEFT, RIGHT


class Controls(key.KeyStateHandler):

    def __init__(self, bat):
        self.bat = bat
        self.current_buttons = 0

    def on_mouse_motion(self, x, y, dx, dy, buttons=None, modifiers=None):
        self.bat.apply_impulse((dx / 50, 0))

    def on_mouse_drag(self, x, y, dx, dy, buttons=None, modifiers=None):
        self.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self.current_buttons |= button

    def on_mouse_release(self, x, y, button, modifiers):
        self.current_buttons &= ~button

    def update(self):
        self.set_rest_angle()

    def set_rest_angle(self):
        if self.current_buttons == LEFT or self[key.Z]:
            angle = -0.5
        elif self.current_buttons == RIGHT or self[key.X]:
            angle = +0.5
        else:
            angle = 0
        self.bat.set_rest_angle(angle)

