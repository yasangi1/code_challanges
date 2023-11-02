''' This program marks a spot on a map with an X.
In the starting code, there will a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

On lines 6 and 23, used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

This program that allows to mark a square on the map using a letter-number system. So an input of A3 should place an X at the position shown below:

     A     B     C
 1 ['⬜️', '⬜️', '⬜️']

 2 ['⬜️', '⬜️', '⬜️']

 3 ['X', '⬜️', '⬜️'] 
 
 '''

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
#print(map)
position = input("Where do you want to put the treasure?   ") 

position_index_1 = position[0].lower()
position_index_2 = int(position[1])

if position_index_1 == "a":
  position_index_1 = 0
elif position_index_1 == "b":
  position_index_1 = 1
else:
  position_index_1 = 2


map[position_index_2-1][position_index_1] = 'X'

#print(map)
print(f"{line1}\n{line2}\n{line3}")
