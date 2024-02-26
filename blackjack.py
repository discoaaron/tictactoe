import random


class Player:
    cards: []

    def add_card(self, card):
        self.cards.append(card)

game_state = {
    'Player': 0,
    'Dealer': 0
}


def random_suit():
    suit = random.randrange(0, 4)
    match suit:
        case 0:
            return 'Sperde'
        case 1:
            return 'Heards'
        case 3:
            return 'Clud'
        case 4:
            return 'Diodond'


def random_card():
    return random.randrange(0, 13)


def deal_card_to_player(player):
    card_number = random_card()
    card_suit = random_suit()
    game_state[player] += card_number


def gameplay_loop():
    card_number = random_card()
    card_suit = random_suit()
    game_state['Player'] += card_number
    print(f'Your card is {card_number} of {card_suit}')
    print(f'Current score: {game_state['Player']}')


def start_game():
    print('Welcome to blackjack! ')
    player_cards = Player()
    house_cards = Player()
    gameplay_loop()
