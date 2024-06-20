from stutter.engine.window import Window

from stutter.game.demo_scene import DemoView


class Stutter(Window):

    def __init__(self):
        super().__init__()
        self.demo = DemoView()
        self.show_view(self.demo)
