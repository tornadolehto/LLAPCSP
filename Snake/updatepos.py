import keyboard # type: ignore
import dependency


def update_input() -> None:
        invalid_combos = [['up','down'],
                        ['down','up'],
                        ['left','right'],
                        ['right','left']]
        if keyboard.is_pressed('a'):
                dependency.direction = 'left'
        elif keyboard.is_pressed('s'):
                dependency.direction = 'down'
        elif keyboard.is_pressed('d'):
                dependency.direction = 'right'
        elif keyboard.is_pressed('w'):
                dependency.direction = 'up'  
        if [dependency.chosen_direction,dependency.direction] in invalid_combos:
                dependency.direction = str(dependency.chosen_direction)
                

def update_coords() -> None:
        new = dependency.positions[0]
        for coords_index in range(0,len(dependency.positions)-1):
            dependency.positions[coords_index] = list(dependency.positions[coords_index+1])

        if dependency.just_ate == True:
              dependency.positions.insert(0,new) 
              dependency.run_add_fruit = True

        if dependency.chosen_direction == "up":
                dependency.positions[len(dependency.positions)-1][1] -= 1
        elif dependency.chosen_direction == 'down':
                dependency.positions[len(dependency.positions)-1][1] += 1
        elif dependency.chosen_direction == 'left':
                dependency.positions[len(dependency.positions)-1][0] -= 1
        elif dependency.chosen_direction == 'right':
                dependency.positions[len(dependency.positions)-1][0] += 1