from board import *
from utilities import *
        
def main():
    
    # Definierar sidan "X"
    while True:
        print('What would you like the side "X" to be?')
        side = int(input(">>> "))
        if side <= 26 and side >= 1:
            break
        else:
            print('\nThe side "X" needs to be below or equal to 26, and bigger or equal to 1.\n')

    # Skapar en variabel för mängden minor
    while True:
        print("How many mines would you like?")
        mines = int(input(">>> "))
        if mines <= side*side and mines >= 1:
            break
        else:
            print('\Invalid number.\n')
        
    facit = generate_board(side, mines)
    
def user_input(side):
    
    print("Coordinate? Separate with space.")
    coordinate = input(">>> ")
    
    answer = []
    for _ in range(side): 
        answer.append([])
    
    for row in answer:
        for _ in range(side):
            row.append("-")

    
    
if __name__ == "__main__":
    main()