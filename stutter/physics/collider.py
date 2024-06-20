"""
For simplicity there are only Convex Polygon colliders

This reduces the code duplication, but does make even simple calculations more complex
Spherical and Cube colliders can come later

Polygons are assumed to be centered on their COM
"""
from typing import NamedTuple

from pyglet.math import Vec2


class Edge(NamedTuple):
    start: Vec2
    end: Vec2
    normal: Vec2


def compute_edge(start: Vec2, end: Vec2) -> Edge:
    diff = (end - start).normalize()
    normal = Vec2(-diff.y, diff.x)
    return Edge(start, end, normal)


class Polygon(NamedTuple):
    points: tuple[Vec2, ...]
    edges: tuple[Edge, ...]


def compute_square(width: float, height: float) -> Polygon:
    w2 = width/2.0
    h2 = height/2.0
    points = (Vec2(-w2, -h2), Vec2(-w2, h2), Vec2(w2, h2), Vec2(w2, -h2))
    edges = (
        compute_edge(points[0], points[1]),
        compute_edge(points[1], points[2]),
        compute_edge(points[2], points[3]),
        compute_edge(points[3], points[0])
    )
    return Polygon(points, edges)
