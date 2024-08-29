import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
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
        angle = random.uniform(20, 50)
        new_ast_vel_1 = self.velocity.rotate(angle)
        new_ast_vel_2 = self.velocity.rotate(-angle)
        self.radius -= ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, self.radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, self.radius)
        new_ast_1.velocity = new_ast_vel_1 * 1.2
        new_ast_2.velocity = new_ast_vel_2 * 1.2
        
        