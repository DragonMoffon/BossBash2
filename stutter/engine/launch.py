from stutter.engine.window import Window


def launch(window: type[Window]):
    win = window()
    win.run()
