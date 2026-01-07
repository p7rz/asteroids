import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        log_event("asteroid_split")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_vector1 = self.velocity.rotate(random_angle)
        random_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        smaller_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        smaller_asteroid_one.velocity = pygame.Vector2(random_vector1) * 1.2
        smaller_asteroid_two.velocity = pygame.Vector2(random_vector2) * 1.2
