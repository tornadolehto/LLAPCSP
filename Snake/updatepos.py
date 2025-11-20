positions = [[0,0],[1,0],[2,0]] #tail ---> head
import keyboard # type: ignore
from dependency import *

direction = "right"
def update_input() -> None:
    global direction
    if keyboard.is_pressed('a'):
         direction = 'left'
    elif keyboard.is_pressed('s'):
         direction = 'down'
    elif keyboard.is_pressed('d'):
         direction = 'right'
    elif keyboard.is_pressed('w'):
         direction = 'up'           

def update_coords() -> None:
        new = positions[0]
        for coords_index in range(0,len(positions)-1):
            positions[coords_index] = list(positions[coords_index+1])

        if ate == True:
              positions.insert(0,new)
        
        if direction == "up":
                positions[len(positions)-1][1] -= 1
        elif direction == 'down':
                positions[len(positions)-1][1] += 1
        elif direction == 'left':
                positions[len(positions)-1][0] -= 1
        elif direction == 'right':
                positions[len(positions)-1][0] += 1
                     





        

    

