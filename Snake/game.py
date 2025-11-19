from updatepos import update_coords
from updatepos import positions
from updatepos import update_input
from display import create_grid
import time
import os
lost = False
rows = 10
columns = 10
grid = create_grid(rows,columns)
while True:
    #loss check
    losscheck = []
    for i in positions:
        if i in losscheck:
            lost = True
            break
        else:
            losscheck.append(i)
        if i[0] > rows-1 or i[0] < 0:
            lost = True
            break
        if i[1] > columns-1 or i[1] < 0:
            lost = True
            break
    if lost == True:
        break

    time.sleep(0.2)
    os.system('cls')
    update_input()
    update_coords()
    for xindex in range(0, columns):
        for yindex in range(0, rows):
            if [xindex, yindex] in positions:
                grid[xindex][yindex] = "O"
            else:
                grid[xindex][yindex] = "/"
    for row in grid:
        print(str("".join(i for i in row)))



