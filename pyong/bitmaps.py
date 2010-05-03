
from pyglet import resource

class Bitmaps(object):

    def load(self):
        resource.path = ['data']
        resource.reindex()
        numbers = resource.image('numbers.png')

        self.numbers = {}
        width = numbers.width / 10
        for n in xrange(0, 10):
            self.numbers[n] = \
                numbers.get_region(n * width, 0, width, numbers.height)

