from os import system
from game import *
from board import *

# Funktion för att cleara terminalen
def clear_terminal():
    system("cls")

# Skriver ut en grid baserat på sidan "X"
def grid(side):

    # Skriver ut alla rader och kolumner, med Y koordinat innan
    for i in range(side, 0, -1):
        if i < 10:
            print(f" {i}", end="")
        else:
            print(f"{i}", end="")
        for _ in range(1, side+1):
            print(" #", end="")
        print("")
        
    # Skriver ut ett värde på X koordinaten
    print("  ", end="")
    for x_coordinate in range(1,side):
        print(f" {x_coordinate}", end="")
    print("")