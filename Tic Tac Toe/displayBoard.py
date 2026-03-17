import depConstants
import os
def display() -> None:
    os.system('cls')
    addString = ""
    for y in range(0,3):
        for x in range(0,3):
            addString += depConstants.board[y][x] + " "
        print(addString)
        addString = ""

#board coords are in the form board[y][x]
def change_at_coords(coords:list,newChar:str) -> None:
    depConstants.board[coords[1]][coords[0]] = newChar