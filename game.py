from board import *
from utilities import *

def user_input(side, facit, board, revealed, marked):
    
    while True:
        # User inputs
        print("\nCoordinate? Separate with space.")
        coordinate = input(">>> ")
        
        # Gör inputs till integer efter den splittat
        try:
            col_string, row_string = coordinate.split()
            row = int(row_string)
            col = int(col_string)
        
        # Om den inte funkar
        except ValueError:
            print("\nInvalid input.")
            continue

        # Om input är mer än sidan eller mindre än 1
        if row > side or col > side or row < 1 or col < 1:
            print(f"\nInvalid input. Please enter row and column values between 1 and {side}.")
            continue

        # Om man väljer samma ruta som en gång innan
        if revealed[row-1][col-1]:
            print("\nThis square has already been revealed. Please choose another square.")
            continue
             
        if marked[row-1][col-1]:
            print("\nThis square has already been marked as a potential mine. Please choose another square.")
            continue
        
        # Prompt user to mark or reveal the square
        print("\nEnter 'm' to mark the square as a potential mine, or 'r' to reveal it.")
        choice = input(">>> ")
        
        if choice == "m":
            marked[row-1][col-1] = True
            return True
        elif choice == "r":
            if facit[row-1][col-1] == "*":
                # Förlora
                board[row-1][col-1] = "*"
                return False
            else:
                count = count_mines(facit, row-1, col-1)
                board[row-1][col-1] = str(count) if count > 0 else " "
                revealed[row-1][col-1] = True
                if count == 0:
                    reveal_square(side, facit, board, revealed, row-1, col-1)
                return True
        else:
            print("\nInvalid input. Please enter 'm' to mark the square or 'r' to reveal it.")
            continue
        
def reveal_square(side, facit, board, revealed, row, col):
    
    # Om det inte är en mina vid input
    if facit[row][col] != "*":
        count = count_mines(facit, row, col)
        
        # Skriver ett mellanrum om det är tomt, gör griden mer clean
        if count == 0:
            board[row][col] = " "
        
        # Om det är minor runt skriver den ut count som en string
        else:
            board[row][col] = str(count)
            
        revealed[row][col] = True
        
        # Gör så att alla 0 runt också blir revealed
        if count == 0:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < side and j >= 0 and j < side and not revealed[i][j]:
                        reveal_square(side, facit, board, revealed, i, j)
    
    else:
        board[row][col] = "*"
        revealed[row][col] = True

def main(board):
    
    # Definierar sidan "X"
    while True:
        print('What would you like the side "X" to be?')
        side = int(input(">>> "))
        if side <= 25 and side >= 1:
            break
        else:
            print('\nThe side "X" needs to be below or equal to 25, and bigger or equal to 1.\n')

    # Skapar en variabel för mängden minor
    while True:
        print("How many mines would you like?")
        mines = int(input(">>> "))
        if mines <= side*side and mines >= 1:
            break
        else:
            print(f'\nThe amount of mines needs to be between 1 and {side*side}\n')

    # Gör ett facit utifrån "generate_board"
    facit = generate_board(side, mines)

    board = [[" " for _ in range(side)] for _ in range(side)]
    revealed = [[False for _ in range(side)] for _ in range(side)]
    marked = [[False for _ in range(side)] for _ in range(side)]

    # Spelet
    while True:
        clear()
        grid(side, board, revealed, marked) # Updated to show marked squares
        user_board = user_input(side, facit, board, revealed, marked) # Updated to accept marked squares

        if user_board is False:
            # Förlora
            clear()
            print("You lost!")
            grid(side, board, revealed, marked)
            break

        elif all_revealed(revealed, facit) and all_marked(marked, facit):
            # Vinna
            clear()
            print("You won!")
            grid(side, board, revealed, marked)
            break

if __name__ == "__main__":
    # Definierar board innan
    board = []
    main(board)