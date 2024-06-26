from typing import NamedTuple

from pyglet.math import Vec2


class RigidBodyState(NamedTuple):
    position: Vec2
    direction: float
    velocity: Vec2
    rotation: float


class RigidBody[T]:

    def __init__(self,
                 position: Vec2,
                 direction: float,
                 velocity: Vec2,
                 rotation: float,
                 mass: float,
                 inertia: float,
                 mesh: T
                 ):
        self.position: Vec2 = position
        self.direction: float = direction
        self.velocity: Vec2 = velocity
        self.rotation: float = rotation

        self.mass: float = mass
        self.inv_mass: float = float('inf') if not mass else 1.0 / mass
        self.inertia: float = inertia
        self.inv_inertia: float = float('inf') if not inertia else 1.0 / inertia

        self.mesh: T = mesh

    def apply_impulse(self, impulse: Vec2, origin: Vec2):
        """
        Assumes instantaneous acceleration so pre-apply delta-time
        """
        torque = impulse.cross(origin - self.position)

        self.velocity += impulse * self.inv_mass
        self.rotation += torque * self.inv_inertia

    def apply_acceleration(self, linear: Vec2 = Vec2(0.0, 0.0), angular: float = 0.0):
        """
        Assumes instantaneous acceleration so pre-apply delta-time
        """
        self.velocity += linear
        self.rotation += angular


def capture_rigidbody(rigidbody: RigidBody) -> RigidBodyState:
    return RigidBodyState(
        rigidbody.position,
        rigidbody.direction,
        rigidbody.velocity,
        rigidbody.rotation
    )
