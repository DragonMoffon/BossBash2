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

        self.mesh: T = mesh

    def capture(self) -> RigidBodyState:
        return RigidBodyState(
            self.position,
            self.direction,
            self.velocity,
            self.rotation
        )
