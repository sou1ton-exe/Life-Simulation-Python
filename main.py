import pygame as pg
from cells import Cells
import random
from const import *

isPlay = True
isPaused = False

mainWindow = pg.display.set_mode(SIZE)
time = pg.time.Clock()

last_ticks = pg.time.get_ticks()

matrix_of_cells = \
 [[Cells(SIZE_OF_CELLS, 0, j*SIZE_OF_CELLS, i*SIZE_OF_CELLS) for j in range(CELL_CONST)] for i in range(CELL_CONST)]
 
offset = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

for i in range(CELL_CONST):
        for j in range(CELL_CONST):
            matrix_of_cells[i][j].state = random.randint(0,1)
            
            
def Neigb(i, j):
    global offset, CELL_CONST
    
    score = 0
    for g in range(len(offset)):
        if (i+offset[g][0] >= 0 and i+offset[g][0] < CELL_CONST) and (j+offset[g][1] >= 0 and j+offset[g][1] < CELL_CONST):
            if matrix_of_cells[i+offset[g][0]][j+offset[g][1]].state == 1: score += 1
        
    return score

def Logic():
    global matrix_of_cells, CELL_CONST
    
    result_matrix = \
    [[Cells(SIZE_OF_CELLS, 0, j*SIZE_OF_CELLS, i*SIZE_OF_CELLS) for j in range(CELL_CONST)] for i in range(CELL_CONST)]
    
    for i in range(CELL_CONST): 
        for j in range(CELL_CONST): 
            if matrix_of_cells[i][j].state == 0 and Neigb(i, j) == 3: result_matrix[i][j].state = 1
            
            elif matrix_of_cells[i][j].state == 1 and (Neigb(i, j) == 3 or Neigb(i, j) == 2): result_matrix[i][j].state = 1
            else: result_matrix[i][j].state = 0

    matrix_of_cells = result_matrix

while isPlay:
    mouse = pg.mouse.get_pressed()
    
    if pg.time.get_ticks() - last_ticks >= TICKS and mouse[0] == True:
        mouse_pos = pg.mouse.get_pos()
    
        x = mouse_pos[0] // SIZE_OF_CELLS
        y = mouse_pos[-1] // SIZE_OF_CELLS
        
        if matrix_of_cells[y][x].state == 0: matrix_of_cells[y][x].state = 1
        elif matrix_of_cells[y][x].state == 1: matrix_of_cells[y][x].state = 0
        
        last_ticks = pg.time.get_ticks()
    
    objectives = pg.event.get()
    
    for i in range(len(objectives)):
        if objectives[i].type == pg.KEYDOWN:
            if objectives[i].key == pg.K_SPACE: isPaused = not isPaused
        
        if objectives[i].type == pg.QUIT:
            isPlay = False
            break
    
    if isPaused == False: Logic()
    
    mainWindow.fill(GREEN)

    for i in range(CELL_CONST):
        for j in range(CELL_CONST):
            matrix_of_cells[i][j].Draw(mainWindow)
    
    pg.display.update()

    time.tick(FPS)

pg.quit()