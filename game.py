# coding=utf-8

import pygame
import time
import random
from pygame.locals import *

pygame.init()
pygame.font.init()

crashed = False
paused = False

# Display
display_width = 640
display_height = 480
line_width = 10

# Snake
snake_width = 25
snake_x = 50
snake_y = 50
direction = 'RIGHT'
delay_on_tick = 0.05
snake = [[snake_x, snake_y]]

# Poop
poop_size = 10
poop_x = 0 
poop_y = 0
poops_collected = 0
poop_on_field = False

# Colors
black = (0,0,0)
border_color = (60,60,60)
snake_color = (86, 153, 216)
snake_border_color = (23, 138, 183)
poop_color = (160, 78, 27)

# Fill display area
screen = pygame.display.set_mode((display_width, display_height))
screen.fill((255,180,120))

# Draw borders
pygame.draw.rect(screen, border_color, [0,0,display_width,line_width])
pygame.draw.rect(screen, border_color, [0,0,line_width, display_height])
pygame.draw.rect(screen, border_color, [0,display_height-line_width,display_width,line_width])
pygame.draw.rect(screen, border_color, [display_width-line_width,0,line_width, display_height+line_width])

# Draw snake
pygame.draw.rect(screen, snake_color, [50, 50, snake_width, snake_width])

pygame.display.flip()

# Fonts
display_font = pygame.font.SysFont('Arial', 20)
pause_font = pygame.font.SysFont('Arial', 50)

while not crashed:
    print(delay_on_tick)
    time.sleep(delay_on_tick)
    textsurface = display_font.render('Napatut kakat: {}'.format(poops_collected), False, (0, 0, 0))
    pause_text = pause_font.render('Peli paussilla, paina P', False, (0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        ###############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_p:
                paused = True
                screen.blit(pause_text,(20, 40))
                pygame.display.flip()
                time.sleep(1)
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                paused = False
        ###############################

    if direction == 'LEFT':
        snake_x -= 5
    if direction == 'RIGHT':
        snake_x += 5
    if direction == 'UP':
        snake_y -= 5
    if direction == 'DOWN':
        snake_y += 5

    if (((poop_x + poop_size) > snake_x) and (poop_x < snake_x + snake_width) and ((poop_y + poop_size) > snake_y) and (poop_y < (snake_y + snake_width))):
        poops_collected += 1
        poop_on_field = False

    if not poop_on_field:
        if delay_on_tick > 0.02:
            delay_on_tick *= 0.95
        poop_x = random.randint(20, display_width - 20)
        poop_y = random.randint(20, display_height - 20)
        poop_on_field = True

    screen.fill((255,180,120))
    screen.blit(textsurface,(10,10))
    pygame.draw.rect(screen, poop_color, [poop_x, poop_y, poop_size, poop_size])
    pygame.draw.rect(screen, border_color, [0,0,display_width,line_width])
    pygame.draw.rect(screen, border_color, [0,0,line_width, display_height])
    pygame.draw.rect(screen, border_color, [0,display_height-line_width,display_width,line_width])
    pygame.draw.rect(screen, border_color, [display_width-line_width,0,line_width, display_height+line_width])
    pygame.draw.rect(screen, snake_color, [snake_x, snake_y, snake_width, snake_width])
    pygame.display.flip()
    
pygame.quit()
exit(0)

# pygame.draw.rect(screen, snake_color, [75, 50, snake_width, snake_width])

# pygame.draw.rect(screen, snake_border, [75, 50, 5, snake_width])
# pygame.draw.rect(screen, snake_border, [100, 50, 5, snake_width])

# pygame.draw.rect(screen, (255,255,255), [55, 55, 5, 10])
# pygame.draw.rect(screen, (0,0,0), [55, 60, 5, 5])