import keyboard # type: ignore
import dependency

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
  
        new = dependency.positions[0]
        for coords_index in range(0,len(dependency.positions)-1):
            dependency.positions[coords_index] = list(dependency.positions[coords_index+1])

        print(dependency.just_ate)
        if dependency.just_ate == True: #bricking out on this condition no idea why
              print('added')
              dependency.positions.insert(0,new) 
              dependency.run_add_fruit = True
        
        if direction == "up":
                dependency.positions[len(dependency.positions)-1][1] -= 1
        elif direction == 'down':
                dependency.positions[len(dependency.positions)-1][1] += 1
        elif direction == 'left':
                dependency.positions[len(dependency.positions)-1][0] -= 1
        elif direction == 'right':
                dependency.positions[len(dependency.positions)-1][0] += 1
        print(dependency.positions)
                     





        

    

