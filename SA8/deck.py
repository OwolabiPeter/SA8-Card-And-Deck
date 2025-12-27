# Author: Owolabi
# Date: 10/27/2025
# Purpose: Defines a Deck class that creates, shuffles, and deals a standard deck of 52 playing cards.

from random import randint
from card import Card

class Deck:
    def __init__(self):
        # Create an empty list to store Card objects
        self.card_list = []

    def add_standard_cards(self):
        # Add all 52 standard playing cards to the deck
        # 4 suits and 13 values per suit
        for suit in range(1, 5):
            for value in range(1, 14):
                # Create a new card and add it to the deck
                self.card_list.append(Card(value, suit))

    def shuffle(self):
        # Randomly shuffle the cards in the deck
        n = len(self.card_list)
        for i in range(n):
            # Pick a random index to swap with
            j = randint(0, n - 1)

            # Use a variable to temporarily store one card
            holder = self.card_list[i]

            # Swap the two cards
            self.card_list[i] = self.card_list[j]
            self.card_list[j] = holder

    def deal(self, num_cards):
        # Create a new Deck object to represent the hand (cards being dealt)
        new_deck = Deck()

        # Remove cards from the end of the deck and add them to the new deck
        for i in range(num_cards):
            if len(self.card_list) > 0:
                new_deck.card_list.append(self.card_list.pop())

        # Return the hand
        return new_deck
