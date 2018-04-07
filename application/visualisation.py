from collections import defaultdict

import pyglet
from  pyglet.gl import *

from pyglet.window import key

from application.simulation import Bike

window = pyglet.window.Window()
player_image = pyglet.resource.image("player1.gif")
player_ship = pyglet.sprite.Sprite(img=player_image, x=400, y=300)


class Env:
    def __init__(self):
        self.keys = defaultdict(lambda: False)
        self._velocity = 100

    @property
    def velocity(self):
        return self._velocity


env = Env()
bike = Bike((40, 0), (0, 0))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        env.keys['up'] = True
    elif symbol == key.LEFT:
        env.keys['left'] = True
    elif symbol == key.RIGHT:
        env.keys['right'] = True
    elif symbol == key.DOWN:
        env.keys['down'] = True
    elif symbol == key.SPACE:
        env._velocity += 100


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        env.keys['up'] = False
    elif symbol == key.LEFT:
        env.keys['left'] = False
    elif symbol == key.RIGHT:
        env.keys['right'] = False
    elif symbol == key.DOWN:
        env.keys['down'] = False
    elif symbol == key.SPACE:
        env._velocity -= 100


def update(dt):
    if env.keys['up']:
        bike.velocity += env.velocity * dt
    if env.keys['down']:
        bike.velocity -= env.velocity * dt
    if env.keys['left']:
        bike.steering_angle -= env.velocity * dt * 0.01
    if env.keys['right']:
        bike.steering_angle += env.velocity * dt * 0.01
    bike.move(dt)

@window.event
def on_draw():
    window.clear()
    # pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    #                      ('v2f', bike.front + bike.back))
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(*bike.front)
    glVertex2f(*bike.back)
    glEnd()
    glBegin(GL_LINES)
    front_wheel = bike.front_wheel()
    glVertex2f(*front_wheel[0])
    glVertex2f(*front_wheel[1])
    glEnd()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()
