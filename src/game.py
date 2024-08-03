import pygame
import sys
from .snake import Snake
from .food import Food

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.width, self.height)
        self.food = Food(self.width, self.height)
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
        return True

    def update(self):
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            self.score += 1
        if self.snake.check_collision():
            return False
        return True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        while True:
            if not self.handle_events():
                break
            if not self.update():
                break
            self.draw()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()