import random

def generate_board(side, mines):
    
    # Facit
    facit = []
    for _ in range(side): 
        facit.append([])
    
    for row in facit:
        for _ in range(side):
            row.append("-")
    
    # Minor randomizer
    mines_placed = 0
    while mines_placed < mines:
        x = random.randint(0, side-1)
        y = random.randint(0, side-1)
        if facit[x][y] != "*":
            facit[x][y] = "*"
            mines_placed += 1
    
    #temp
    print(facit)
    
    return facit