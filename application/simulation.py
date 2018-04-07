from math import sqrt, pow, fabs, sin, tan, copysign, cos


class Bike:
    steering_dead_zone = 0.05

    def __init__(self, front=(1, 0), back=(0, 0)):
        self.front = front
        self.back = back
        self.length = sqrt(pow(front[0] - back[0], 2) + pow(front[1] - back[1], 2))
        self.steering_angle = 0
        self.velocity = 0

    @property
    def big_radius(self):
        return fabs(self.length / sin(self.steering_angle))

    @property
    def small_radius(self):
        return fabs(self.length / tan(self.steering_angle))

    @property
    def angular_velocity(self):
        return self.velocity / self.big_radius * copysign(1, self.steering_angle)

    @property
    def circle_center(self):
        x = (self.front[1] - self.back[1]) \
            * (self.small_radius / self.length) \
            * copysign(1, self.steering_angle) \
            + self.back[0]

        y = (self.back[0] - self.front[0]) \
            * (self.small_radius / self.length) \
            * copysign(1, self.steering_angle) \
            + self.back[1]

        return x, y

    def move(self, time_delta):
        if fabs(self.steering_angle) > self.steering_dead_zone:
            angular_distance = - self.angular_velocity * time_delta
            x, y = self.circle_center
            cos_ad = cos(angular_distance)
            sin_ad = sin(angular_distance)

            front_x = (self.front[0] - x) * cos_ad - (self.front[1] - y) * sin_ad + x
            front_y = (self.front[0] - x) * sin_ad + (self.front[1] - y) * cos_ad + y

            back_x = (self.back[0] - x) * cos_ad - (self.back[1] - y) * sin_ad + x
            back_y = (self.back[0] - x) * sin_ad + (self.back[1] - y) * cos_ad + y

            self.front = front_x, front_y
            self.back = back_x, back_y

        else:
            vector_x = (self.front[0] - self.back[0]) / self.length
            vector_y = (self.front[1] - self.back[1]) / self.length





        return self.front, self.back
