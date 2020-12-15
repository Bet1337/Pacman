import pygame
from constants import *

pacman = pygame.Rect(SQUARE_SIZE*8+SQUARE_SIZE//4, SQUARE_SIZE*7+SQUARE_SIZE//4, 13, 13)
life = 3
def draw_pac():
    pygame.draw.rect(screen, YELLOW, pacman)

def pacman_collision():
    for i in WALLS:
        if pacman.collidelist(WALLS) >=0:
            return True

def collide_fruit():
    for j in FRUITS:
            if pacman.colliderect(j):
                FRUITS.remove(j)

def collide_ghost():

    for i in GHOST: 
        if pacman.colliderect(i):
            return True
def die_pac():
    global life 
    life -= 1
    if life == 0:
        pygame.quit()

def move_pac(key):

        dic = {275:"Right", 273:"Top", 276:"Left", 274:"Down", 0:"STOP"}

        last_pos = (pacman.x,pacman.y)

        collide_fruit()

        
        
        if dic[key] == "Right":
            pacman.x+=1
        elif dic[key] == "Left":
            pacman.x-=1
        elif dic[key] == "Down":
            pacman.y+= 1  
        elif dic[key] == "Top":
            pacman.y-=1
        else: 
            pass

        collide =  pacman_collision()
        ghost_col = collide_ghost()

        if collide:
            pacman.x,pacman.y = last_pos
        
        if ghost_col:
            pacman.x, pacman.y = SQUARE_SIZE*8+SQUARE_SIZE//4, SQUARE_SIZE*7+SQUARE_SIZE//4
            die_pac()

        
             
            
    
