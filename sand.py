#modules and files
import pygame, random
from pygame.locals import *

#init
pygame.init()
display = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
framespassed = 0

#variables
Map = []
colors = [(255,255,100), (255,255,50), (255, 92, 28)]
    
#methods


#game loop
while True:
    
    #filing
    display.fill((0,0,0))
    
    #input
    mclick = pygame.mouse.get_pressed()[0]
    mx, my = pygame.mouse.get_pos()
    
    
    #event loop
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    
    
    #tile drawing
    if mclick and not [mx // 8, my // 8] in Map:
        Map.append([mx // 8, my // 8])
        
    
    #tile loading
    for tile in Map:
        pygame.draw.rect(display, (255, 255, 100), (tile[0] * 8, tile[1] * 8, 8, 8))
        if not [tile[0], tile[1] + 1] in Map and not tile[1] == 69:
            tile[1] += 1
        elif not [tile[0] + 1, tile[1] + 1] in Map and not tile[1] == 69 and not tile[0] == 76 and not tile[0] == 2:
            tile[1] += 1
            tile[0] += 1
        elif not [tile[0] - 1, tile[1] + 1] in Map and not tile[1] == 69 and not tile[0] == 76 and not tile[0] == 2:
            tile[1] += 1
            tile[0] -= 1
    
    
    #update
    pygame.display.update()
    clock.tick(60)
