from dataclasses import dataclass

from stutter.data import load_config


@dataclass()
class _CONFIG:
    screen_size: tuple[float, float]
    screen_name: str


CONFIG = _CONFIG(**load_config('game_config'))
