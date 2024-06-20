from dataclasses import dataclass

from stutter.data import load_config


@dataclass()
class _CONFIG:
    screen_size: tuple[float, float]
    screen_name: str
    fixed_rate: int
    iterations: int
    warm_start: bool


CONFIG = _CONFIG(**load_config('game_config'))
