import importlib.resources as pkg_resources

import arcade
import json

import stutter.data.images as imgs
import stutter.data.fonts as fonts
import stutter.data.audio as audio
import stutter.data.shaders as shaders
import stutter.data.config as config


def load_texture(name, *, fmt: str = "png", **kwargs):
    with pkg_resources.path(imgs, f"{name}.{fmt}") as texture_path:
        return arcade.load_texture(texture_path, **kwargs)


def load_config(name):
    with pkg_resources.open_text(config, f'{name}.json') as config_file:
        return json.load(config_file)


def load_font(name: str) -> None:
    font_name = name + ".ttf"
    with pkg_resources.path(fonts, font_name) as path:

        arcade.text.load_font(path)


def load_audio(name: str, *, streaming: bool = False) -> arcade.Sound:
    audio_name = f"{name}.wav"
    with pkg_resources.path(audio, audio_name) as audio_path:
        return arcade.load_sound(audio_path, streaming=streaming)


def load_shader(name: str):
    shader_name = f"{name}.glsl"
    return pkg_resources.read_text(shaders, shader_name)