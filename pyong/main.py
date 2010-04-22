
import startup
startup

import pyglet

import traceback

from gameloop import Gameloop

def main():
    try:
        gameloop = Gameloop()
        gameloop.prepare()
        pyglet.app.run()
    except Exception, e:
        traceback.print_exc()
    finally:
        gameloop.stop()

if __name__ == '__main__':
    main()

