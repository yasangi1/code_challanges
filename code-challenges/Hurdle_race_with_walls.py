# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Hurdle race with walls until reached the Goal

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def goal_go():
    if front_is_clear():
        move()
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
while not at_goal():
      goal_go()
print("Reached the goal")

    













