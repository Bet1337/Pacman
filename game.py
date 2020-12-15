import pygame 
from pygame.locals import * 
import time
import random 
from constants import *
from Objetos.pacman import *
from Objetos.table import *
from Objetos.ghost import *

add_list()
append_ghost()


def game(pos):

    draw_walls()
    draw_fruit()
    draw_pac()
    draw_ghost()
    move_pac(pos)
    move_ghost()