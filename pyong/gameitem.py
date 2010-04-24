
class GameItem(object):

    static = False
    friction = 0.0

    def __init__(self, outline, color):
        self.outline = outline
        self.color = color
        self.itemid = None
        self.body = None
        self.shape = None
        self.glyph = None

    @property
    def x(self):
        return self.body.position.x

    @property
    def y(self):
        return self.body.position.y

    @property
    def angle(self):
        return self.body.angle

    def update(self):
        self.body.reset_forces()
        if self.friction > 0:
            self.body.apply_impulse(
                -self.body.velocity * self.friction, (0, 0))
        self.body.torque = -self.body.angle / 400
            # + self.body.angular_velocity * 2


class Bat(GameItem):
    friction = 1.0

class Ball(GameItem):
    pass

class Wall(GameItem):
    static = True

