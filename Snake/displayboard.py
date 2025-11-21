import random
import dependency

def create_grid(rows,columns) -> list:
    grid = []
    for row in range(0,rows):
        grid.append([])
    for row in grid:
        for _ in range(0,columns):
            row.append("/")
    return grid

def add_fruit(positions) -> None:
    print(dependency.run_add_fruit)
    if dependency.run_add_fruit == True:
        dependency.run_add_fruit = False
        possiblex = [  x for x in range(dependency.columns)  ]
        possibley = [  y for y in range(dependency.rows)  ]
        possible_positions = []
        for x in possiblex:
            for y in possibley:
                if [x,y] not in positions:
                    possible_positions.append([x,y])
        dependency.chosen_position = random.choice(possible_positions)
    print(dependency.chosen_position)

def check_ate():
    if dependency.positions[len(dependency.positions)-1] == dependency.chosen_position:
        dependency.just_ate = True
    else:
        dependency.just_ate = False
    print(dependency.just_ate)




        
        










