import random
from game import *
from utilities import *

def generate_board(side, mines):
    
    # Skapar en tom array med "side" antal rader
    facit = []
    for _ in range(side): 
        facit.append([])
    
    # Fyller varje rad i facit-arrayen med "#" "side" antal gånger, 
    # för att senare kunna jämföra med spelarens board
    for row in facit:
        for _ in range(side):
            row.append("#")
    
    # Placerar ut minor slumpmässigt tills antalet minor blir samma som "mines", 
    # definierat i game.py
    mines_placed = 0
    while mines_placed < mines:
        x = random.randint(0, side-1)
        y = random.randint(0, side-1)
        # Om koordinaten inte redan innehåller en mina, lägg till en mina på koordinaten
        if facit[x][y] != f"{Fore.RED}M{Fore.WHITE}":
            facit[x][y] = f"{Fore.RED}M{Fore.WHITE}"
            mines_placed += 1
    
    # Returnerar facit-arrayen som spelplan
    return facit

def lose(side, facit, revealed, marked, board):
    # Skriv ut alla rader
    for i in range(side-1, -1, -1):
        
        # Skriv ut Y-koordinaten för varje rad
        print(f"{i+1:2d}", end="")
        
        for j in range(side):
            
            # Om användaren har valt den rutan, skriv ut dess värde (tomt, eller antalet minor runt omkring)
            if revealed[i][j]:
                print(f" {board[i][j]}", end="")
            
            # Skriv ut ett M som flagga
            elif marked[i][j]:
                print(f" {Fore.RED}M{Fore.WHITE}", end="")
            
            else:
                if facit[i][j] == f"{Fore.RED}M{Fore.WHITE}":
                    print(f" {Fore.RED}M{Fore.WHITE}", end="")
                else:
                    print(" #", end="")
                
        print()
        
    # Skriv ut övre X-koordinat
    print("  ", end="")
    for x_coordinate in range(1,side+1):
        if x_coordinate > 9 and x_coordinate < 20:
            print(" 1", end="")
        elif x_coordinate > 19:
            print(" 2", end="")
        else:
            print(f" {x_coordinate}", end="")
    print("")

    # Skriv ut nedre X-koordinat
    print("                     ", end="")
    for ental in range(0,side-9):
        if ental < 10:
            print(f"{ental} ", end="")
        elif ental < 19:
            print(f"{ental-10} ", end ="")
            