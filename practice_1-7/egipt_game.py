from random import randint
import acsi_art


easy = [3, 3]
mid = [5, 5]
hard = [7, 7]
game_inprogress = False
lifes = 0
columns_map_treasure = []
normal_column = []
game_map = []



print(acsi_art.nefertiti)
print("Welcome and good luck finding the treasure!")


# level selection
# map_columns
# map_rows
# game_inprogress = True
# lifes = 2, 4, 6

while game_inprogress is not True:
    level = int(input("Select your level: Type 0-easy, 1-mid, 2-hard\n"))
    if level == 0:
        map_columns = easy[0]
        map_rows = easy[1]
        game_inprogress = True
        lifes = 2
        print("easy selected\n")
    elif level == 1:
        map_columns = mid[0]
        map_rows = mid[1]
        game_inprogress = True
        lifes = 4
        print("mid selected\n")
    elif level == 2:
        map_columns = hard[0]
        map_rows = hard[1]
        game_inprogress = True
        lifes = 6
        print("hard selected\n")
    else:
        print("wrong entry!")
        game_inprogress = False

#Map Setup
treasure_location_column = randint(0,map_columns-1)
treasure_location_row = randint(0, map_rows-1)

for i in range(map_columns):
    normal_column.append(False)

for i in range(map_columns):
    if i == treasure_location_column:
        columns_map_treasure.append(True)
    else:
        columns_map_treasure.append(False)

for i in range(map_rows):
    if i == treasure_location_row:
        game_map.append(columns_map_treasure)
    else:
        game_map.append(normal_column)


#print map
for item in game_map:
    print(f"{item}\n")




