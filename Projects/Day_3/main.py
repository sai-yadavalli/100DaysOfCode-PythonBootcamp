def initialize():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

def treasureIsland():
    initialize()
    direction = input("left or right? ")
    if (direction == "left"):
        nextMove = input("swim or wait? ")
        
        if (nextMove == "wait"):
            door = str(input("Which door? "))

            if (door == "red"):
                print("Burned by fire.")
                print("Game Over.")
                treasureIsland()

            elif (door == "blue"):
                print("Eaten by beasts.")
                print("Game Over.")
                treasureIsland()
            
            elif (door == "yellow"):
                print("You Win!")
                treasureIsland()
            
            else:
                print("Game Over.")
                treasureIsland()
        
        elif (nextMove == "swim" | (nextMove != "wait" & nextMove != "swim")):
            print("Attacked by trout.")
            print("Game Over.")
            treasureIsland()
        
    elif (direction == "right" | (direction != "left" & direction != "right")):
        print("Fall into a hole.")
        print("Game Over.")
        treasureIsland()

treasureIsland()


