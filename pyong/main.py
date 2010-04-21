
import startup
startup

import traceback

from gameloop import Gameloop
from world import World, populate

def main():
    world = World()
    populate(world)
    try:
        gameloop = Gameloop()
        gameloop.start(world)
    except Exception, e:
        traceback.print_exc()
    finally:
        gameloop.stop()

if __name__ == '__main__':
    main()

