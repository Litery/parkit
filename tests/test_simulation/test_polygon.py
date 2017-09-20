from functools import partial

from unittest import TestCase

from simulation.simulation import Polygon

def construct_polygon(poly):
    x, y = zip(*poly)
    return Polygon(x, y)

class TestPolygon(TestCase):
    def test_not_collides_1(self):
        points1 = [(1.0, 2.0), (1.0, 1.0), (0.0, 1.0), (1.0, 2.0)]
        points2 = [(-1.0, -1.0),
                (-1.0, 1.0),
                (0.0, 0.5),
                (1.0, 1.0),
                (1.0, -1.0),
                (0.0, -0.5),
                (-1.0, -1.0)]
        poly1 = construct_polygon(points1)
        poly2 = construct_polygon(points2)
        assert not poly1.collides(poly2)

    def test_collides_1(self):
        points1 = [(0.0, 1.0), (0.0, 0.0), (-1.0, 0.0), (0.0, 1.0)]
        points2 = [(-1.0, -1.0),
                (-1.0, 1.0),
                (0.0, 0.5),
                (1.0, 1.0),
                (1.0, -1.0),
                (0.0, -0.5),
                (-1.0, -1.0)]
        poly1 = construct_polygon(points1)
        poly2 = construct_polygon(points2)
        assert poly1.collides(poly2)