class Player:

    def __init__(self, given_name):
        self.__name = given_name
        self.__score = 0

class PlayingCard:

    def __init__(self, given_suit, given_rank, given_value):
        self.__suit = given_suit
        self.__rank = given_rank
        self.__value = given_value


class Deck:

    def __init__(self):
        self.__cards = []
        # Code to generate a deck of cards here
# mygame = Deck.

def shuffle(self):
    # Code to shuffle cards here
    pass


def deal(self):
    # Code to deal a card from the deck
    pass

player_name = input("Enter your name ")
game_player = Player(player_name)


class Deck:

    def __init__(self):
        self.__cards = []

        # Generate a deck of cards
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for i in range(4):  # For each suit
            for j in range(13):  # For each rank in suit
                new_card = PlayingCard(suits[i], ranks[j], values[j])
                self.__cards.append(new_card)
