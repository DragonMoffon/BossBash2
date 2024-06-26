from arcade import Window as _Window

from stutter.config import CONFIG


class Window(_Window):

    def __init__(self):
        super().__init__(*CONFIG.screen_size, CONFIG.screen_name)
        self.register_event_type('on_fixed_update')
        self.center_window()

    def _dispatch_updates(self, delta_time: float):
        # Tick main clock

        # Accumulate time for fixed update
        # If enough time accumulated do more physics steps
        self.dispatch_event('on_fixed_update', 1 / CONFIG.fixed_rate)
        # Calculate remainder time to lerp between simulation steps

        self.dispatch_event('on_update', delta_time)

        # Dispatch Notifications (if have time)
