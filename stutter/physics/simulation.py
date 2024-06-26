from pyglet.math import Vec2

from stutter.physics.body import RigidBody, RigidBodyState
from stutter.physics.constraint import Constraint

from stutter.config import CONFIG

GRAVITY = Vec2(0.0, -98.1)


class Simulation:

    def __init__(self):
        self.bodies: list[RigidBody] = []
        # Every fixed simulation step is saved, so we can change the flow of observed time, including backwards, without issue.
        self.steps: list[tuple[RigidBodyState, ...]] = []
        # Joints, and other connections can be modeled as constraints, so they can need to be solved every frame
        self.continuous_constraints: list[Constraint] = []
        # To allow collisions to behave better overtime we assume a collision will keep happening between frames,
        # so we reuse the last frame's solution as the input to the next solution.
        self.context_constraints: dict[str, Constraint] = {}

    def step(self, dt: float):
        """
        Apply forces (calculate acceleration for frame and change the velocity by that amount)
        detect collisions, and construct the constraints for the frame
        do x iterations of solving each constraint through velocity and position impulses
        do integration (update position)
        capture state
        """
        for body in self.bodies:
            # Normally we would apply a force but because gravity is dependent on mass it cancels with the
            # acceleration making it cheaper to apply it as an impulse. This will change in the future
            # we apply it at the body's center so there is no radial component
            body.apply_acceleration(GRAVITY * dt)

        if not CONFIG.warm_start:
            for constraint in self.continuous_constraints:
                constraint.impulse = 0.0

        for iteration in range(CONFIG.iterations):
            self.iteration()

    def iteration(self):
        """
        for every constraint (collisions and joints) do a sub step to solve each constraint
        """
        for constraint in self.continuous_constraints:
            constraint.solve()
