from board import *
from utilities import *

def user_input(side, facit, board, revealed):
    while True:
        # Take inputs
        print("\nCoordinate? Separate with space.")
        coordinate = input(">>> ")

        # Convert inputs to integers
        try:
            row_string, column_string = coordinate.split()
            row = int(row_string)
            column = int(column_string)
        except ValueError:
            print("\nInvalid input.")
            continue

        if row > side or column > side or row < 1 or column < 1:
            print(f"\nInvalid input. Please enter row and column values between 1 and {side}.")
            continue

        # Handle cell that has already been revealed
        if revealed[row-1][column-1]:
            print("\nThis cell has already been revealed. Please choose another cell.")
            continue
            
        # Reveal 
        if facit[row-1][column-1] == "*":
            # Lose game
            board[row-1][column-1] = "*"
            return False
        else:
            # Check adjacent cells for mines and update board
            count = count_mines(facit, row-1, column-1)
            board[row-1][column-1] = str(count) if count > 0 else " "
            revealed[row-1][column-1] = True
            if count == 0:
                reveal_cells(side, facit, board, revealed, row-1, column-1)
            return True
        
def reveal_cells(side, facit, board, revealed, row, col):
    if facit[row][col] != "*":
        count = count_mines(facit, row, col)
        if count == 0:
            board[row][col] = " "
        else:
            board[row][col] = str(count)
        revealed[row][col] = True
        if count == 0:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < side and j >= 0 and j < side and not revealed[i][j]:
                        reveal_cells(side, facit, board, revealed, i, j)
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
            print(f'\nThe amount of mines need to be between {(side*side)} and 1\n')
        
    facit = generate_board(side, mines)
    board = [[" " for _ in range(side)] for _ in range(side)]
    revealed = [[False for _ in range(side)] for _ in range(side)]
    
    # Spelet
    while True:
        clear()
        grid(side, board, revealed)
        user_board = user_input(side, facit, board, revealed)
        if user_board is False:
            # Lose game
            clear()
            print("You lost!")
            grid(side, facit)
            break
        elif board == facit:
            # Win game
            clear()
            print("You won!")
            grid(side, board, revealed)
            break

if __name__ == "__main__":
    # Definierar board innan
    board = []
    main(board)