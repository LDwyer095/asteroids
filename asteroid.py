import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randAngle = random.uniform(20,50)

        astro1 = self.velocity.rotate(randAngle)
        astro2 = self.velocity.rotate(-randAngle)
        newRad = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, newRad)
        asteroid.velocity = astro1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, newRad)
        asteroid.velocity = astro2 * 1.2

