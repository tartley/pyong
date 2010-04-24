
import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from camera import Camera
from controls import Controls
from render import Render
from world import World, populate

class Gameloop(object):

    def __init__(self):
        self.window = None

    def prepare(self):
        self.world = World()
        self.world.init()
        populate(self.world)
        self.camera = Camera(zoom=10.0)
        self.render = Render()
        self.controls = Controls(self.world.bat)
        self.window = Window(fullscreen=True, visible=False)
        self.window.set_exclusive_mouse(True)
        self.window.on_draw = self.draw
        self.window.on_resize = self.render.resize
        self.window.on_mouse_motion = self.controls.mouse_move
        self.render.init()
        pyglet.clock.schedule(self.update)
        self.window.set_visible()

    def update(self, dt):
        # scale dt such that the 'standard' framerate of 60fps gives dt=1.0
        dt *= 60.0
        # don't attempt to compensate for framerate of less than 30fps. This
        # guards against huge explosion when game is paused for any reason
        # and then restarted
        dt = min(dt, 2)
        self.world.update()
        self.window.invalid = True

    def draw(self):
        self.window.clear()
        self.camera.world_projection(self.window.width, self.window.height)
        self.camera.look_at()
        self.render.draw(self.world)
        self.window.flip()
        return EVENT_HANDLED

    def stop(self):
        if self.window:
            self.window.close()

