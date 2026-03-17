import depConstants
import displayBoard

turn = "X"
won = False

def checkWin(turn:str) -> bool:
    for y in depConstants.board:
        if "".join(y) == turn*3:
            return True
    for x in range(0,3):
        if depConstants.board[0][x] + depConstants.board[1][x] + depConstants.board[2][x] == turn*3:
            return True
    if depConstants.board[2][0] + depConstants.board[1][1] + depConstants.board[0][2] == turn*3:
        return True
    if depConstants.board[2][2] + depConstants.board[1][1] + depConstants.board[0][0] == turn*3:
        return True
    return False

def runTurn(turn: str):
    displayBoard.display()
    coords = input(f"{turn}'s turn. Input coords in the form of XY.")
    while int(coords[0]) > 2 or int(coords[0]) < 0 or int(coords[1]) > 2 or int(coords[1]) < 0:
        coords = input(f"Please input valid coordinates.")
    while depConstants.board[2-(int(coords[1]))][int(coords[0])] != "-":
        coords = input(f"Please do not overlap taken tiles.")
    
    newCoords = [int(coords[0]),2-(int(coords[1]))] #convert to cartesian
    displayBoard.change_at_coords(newCoords,turn)

while True:
    runTurn(turn)
    if checkWin(turn) == True:
        break
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
displayBoard.display()
print(f"{turn}'s win!")