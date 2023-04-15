from os import system
from game import *
from board import *
import colorama
from colorama import Fore
import time

colorama.init()

# Rensa skärmen
def clear():
    system("cls")
    
def slowprint(words):
    for i in words:
        print(i, end="", flush=True)
        time.sleep(0.04)
    input()

# Skriv ut en grid baserat på brädans "sida"
def grid(side, board, revealed, marked):

    # Skriv ut alla rader
    for i in range(side-1, -1, -1):
        
        # Skriv ut Y-koordinaten för varje rad
        print(f"{i+1:2d}", end="")
        for j in range(side):
            
            # Om användaren har valt den rutan, skriv ut dess värde (tomt, eller antalet minor runt omkring)
            if revealed[i][j]:
                print(f" {board[i][j]}", end="")
                # Skriv ett mellanrum om det är tomt, gör griden mer clean
            
            # Skriv ut ett M som flagga
            elif marked[i][j]:
                print(f" {Fore.RED}M{Fore.WHITE}", end="")
            
            # Om användaren inte har valt den, skriv ut #
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
    print()
    
    # Skriv ut nedre X-koordinat
    print("                     ", end="")
    for ental in range(0,side-9):
        if ental < 10:
            print(f"{ental} ", end="")
        elif ental < 19:
            print(f"{ental-10} ", end ="")
           
# Räkna antalet minor runt omkring den ruta man valde 
def count_mines(board, row, col):
    count = 0
    
    # Loopar igenom de nio rutorna runt omkring den valda rutan
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            
            # Kolla rutorna runt och lägg till +1 på count för varje mina
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == f"{Fore.RED}M{Fore.WHITE}":
                count += 1
    return count

def reveal_square(side, facit, board, revealed, row, col, board_two):
    
    # Om det inte är en mina vid input
    if facit[row][col] != f"{Fore.RED}M{Fore.WHITE}":
        count = count_mines(facit, row, col)
        
        
        # Skriv ett mellanrum om det är tomt, gör griden mer clean
        if count == 0:
            board[row][col] = " "
            
        # Om det är minor runt, skriv ut count som en sträng
        elif count == 1:
            board[row][col] = (Fore.BLUE + "1" + Fore.WHITE)
            
        elif count == 2:
            board[row][col] = (Fore.GREEN + "2" + Fore.WHITE)
            
        elif count == 3:
            board[row][col] = (Fore.LIGHTRED_EX + "3" + Fore.WHITE)
            
        elif count == 4:
            board[row][col] = (Fore.PURPLE + "4" + Fore.WHITE)
            
        elif count == 5:
            board[row][col] = (Fore.RED + "5" + Fore.WHITE)
            
        elif count == 6:
            board[row][col] = (Fore.CYAN + "6" + Fore.WHITE)
        
        else:
            board[row][col] = str(count)
        
        board_two[row-1][col-1] = "#"
            
        # Revealed för den minan = True, gör så den inte blir vald igen
        revealed[row][col] = True
        
        # Gör så att alla 0 runt också blir revealed
        if count == 0:
            
            # Loopar igenom de 8 rutorna runt omkring den valda rutan
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    
                    # Tar den rutan som bestäms av det ovan och kollar om det är en mina där, 
                    # t.ex om i = 5 och j = 2 så kollar den rutan med koordinaten 5 2
                    if i >= 0 and i < side and j >= 0 and j < side and not revealed[i][j]:
                        
                        # Använder funktionen ovan för att bestämma vad den ska skriva ut
                        reveal_square(side, facit, board, revealed, i, j, board_two)
    
    else:
        board[row][col] = f"{Fore.RED}M{Fore.WHITE}"
        board_two[row][col] = f"{Fore.RED}M{Fore.WHITE}"
        revealed[row]