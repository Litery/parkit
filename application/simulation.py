from math import sqrt, pow, fabs, sin, tan, copysign, cos, pi


class Bike:
    steering_dead_zone = 0.05

    def __init__(self, front=(1, 0), back=(0, 0)):
        self.front = front
        self.back = back
        self.length = sqrt(pow(front[0] - back[0], 2) + pow(front[1] - back[1], 2))
        self._steering_angle = 0
        self.velocity = 0

    @property
    def steering_angle(self):
        return self._steering_angle

    @steering_angle.setter
    def steering_angle(self, value):
        self._steering_angle = (fabs(value) % pi) * copysign(1, value)

    @property
    def driving_vector(self):
        x = (self.front[0] - self.back[0]) / self.length
        y = (self.front[1] - self.back[1]) / self.length
        return x, y

    def front_wheel(self):
        x, y = self.driving_vector
        cos_sa = cos(-self.steering_angle)
        sin_sa = sin(-self.steering_angle)
        wheel_vector = x * cos_sa - y * sin_sa, \
                       x * sin_sa + y * cos_sa

        front = self.front[0] + wheel_vector[0] * self.length / 3, \
                self.front[1] + wheel_vector[1] * self.length / 3

        back = self.front[0] - wheel_vector[0] * self.length / 3, \
                self.front[1] - wheel_vector[1] * self.length / 3

        return front, back

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
            distance = self.velocity * time_delta
            x, y = self.driving_vector
            dx = x * distance
            dy = y * distance
            self.front = self.front[0] + dx, self.front[1] + dy
            self.back = self.back[0] + dx, self.back[1] + dy

        return self.front, self.back
