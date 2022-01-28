import sys

import pygame

def check_events() :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,snake) :
    screen.fill(ai_settings.bg_color)
    snake.blitme()
    pygame.display.flip()