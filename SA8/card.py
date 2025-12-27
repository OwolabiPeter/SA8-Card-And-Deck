# Author: Owolabi
# Date: 10/27/2025
# Purpose: Defines a Card class that represents a single playing card with a value and suit, and displays it

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        if value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        elif value == 1:
            self.value = "Ace"

        if suit == 1:
            self.suit = "clubs"
        elif suit == 2:
            self.suit = "spades"
        elif suit == 3:
            self.suit = "diamonds"
        elif suit == 4:
            self.suit = "hearts"

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)
