from random import Random

from arcade import draw_circle_filled, draw_line, Camera2D
from pyglet.math import Vec2
from stutter.engine.view import View


class DemoView(View):

    def __init__(self):
        super().__init__()
        self._scene_camera: Camera2D = Camera2D(position=Vec2(0.0, 0.0))

    def on_draw(self):
        with self._scene_camera.activate():
            pass

