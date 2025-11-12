import pygame
from logger import log_event
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
            return "This was a small asteroid and we're done."
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            one = Asteroid(self.position.x, self.position.y, new_radius)
            two = Asteroid(self.position.x, self.position.y, new_radius)
 
            one.velocity = self.velocity.rotate(angle) * 1.2
            two.velocity = self.velocity.rotate(-angle) * 1.2
