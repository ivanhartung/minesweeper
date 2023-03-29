from board import *
from utilities import *
    
def user_input(side, facit):
    
    while True:
        
        # Tar inputs
        
        print("\nCoordinate? Separate with space.")
        coordinate = input(">>> ")

        # Gör inputsen till 2 strings som splittas som blir till integers
        try:
            row_string, column_string = coordinate.split()
            row = int(row_string)
            column = int(column_string)
        
        except ValueError:
            print("\nInvalid input.")
            continue

        if row > side:
            print(f"\nYour x coordinate is greater than your side of {side}")
            
        elif column > side:
            print(f"\nYour y coordinate is greater than your side of {side}")
        
        else:
            
            # Förlora
            if facit[row-1][column-1] == "*":
                print("\nGame over! You hit a mine.")
                return None
            
            else:
                break

    # Lägger user input i en egen lista
    answer = []

    answer.append(row)
    answer.append(column)

    return answer
        
def main(answer):
    
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
    
    # Spelet
    while answer != facit:
        clear()
        grid(side)
        user_answer = user_input(side, facit)
        if user_answer is None: # Chat GPT
            break

if __name__ == "__main__":
   
    # Definierar answer innan
    answer = []
    main(answer)