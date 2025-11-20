import displayboard
import updatepos
import time
import os
from dependency import *
lost = False
grid = displayboard.create_grid(rows,columns)
while True:
    #loss check
    losscheck = []
    for i in updatepos.positions:
        if i in losscheck:
            lost = True
            break
        else:
            losscheck.append(i)
        if i[1] > rows-1 or i[1] < 0:
            lost = True
            break
        if i[0] > columns-1 or i[0] < 0:
            lost = True
            break
    if lost == True:
        break

    time.sleep(0.2)
    os.system('cls')
    updatepos.update_input()
    updatepos.update_coords()
    displayboard.add_fruit(updatepos.positions)
    displayboard.check_eat(updatepos.positions)

    
    for xindex in range(0, columns):
        for yindex in range(0, rows):
            if [xindex, yindex] in updatepos.positions:
                grid[yindex][xindex] = "O"
            elif [xindex,yindex] == fruit_coords:
                grid[yindex][xindex] = "X"
                print('yes')
            else:
                grid[yindex][xindex] = "/"
    for row in grid:
        print(str("".join(i for i in row)))



