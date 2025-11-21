import displayboard
import updatepos
import time
import os
import dependency
lost = False
grid = displayboard.create_grid(dependency.rows,dependency.columns)
while True:
    #loss check
    losscheck = []
    for i in dependency.positions:
        if i in losscheck:
            lost = True
            break
        else:
            losscheck.append(i)
        if i[1] > dependency.rows-1 or i[1] < 0:
            lost = True
            break
        if i[0] > dependency.columns-1 or i[0] < 0:
            lost = True
            break
    if lost == True:
        break

    time.sleep(0.2)
    os.system('cls')
    updatepos.update_input()
    displayboard.check_ate()
    updatepos.update_coords()
    displayboard.add_fruit(dependency.positions)
    for xindex in range(0, dependency.columns):
        for yindex in range(0, dependency.rows):
            if [xindex, yindex] in dependency.positions:
                grid[yindex][xindex] = "O"
            elif [xindex,yindex] == dependency.chosen_position:
                grid[yindex][xindex] = "X"
            else:
                grid[yindex][xindex] = "/"
    for row in grid:
        print(str("".join(i for i in row)))



