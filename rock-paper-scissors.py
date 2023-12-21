from getpass import getpass as input

player1_win = 0
player2_win = 0

while True:
    if player1_win == 3:
        exit(print("Player 1 wins 3 rounds. Thanks for playing!"))
    elif player2_win == 3:
        exit(print("Player 2 wins 3 rounds. Thanks for playing!"))

    player1 = input("Player 1, choose R, P, or S: ")
    player2 = input("Player 2, choose R, P, or S: ")

    player_choices = {player1: player2}
    losing_pair = {"R": "P", "P": "S", "S": "R"}

    # Compare if one dict appears in another
    if player1 == player2:
        print("Tie")
        continue
    elif player1 in losing_pair and player2 == losing_pair[player1]:
        player2_win += 1
        print(
            f"Player 1 chooses {player1} which is countered by Player 2's {player2}. Player 2 wins."
        )
        continue
    else:
        player1_win += 1
        print(
            f"Player 2 chooses {player2} which is countered by Player 1's {player1}. Player 1 wins."
        )
        continue
