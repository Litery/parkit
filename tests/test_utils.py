from functools import partial

from unittest import TestCase

from framework.utils import double_array
from simulation.simulation import pnpoly


def prepare_function(poly):
    x, y = zip(*poly)
    return partial(pnpoly, len(poly), double_array(x), double_array(y))


class TestPointInPolygon(TestCase):

    def run_test(self, poly, args, expected):
        fun = prepare_function(poly)
        for _args, _expected in zip(args, expected):
            self.assertEqual(fun(*_args), _expected)

    def test_triangle_1(self):
        poly = [(1.0, 2.0), (1.0, 1.0), (0.0, 1.0), (1.0, 2.0)]
        args = [(0.88, 1.37), (0.99, 1.82), (2.0, 1.82)]
        expected = [1, 1, 0]
        self.run_test(poly, args, expected)

    def test_polygon_1(self):
        poly = [(-1.0, -1.0),
                (-1.0, 1.0),
                (0.0, 0.5),
                (1.0, 1.0),
                (1.0, -1.0),
                (0.0, -0.5),
                (-1.0, -1.0)]
        args = [(-0.81, 0.63), (-0.86, -0.78), (-1.04, 0.66), (0.97, 0.83)]
        expected = [1, 1, 0, 1]
        self.run_test(poly, args, expected)
