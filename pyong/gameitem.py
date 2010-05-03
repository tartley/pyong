
class GameItem(object):

    static = False
    friction = 0.0
    rest_angle = None
    rest_y = None

    def __init__(self, geometry, color):
        self.geometry = geometry
        self.color = color
        self.itemid = None
        self.physics = None
        self.glyph = None

    @property
    def position(self):
        return self.physics.body.position

    @property
    def angle(self):
        return self.physics.body.angle

    def apply_impulse(self, impulse):
        self.physics.apply_impulse(impulse)

    def set_rest_angle(self, angle):
        self.physics.set_rest_angle(angle)

    def update(self):
        pass


class Bat(GameItem):
    friction = 1.0
    rest_angle = 0

    def update(self):
        if self.rest_y is None:
            self.rest_y = self.position[1]

class Ball(GameItem):
    pass

class Wall(GameItem):
    static = True

