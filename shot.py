from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt