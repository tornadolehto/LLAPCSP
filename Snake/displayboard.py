import random
from dependency import *

def create_grid(rows,columns) -> list:
    grid = []
    for row in range(0,rows):
        grid.append([])
    for row in grid:
        for _ in range(0,columns):
            row.append("/")
    return grid

def add_fruit(positions) -> None:
    global fruit_present
    global chosen_position
    if fruit_present != True:
        fruit_coords = []
        fruit_present = True
        possiblex = [  x for x in range(columns)  ]
        possibley = [  y for y in range(rows)  ]
        possible_positions = []
        for x in possiblex:
            for y in possibley:
                if [x,y] not in positions:
                    possible_positions.append([x,y])
        chosen_position = random.choice(possible_positions)
        fruit_coords = [chosen_position[1],chosen_position[0]]

def check_eat(positions) -> None:
    global fruit_present
    global ate
    ate = False
    if positions[len(positions)-1] == chosen_position:
        fruit_present = False
        ate = True
        
        










