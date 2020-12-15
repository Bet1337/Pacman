import pygame
from constants import *

def add_list(): 
    for row in range(ROW):
        for col in range(COL):
            if tiles[row][col] == 0: 
                WALLS.append(pygame.Rect(SQUARE_SIZE*col, SQUARE_SIZE*row,SQUARE_SIZE,SQUARE_SIZE))
            else:
                FRUITS.append(pygame.Rect(SQUARE_SIZE*col+SQUARE_SIZE//4,SQUARE_SIZE*row+SQUARE_SIZE//4,5,5))
            
def draw_walls(): 
    for i in WALLS:
        pygame.draw.rect(screen, BLUE, i)

def draw_fruit():
    
    for i in FRUITS:
        pygame.draw.rect(screen, WHITE, i)

