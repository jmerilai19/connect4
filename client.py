import connect4

def print_board(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(matrix[y][x], end=" ")
        print()

def connect4_console():
    """Play a game of Connect 4 in the console."""
    
    game = connect4.Game()
    print_board(game.start()[1])
    
    print("Drop a piece in a column by typing the column number. Type 'q' to quit.")

    while True:
        column = input("Column: ")
        
        if column == "q":
            return
        
        try:
            column = int(column)-1
        except ValueError:
            print("Invalid column")
            continue
        
        status, board = game.play(column)

        if status == -1:
            print("Invalid column")
            continue

        print_board(board)
        
        if status == 3:
            print("Player 1 wins!")
            break
        elif status == 4:
            print("Player 2 wins!")
            break
        elif status == 5:
            print("Draw!")
            break
    exit()

if __name__ == "__main__":
    connect4_console()
    