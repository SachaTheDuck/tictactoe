while True:
    board = [" " for _ in range(9)]


    def Board(a, winner=None):
        print(" " + a[0] + " | " + a[1] + " | " + a[2] + " ")
        print("---+---+---")
        print(" " + a[3] + " | " + a[4] + " | " + a[5] + " ")
        print("---+---+---")
        print(" " + a[6] + " | " + a[7] + " | " + a[8] + " ")

        if winner:
            print("> Game ended. The winner is Player {0}.".format(winner))


    def Tictactoe():
        player = "X"
        round = 0

        while True:
            Board(board, None)
            print("> Player's " + player + " round. [Tip : type a number from 1 to 9]")
            move = int(input()) - 1

            if move > 8:
                print("> You need to take a number between 1 and 9.")
                continue

            if board[move] == " ":
                board[move] = player
                round += 1
            else:
                print("> This tile is already taken.")
                continue

            if board[0] == board[1] == board[2] != " " \
                    or board[3] == board[4] == board[5] != " " \
                    or board[6] == board[7] == board[8] != " " \
                    or board[0] == board[3] == board[6] != " " \
                    or board[1] == board[4] == board[7] != " " \
                    or board[2] == board[5] == board[8] != " " \
                    or board[0] == board[4] == board[8] != " " \
                    or board[2] == board[4] == board[6] != " ":
                Board(board, player)
                break

            if round == 9:
                print("> Draw.")
                break

            player = "O" if player == "X" else "X"


    if __name__ == "__main__":
            Tictactoe()
