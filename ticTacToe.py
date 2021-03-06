board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]


def display_board():
    print(
        board[6] + " | " + board[7] + " | " + board[8] + "\n" +
        board[3] + " | " + board[4] + " | " + board[5] + "\n" +
        board[0] + " | " + board[1] + " | " + board[2]
    )


def play_game():
    display_board()
    plays = 0
    winner = False

    while plays < 9:
        plays += 2
        player_turn(1)
        if win_check(1):
            winner = True
            print("Congratulations, player 1 wins the game!")
            break
        if plays < 9:
            player_turn(2)
            if win_check(2):
                winner = True
                print("Congratulations, player 2 wins the game!")
                break

    if not winner:
        print("Draw game")


def win_check(player):
    if player == 1:
        piece = "X"
    elif player == 2:
        piece = "O"

    if (board[0] == piece and board[1] == piece and board[2] == piece) or \
            (board[3] == piece and board[4] == piece and board[5] == piece) or \
            (board[6] == piece and board[7] == piece and board[8] == piece) or \
            (board[0] == piece and board[3] == piece and board[6] == piece) or \
            (board[1] == piece and board[4] == piece and board[7] == piece) or \
            (board[2] == piece and board[5] == piece and board[8] == piece) or \
            (board[0] == piece and board[4] == piece and board[8] == piece) or \
            (board[6] == piece and board[4] == piece and board[2] == piece):
        return True


def player_turn(player):
    while True:
        player_input = input(f'Player {player}, choose a spot on the board: ')
        try:
            val = int(player_input)
            if (val in range(1, 10) and player_input.isdigit())\
                    and not (board[int(player_input) - 1] == "X" or board[int(player_input) - 1] == "O"):
                if player == 1:
                    board[int(player_input) - 1] = "X"
                else:
                    board[int(player_input) - 1] = "O"
                break
            else:
                print("Please choose 1-9 on an empty spot")
        except ValueError:
            print("Not a valid number")

    display_board()


play_game()
