from unittest import TestCase

from application.simulation import Bike


class TestBike(TestCase):
    def setUp(self):
        self.bike = Bike()

    def assertAlmostEqual(self, first, second, **kwargs):
        if hasattr(first, '__iter__'):
            for f, s in zip(first, second):
                self.assertAlmostEqual(f, s)
        else:
            super().assertAlmostEqual(first, second, **kwargs)

    def test_bike_1(self):
        self.bike.front = 0, 1
        self.bike.back = 0, 0
        self.bike.length = 1
        self.bike.velocity = 2
        self.bike.steering_angle = 0.12

        front, back = self.bike.move(1)
        self.assertAlmostEqual(front, (0.473712786596821, 2.938175599198570))
        self.assertAlmostEqual(back, (0.236569287492403, 1.966700967088950))

        front, back = self.bike.move(1)
        self.assertAlmostEqual(front, (1.393538485154340, 4.708726118609750))
        self.assertAlmostEqual(back, (0.932780698055037, 3.821200196944730))

        self.bike.steering_angle = 0.09
        self.bike.velocity = 1
        front, back = self.bike.move(1)
        self.assertAlmostEqual(front, (1.969312893894910, 5.525923054491420))
        self.assertAlmostEqual(back, (1.430752703261540, 4.683336013845200))

        self.bike.steering_angle = -0.1
        self.bike.velocity = 1
        front, back = self.bike.move(1)
        self.assertAlmostEqual(front, (2.375818232306970, 6.439116969532610))
        self.assertAlmostEqual(back, (1.923918332407090, 5.54704831720226))
