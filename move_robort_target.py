# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle 1 until 13 position in x - (13(x),1(y)


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

for i in range(1, 13, 2):
  jump()






