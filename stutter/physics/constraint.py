from pyglet.math import Vec2

from stutter.physics.body import RigidBody


class Constraint:

    def __init__(self):
        self.impulse: Vec2 = Vec2(0.0, 0.0)

    def compute_impulse(self):
        raise NotImplementedError()

    def apply_impulse(self):
        raise NotImplementedError()

    def solve(self):
        raise NotImplementedError()


class PointCollisionConstraint(Constraint):

    def __init__(self, a: RigidBody, b: RigidBody, p: Vec2, n: Vec2):
        super().__init__()


class EdgeCollisionConstraint(Constraint):
    # TODO

    def __init__(self, a: RigidBody, b: RigidBody):
        super().__init__()
