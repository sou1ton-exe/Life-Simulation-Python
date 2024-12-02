import random
import pygame as pg
from const import *

class Cells:
    def __init__(self, size, state, x, y):
        self.size = size
        self.state = state
        self.x = x
        self.y = y
    
    def Draw(self, window):
        rect = pg.Rect(self.x, self.y, self.size, self.size)
        if self.state == 1: pg.draw.rect(window, BLACK, rect)
        else: pg.draw.rect(window, WHITE, rect)
        
        