if __name__ == "__main__":
    
    def side():
        print('What would you like the side "X" to be?')
        x = int(input(">>> "))
        
        x_coordinate = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        print("\n")
        for i in range(x, 0, -1):
            print(f"{i} ", end="")
            print(x * "# ")

        print("  ", end="")
        for i in range(1,x+1):
            print(f"{x_coordinate[i-1]} ", end='')
            
    side()

    