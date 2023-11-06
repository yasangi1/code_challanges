# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# Reeborg challange - Robort find the randomly generated goal.

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
 move()
 turn_left()
 move()
 turn_right()
 move()
 turn_right()
 move()
 turn_left()

#nu_of_hurdles = 6

while not at_goal():
  jump()
    #nu_of_hurdles -= 1
    #print(nu_of_hurdles)
