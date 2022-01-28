import pygame
from pygame.sprite import Sprite
class Snake(Sprite) :
    """create a small snake with circles"""
    def __init__(self,screen):
        super().__init__()
        #initialise the settings of snake
        self.screen = screen
        self.snake = pygame.image.load("snake_images/snake.bmp")
        self.snake_rect = self.snake.get_rect()
        self.screen_rect = screen.get_rect()

        #positioning the snake
        self.snake_rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.snake,self.snake_rect)


