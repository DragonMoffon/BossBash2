class Simulation:

    def step(self):
        """
        Apply forces (calculate acceleration for frame)
        do semi-implicit euler integration (update position and velocity)
        detect collisions, and construct the constraints for the frame
        do x iterations of solving each constraint through velocity and position impulses
        """

    def iteration(self):
        """
        for every constraint (collisions and joints) do a sub step to solve each constraint
        """