from board import *
from utilities import *
import colorama
from colorama import Fore

colorama.init()

def user_input(side, facit, board, revealed, marked, board_two):
    
    while True:
        # User inputs
        print(f'\nCoordinate? Separate with space. Write "{Fore.RED}M{Fore.WHITE}" after to mark. ("3 2 {Fore.RED}M{Fore.WHITE}")')
        coordinate = input(">>> ").lower()
        
        if coordinate == "lazy":
            
            try:
                for i in range(side):
                    for j in range(side):
                        if facit[i][j] != f"{Fore.RED}M{Fore.WHITE}":
    
                            count = count_mines(facit, i, j)
                
                            # Skriv ett mellanrum om det är tomt, gör griden mer clean
                            if count == 0:
                                board[i][j] = " "
                                
                            # Om det är minor runt, skriv ut count som en sträng
                            elif count == 1:
                                board[i][j] = (Fore.BLUE + "1" + Fore.WHITE)
                                
                            elif count == 2:
                                board[i][j] = (Fore.GREEN + "2" + Fore.WHITE)
                                
                            elif count == 3:
                                board[i][j] = (Fore.LIGHTRED_EX + "3" + Fore.WHITE)
                                
                            elif count == 4:
                                board[i][j] = (Fore.MAGENTA + "4" + Fore.WHITE)
                                
                            elif count == 5:
                                board[i][j] = (Fore.RED + "5" + Fore.WHITE)
                                
                            elif count == 6:
                                board[i][j] = (Fore.CYAN + "6" + Fore.WHITE)
                            
                            else:
                                board[i][j] = str(count)
                                
                            board_two[i][j] = "#"
                            revealed[i][j] = True
                            
                            if count == 0:
                                reveal_square(side, facit, board, revealed, i, j, board_two)
                                
                            clear()
                            grid(side, board, revealed, marked)
                            
                        elif facit[i][j] == f"{Fore.RED}M{Fore.WHITE}":
                            marked[i][j] = True
                            board_two[i][j] = f"{Fore.RED}M{Fore.WHITE}"
                            
                        if board_two == facit:
                            clear()
                            grid(side, board, revealed, marked)
                            print("\nYou won!")
                            exit()
                            
            except ValueError:
                print("\nInvalid input.")
                continue
            
        elif "m" in coordinate:
        
            # Gör inputs till integer efter den splittat
            try:
                col_string, row_string, flag = coordinate.split()
                row = int(row_string)
                col = int(col_string)
                board_two[row-1][col-1] = f"{Fore.RED}M{Fore.WHITE}"
                marked[row-1][col-1] = True
                return True
            
            # Om det inte funkar
            except ValueError:
                print("\nInvalid input.")
                continue
        
        # debug 
        elif coordinate == "facit":
            print(facit)
        elif coordinate == "board":
            print(board_two)
            
        else:
            
            # Gör inputs till integer efter den splittat
            try:
                col_string, row_string = coordinate.split()
                row = int(row_string)
                col = int(col_string)
            
            # Om det inte funkar
            except ValueError:
                print("\nInvalid input.")
                continue
            
            if facit[row-1][col-1] == f"{Fore.RED}M{Fore.WHITE}":
                    # Förlora
                    board[row-1][col-1] = f"{Fore.RED}M{Fore.WHITE}"
                    board_two[row-1][col-1] = f"{Fore.RED}M{Fore.WHITE}"
                    return False
                
            else:
                count = count_mines(facit, row-1, col-1)
                
                # Skriv ett mellanrum om det är tomt, gör griden mer clean
                if count == 0:
                    board[row-1][col-1] = " "
                    
                # Om det är minor runt, skriv ut count som en sträng
                elif count == 1:
                    board[row-1][col-1] = (Fore.BLUE + "1" + Fore.WHITE)
                    
                elif count == 2:
                    board[row-1][col-1] = (Fore.GREEN + "2" + Fore.WHITE)
                    
                elif count == 3:
                    board[row-1][col-1] = (Fore.LIGHTRED_EX + "3" + Fore.WHITE)
                    
                elif count == 4:
                    board[row-1][col-1] = (Fore.MAGENTA + "4" + Fore.WHITE)
                    
                elif count == 5:
                    board[row-1][col-1] = (Fore.RED + "5" + Fore.WHITE)
                    
                elif count == 6:
                    board[row-1][col-1] = (Fore.CYAN + "6" + Fore.WHITE)
                
                else:
                    board[row-1][col-1] = str(count)
                    
                board_two[row-1][col-1] = "#"
                revealed[row-1][col-1] = True
                if count == 0:
                    reveal_square(side, facit, board, revealed, row-1, col-1, board_two)
                return True

def main(board, board_two):
    
    slowprint("Welcome to Ivan's Minesweeper!")
    
    # Definierar sidan "X"
    while True:
        print('\nWhat would you like the side "X" to be?')
        
        try:
            side = int(input(">>> "))
        except ValueError:
            print("\nEnter integer.\n")
            continue
        
        if side <= 25 and side >= 1:
            break
        else:
            print('\nThe side "X" needs to be below or equal to 25, and bigger or equal to 1.\n')

    # Skapar en variabel för mängden minor
    while True:
        print("How many mines would you like?")
        
        try:
            mines = int(input(">>> "))
        except ValueError:
            print("\nEnter integer.\n")
            continue
            
        if mines <= side*side and mines >= 1:
            break
        else:
            print(f'\nThe amount of mines needs to be between 1 and {side*side}\n')

    # Gör ett facit utifrån "generate_board"
    facit = generate_board(side, mines)

    board = [["#" for _ in range(side)] for _ in range(side)]
    board_two = [["#" for _ in range(side)] for _ in range(side)]
    revealed = [[False for _ in range(side)] for _ in range(side)]
    marked = [[False for _ in range(side)] for _ in range(side)]

    # Spelet
    while True:
        clear()
        grid(side, board, revealed, marked)
        user_board = user_input(side, facit, board, revealed, marked, board_two)
        
        if user_board is False:
            # Förlora
            clear()
            lose(side, facit, revealed, marked, board)
            print("\nYou lost!")
            break

        elif board_two == facit:
            # Vinna
            clear()
            grid(side, board, revealed, marked)
            print("\nYou won!")
            break

if __name__ == "__main__":
    # Definierar board innan
    # Board_two finns för att jämföra med facit
    board = []
    board_two = []
    main(board, board_two)