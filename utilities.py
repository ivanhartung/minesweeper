from os import system
from game import *
from board import *

# Clear
def clear():
    system("cls")

# Skriver ut en grid baserat på sidan "X"
def grid(side, board, revealed):

    # Skriver alla rader
    for i in range(side-1, -1, -1):
        
        # Skriver ut Y koordinat för varje rad
        print(f"{i+1:2d}", end="")
        for j in range(side):
            
            # Om user väljer den rutan, skriv ut dess värde (tomt, eller antalet minor runt omkring)
            if revealed[i][j]:
                print(f" {board[i][j]}", end="")
                
            
            # Om user inte valt den, skriv ut #
            else:
                print(" #", end="")
        print()
        
    # Skriver ut ett värde på X koordinaten
    print("  ", end="")
    for x_coordinate in range(1,side+1):
        if x_coordinate > 9 and x_coordinate < 20:
            print(" 1", end="")
        elif x_coordinate > 19:
            print(" 2", end="")
        else:
            print(f" {x_coordinate}", end="")
    print("")
    print("                     ", end="")
    for ental in range(0,side-9):
        if ental < 10:
            print(f"{ental} ", end="")
        elif ental < 19:
            print(f"{ental-10} ", end ="")
           
# Räknar mängden minor runt omkring den ruta man valde 
def count_mines(board, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            
            # Kollar rutorna runt och lägger till +1 på count för varje mina
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == "*":
                count += 1
    return count

def all_revealed(revealed):
    for row in revealed:
        for square in row:
            if not square:
                return False
    return True

def all_marked(board, facit):
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square != "X" and facit[i][j] == "*":
                return False
    return True