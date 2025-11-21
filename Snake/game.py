import displayboard
import updatepos
import time
import os
import dependency
lost = False
grid = displayboard.create_grid(dependency.rows,dependency.columns)
iteration = 1
input_buffer = []
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

    time.sleep(0.0125)
    updatepos.update_input()
    input_buffer.append(dependency.direction)

    if iteration % 8 == 0:
        dependency.chosen_direction = input_buffer[len(input_buffer)-1]
        input_buffer = []
        os.system('cls')
        displayboard.check_ate()
        updatepos.update_coords()
        displayboard.add_fruit(dependency.positions)
        for xindex in range(0, dependency.columns):
            for yindex in range(0, dependency.rows):
                if [xindex, yindex] in dependency.positions:
                    grid[yindex][xindex] = dependency.snake_char
                elif [xindex,yindex] == dependency.chosen_position:
                    grid[yindex][xindex] = dependency.fruit_char
                else:
                    grid[yindex][xindex] = dependency.empty_char
        for row in grid:
            print(str("".join(i for i in row)))
        print(f"Score: {dependency.score}")
    iteration += 1
print("You lose! Moron! Idiot!")