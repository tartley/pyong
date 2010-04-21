
import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from camera import Camera
from render import Render

class Gameloop(object):

    def __init__(self):
        self.window = None

    def start(self, world):
        self.window = Window(fullscreen=True, visible=False)
        self.render = Render()
        self.camera = Camera()
        self.window.on_draw = lambda: self.draw(world)
        pyglet.clock.schedule(self.update)
        self.window.set_visible()
        pyglet.app.run()

    def update(self, dt):
        # scale dt such that 'standard' framerate of 60fps gives dt=1.0
        dt *= 60.0
        # don't attempt to compensate for framerate of less than 30fps. This
        # guards against huge explosion when game is paused for any reason
        # and then restarted
        dt = min(dt, 2)
        self.window.invalid = True

    def draw(self, world):
        self.window.clear()
        self.camera.world_projection(self.window.width, self.window.height)
        self.camera.look_at()
        self.render.draw(world)
        self.window.flip()
        return EVENT_HANDLED

    def stop(self):
        if self.window:
            self.window.close()

