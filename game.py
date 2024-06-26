class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def compare(self, other, trump_suit):
        value_hierarchy = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if self.suit == other.suit:
            return value_hierarchy.index(self.value) > value_hierarchy.index(other.value)
        elif self.suit == trump_suit:
            return True
        else:
            return False


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

class Game:
    def __init__(self):
        self.deck = []
        self.players = []
        self.trump = None

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def start_game(self):
        self.create_deck()
        self.shuffle_deck()
        self.trump = self.deck[-1]
    


    def add_player(self, name):
        if len(self.players) < 6:
            self.players.append(Player(name))
        else:
            print("Cannot add more players, the game is full.")

    def deal_cards(self):
        for player in self.players:
            for i in range(6):
                if self.deck:
                    player.hand.append(self.draw_card())

    def check_game_over(self):
        # zählt wieviele Spieler noch Karten haben
        players_with_cards = sum(1 for player in self.players if player.hand)

        # wenn nur noch ein Spieler mit Karten ist, Spiel beenden
        if players_with_cards == 1:
            self.end_game()



            
# Spiel starten

game = Game()
game.start_game()

# Spieler hinzufügen
game.add_player("Player1")
game.add_player("Player2")
#game.add_player("Player3")

# Karten initialisieren
game.deal_cards()

# Karten jedes Spielers ausgeben
for player in game.players:
    print(f"{player.name}'s cards:")
    for card in player.hand:
        print(f"{card.value} of {card.suit}")


#Karten für jeden Spieler
card1 = game.players[0].hand[0]
card2 = game.players[1].hand[0]
#card3 = game.players[2].hand[0]

print(f"\nThe trump card is {game.trump.value} of {game.trump.suit}")

# Karten vergleichen
print(f"\nComparing {card1.value} of {card1.suit} and {card2.value} of {card2.suit}")

# Karten vergleichen Spieler mit höherer Karte ausgeben
if card1.compare(card2, game.trump.suit):
    print(f"{game.players[0].name}'s card is higher")
elif card2.compare(card1, game.trump.suit):
    print(f"{game.players[1].name}'s card is higher")
else:
    print("Cards are equal")
    
game.check_game_over()
