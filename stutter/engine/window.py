from arcade import Window as _Window

from stutter.config import CONFIG


class Window(_Window):

    def __init__(self):
        super().__init__(*CONFIG.screen_size, CONFIG.screen_name)
        self.center_window()

    def _dispatch_updates(self, delta_time: float):
        # Tick main clock
        self.dispatch_event('on_update', delta_time)

        # Accumulate time for fixed update
        # If enough time accumulated do more physics steps

        # Dispatch Notifications (if have time)
