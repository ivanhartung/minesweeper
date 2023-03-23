from os import system
from game import *
from board import *

# Funktion för att cleara terminalen
def clear_terminal():
    system("cls")

# Skriver ut en grid baserat på sidan "X"
def grid(side, X_COORDINATE):
    
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
        print(f" {X_COORDINATE[i-1]}", end='')
