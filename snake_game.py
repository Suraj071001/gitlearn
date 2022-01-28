import pygame
from pygame.sprite import Group

from settings import Settings
from snake import Snake
import game_functions as gf

def run_game() :
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("snake_game")

    #instance of snake
    snake = Snake(screen)
    snakes = Group()

    while True :
        gf.check_events()
        gf.update_screen(ai_settings,screen,snake)
run_game()