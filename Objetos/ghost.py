import pygame
import random 
from constants import *
 
red = pygame.Rect(SQUARE_SIZE*8+SQUARE_SIZE//4, SQUARE_SIZE*3+SQUARE_SIZE//4, 13, 13)
pink = pygame.Rect(SQUARE_SIZE*8+SQUARE_SIZE//4, SQUARE_SIZE*3+SQUARE_SIZE//4, 13, 13)
purple = pygame.Rect(SQUARE_SIZE*8+SQUARE_SIZE//4, SQUARE_SIZE*3+SQUARE_SIZE//4, 13, 13)

def append_ghost():

    GHOST.append(red)
    GHOST.append(pink)
    GHOST.append(purple)

def draw_ghost(): 
    pygame.draw.rect(screen, RED, red)
    pygame.draw.rect(screen, PINK, pink)
    pygame.draw.rect(screen, PURPLE, purple)

def collision_ghost():
    for i in WALLS:
        if red.collidelist(WALLS) >=0:
            return "Red"
        elif purple.collidelist(WALLS) >=0:
            return "Purple"
        elif pink.collidelist(WALLS) >=0:
            return "Pink"

def move_ghost(): 
    
    position =["Right","Left", "Top", "Down"]
    ghosts = [red, purple,pink]
    
    for i in ghosts:
        
        get_pos_red = (red.x, red.y)
        get_pos_pink = (pink.x, pink.y)
        get_pos_purple = (purple.x, pink.y)

        randomic = random.choice(position)

        if randomic == "Right": 
            i.x+=1
        elif randomic == "Left":
            i.x-=1
        elif randomic == "Down":
            i.y+= 1
        elif randomic == "Top":
            i.y-=1
        else: 
            pass

        collide = collision_ghost()

        if collide == "Red":
            red.x, red.y = get_pos_red
        elif collide == "Pink":
            pink.x, pink.y = get_pos_pink
        elif collide == "Purple":
            purple.x, purple.y = get_pos_purple
