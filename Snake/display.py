import random
def create_grid(rows,columns) -> list:
    grid = []
    for row in range(0,rows):
        grid.append([])
    for row in grid:
        for _ in range(0,columns):
            row.append("/")
    return grid

fruit_present = False
chosen_position = []

def add_fruit(grid,positions) -> None:
    global fruit_present
    global chosen_position
    if fruit_present != True:
        possiblex = [  x for x in range(0,len(grid))  ]
        possibley = [  y for y in range(0,len(grid[0]))  ]
        possible_positions = []
        for x in possiblex:
            for y in possibley:
                if [x,y] not in positions:
                    possible_positions.append([x,y])
        chosen_position = random.choice(possible_positions)
        grid[chosen_position[y][chosen_position[x]]] = "X"

#def eat(grid,positions) -> None:








