# main.py

from player import HumanPlayer, BotPlayer
from tic_tac_toe_game import TicTacToeGame

def start_game():
    player1 = HumanPlayer('X')
    choice = input("Play against another player (2) or bot (1)? ")
    player2 = BotPlayer('O') if choice == '1' else HumanPlayer('O')

    game = TicTacToeGame(player1, player2)
    game.play_game()

if __name__ == '__main__':
    while True:
        start_game()
        try_again = input("Do you want to play again? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break
