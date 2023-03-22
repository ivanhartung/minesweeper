import random

def side_and_mines():
    
    x_coordinate = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
    # Definierar sidan "X"
    while True:
        print('What would you like the side "X" to be?')
        side = int(input(">>> "))
        if side <= 26 and side >= 1:
            break
        else:
            print('\nThe side "X" needs to be below or equal to 26, and bigger or equal to 1.\n')
    
    # Skapar en variabel för mängden minor
    while True:
        print("How many mines would you like?")
        mines = int(input(">>> "))
        if mines < 1 or mines > side*side:
            print("\nInvalid number.\n")
        else:
            break
    
    # Skriver ut en grid baserat på sidan "X"
    print("")
    for i in range(side, 0, -1):
        if i < 10:
            print(f" {i}", end="")
            print(side * " #")
        else:
            print(f"{i} ", end="")
            print(side * "# ")

    # Skriver x koordinaten som en bokstav från listan "x_coordinate"
    print("  ", end="")
    for i in range(1,side+1):
        print(f" {x_coordinate[i-1]}", end='')

    # ????
    board = []
    for _ in range(side): 
        board.append([]) # niclas kod
    
    # Minor randomiser
    mines_placed = 0
    while mines_placed < mines:
        x = random.randint(0, side-1)
        y = random.randint(0, side-1)
        if board[x][y] != "*":
            board[x][y] = "*"
            mines_placed += 1


def user_input():
    
    print("Coordinate?")
    coordinate = input(">>> ")
    
    
side_and_mines()
