from os import system
from game import *
from board import *

# Clear board
def clear():
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
    for x_coordinate in range(1,side+1):
        if x_coordinate > 9 and x_coordinate < 20:
            print(" 1", end="")
        elif x_coordinate > 19:
            print(" 2", end="")
        else:
            print(f" {x_coordinate}", end="")
    print("")
    print("                     ", end="")
    n = 0
    for ental in range(0,side-9):
        if ental < 10:
            print(f"{ental} ", end="")
        elif ental < 19:
            print(f"{ental-10} ", end ="")