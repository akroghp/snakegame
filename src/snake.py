import pygame
import random

class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.body = [(width // 2, height // 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def get_head_position(self):
        return self.body[0]

    def change_direction(self, new_direction):
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        cur = self.get_head_position()
        x, y = cur
        if self.direction == 'UP':
            y -= 20
        elif self.direction == 'DOWN':
            y += 20
        elif self.direction == 'LEFT':
            x -= 20
        elif self.direction == 'RIGHT':
            x += 20
        self.body.insert(0, (x, y))
        if len(self.body) > 1:
            self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def check_collision(self):
        head = self.get_head_position()
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height
        )

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (segment[0], segment[1], 20, 20))