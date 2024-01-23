import tictactoe


def choose_game():
    print('Choose a game by typing the game name')
    print('Games:')
    print('  tictactoe')
    game = input()
    if game == 'tictactoe':
        tictactoe.start_game()
    else:
        print('Ya dun messed up A-A-ron!')


if __name__ == '__main__':
    choose_game()
