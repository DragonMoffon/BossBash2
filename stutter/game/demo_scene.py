from random import Random

from arcade import draw_circle_filled, draw_line, Camera2D
from pyglet.math import Vec2

from stutter.engine.view import View

from stutter.physics.simulation import Simulation
from stutter.physics.collider import Polygon, compute_square
from stutter.physics.body import RigidBody, RigidBodyState, capture_rigidbody


class DemoView(View):

    def __init__(self):
        super().__init__()
        self._scene_camera: Camera2D = Camera2D(position=Vec2(0.0, 0.0))

        self._simulation: Simulation = Simulation()
        self._hinge: object = None
        self._body: RigidBody = RigidBody(
            Vec2(0.0, -100.0),
            0.0,

        )
        self._simulation.bodies.append(self._body)

        self._last_frame: RigidBodyState = None
        self._next_frame: RigidBodyState = None
        self._last_frame = self._next_frame = capture_rigidbody(self._body)

    def on_fixed_update(self, delta_time: float):
        self._simulation.step(delta_time)
        self._last_frame = self._next_frame
        self._next_frame = capture_rigidbody(self._body)

    def on_draw(self):
        with self._scene_camera.activate():
            pass

