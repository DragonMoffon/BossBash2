from pyglet.math import Vec2

from stutter.physics.body import RigidBody
from stutter.physics.collider import Polygon


class Constraint:

    def __init__(self):
        self.impulse: float = 0.0

    def compute_impulse(self) -> float:
        raise NotImplementedError()

    def apply_impulse(self, impulse: float):
        raise NotImplementedError()

    def solve(self):
        raise NotImplementedError()


class PositionConstraint:
    """
    takes the form C(x) = 0 where x = (x, y)^T

    inequality constraints
    C(x, y) >= 0 i.e. if C <= 0 then enforce C' >= 0 otherwise skip
    """


class VelocityConstraint:
    """
    takes the form C' = 0 or C' = Jv where is J is the Jacobian, and v = (x', y')^T

    F = J^T * l
    l is the Lagrange Multiplier (lambda) is the signed magnitude we need to solve to use constraint.

    Each constraint has its own Jacobian we will use to solve for l

    some velocity constraints have time dependence 'bias' b
    position: C(x, t) = 0
    velocity: C' = Jv + b(t) = 0

    Recipe for J
    Use geometry to write C
    Diff C with respect to T i.e. dC/dt = C * d/dt
    isolate V ([x, y] * d/dt)
    identify J and b

    note 0 <= l <= inf
    """


class DistanceConstraint(VelocityConstraint):
    """
    position: C = ||a - b|| - L
    velocity: C' = (a - b) / ||a - b|| * v
    Jacobian: J = (a - b) / ||a - b|| = [(a.x - b.x) / ||a - b||, (a.y - b.y) / ||a - b||]
    bias: 0
    """