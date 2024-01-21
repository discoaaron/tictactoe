gs = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " ",
}


def update_game_state(coords, player):
    gs[coords] = player


def print_board():
    print(f'''
    |{gs["A1"]}|{gs["A2"]}|{gs["A3"]}|
    |{gs["B1"]}|{gs["B2"]}|{gs["B3"]}|
    |{gs["C1"]}|{gs["C2"]}|{gs["C3"]}|
    ''')


def check_win_condition(player):
    # there are 8 winning states
    # across
    win1 = ["A1", "A2", "A3"]
    win2 = ["B1", "B2", "B3"]
    win3 = ["C1", "C2", "C3"]
    # down
    win4 = ["A1", "B1", "C1"]
    win5 = ["A2", "B2", "C2"]
    win6 = ["A3", "B3", "C3"]
    # diagonals
    win7 = ["A1", "B2", "C3"]
    win8 = ["C1", "B2", "A3"]
    all_win_states = win1, win2, win3, win4, win5, win6, win7, win8

    # get player keys
    player_positions = [k for k, v in gs.items() if v >= player]
    for winState in all_win_states:
        counter = 0
        for position in winState:
            if player_positions.__contains__(position):
                counter += 1
            else:
                break
            if counter == 3:
                return True


def player_input(player):
    print(f'Player {player}\'s turn')
    return input()


def gameplay_loop():
    # Player X = true, player 0 = false
    player_toggle = True
    while True:
        player = 'X' if player_toggle else '0'
        player_position = player_input(player)
        update_game_state(player_position, player)
        print_board()
        if check_win_condition(player):
            print(f'Player {player} wins!')
            return
        player_toggle = not player_toggle


if __name__ == '__main__':
    print('Welcome to tic tac to! ')
    print('Choose a position by typing a coordinate between A1 and B3')
    gameplay_loop()
