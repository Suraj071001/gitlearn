import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from snake import Snake

def run_game() :
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.height,ai_settings.width))
    pygame.display.set_caption("snake_game")

    #instance of snake
    snake = Snake(screen)

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
        screen.fill(ai_settings.bg_color)
        snake.blitme()
        pygame.display.flip()
run_game()