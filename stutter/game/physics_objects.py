from stutter.physics.body import RigidBody
from stutter.physics.collider import Polygon, compute_square

from pyglet.math import Vec2


def create_square_body(pos, direction, width, height, mass) -> RigidBody[Polygon]:
    square = compute_square(width, height)
    return RigidBody(
        pos,
        direction,
        Vec2(),
        0,
        mass,
        1.0/12.0 * mass * (width**2 + height**2),
        square
    )
