import pygame
from pygame.locals import *


pygame.init()  
win = pygame.display.set_mode((800, 600)) # Game window 800x600
pygame.display.set_caption("Button Running")

run = True

win.fill("white")
pygame.display.update() # updates to show background color

mouse_pos = pygame.mouse.get_pos()

while run:







    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False
            pygame.quit()
