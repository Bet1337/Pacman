import pygame 
from pygame.locals import * 
from constants import *
from game import *

pygame.init()
pygame.display.set_caption('PACMAN')

add_list()

def main():
    in_game = True
    pos = 0 
    clock = pygame.time.Clock()

    while in_game:

        for event in pygame.event.get():
            if event.type == QUIT:
                in_game = False
            if event.type == pygame.KEYDOWN:
                pos = event.key
        print()
        screen.fill(BLACK)
        game(pos)

        if FRUITS == []:
            in_game = False
        clock.tick(30)
    
        pygame.display.update()

    pygame.quit()

main()
