import pygame
import random

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (self.width - 20) // 20) * 20,
            random.randint(0, (self.height - 20) // 20) * 20
        )
        return self.position

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], 20, 20))