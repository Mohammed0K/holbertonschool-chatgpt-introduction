#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    # check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # input validation for row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row in (0, 1, 2):
                    break
                else:
                    print("Row must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number 0, 1, or 2.")

        # input validation for column
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col in (0, 1, 2):
                    break
                else:
                    print("Column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number 0, 1, or 2.")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # make move
        board[row][col] = player

        # check for win
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return

        # check for draw
        if all(cell != " " for r in board for cell in r):
            print_board(board)
            print("It's a draw!")
            return

        # switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

