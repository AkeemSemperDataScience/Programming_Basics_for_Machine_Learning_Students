import math
import random
from collections import Counter

class Card():
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        ret_string = "{} of {}".format(self.rank, self.suit)
        return ret_string

    # Comparison Operators
    def __lt__(self, other):
        self_rank =  Card.rank.index(self.rank)
        other_rank = Card.rank.index(other.rank)
        if self_rank == other_rank:
            self_suit = Card.suits.index(self.suit)
            other_suit = Card.suits.index(other.suit)
            return self_suit < other_suit
        return self_rank < other_rank
    def __gt__(self, other):
        return other.__lt__(self)
    
    def __eq__(self, other):
        return (self.suit == other.suit) and (self.rank == other.rank)
    
class Deck():

    # Card Information
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
    # This stuff is to make a function to convert to short to the short version. 
    # This doesn't really matter function-wise
    short_suits = ['H', 'D', 'C', 'S']
    short_rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'J', 'Q', 'K', 'A']
    @staticmethod
    def tooShort(card):
        return Deck.short_rank[Deck.rank.index(card.rank)]+Deck.short_suits[Deck.suits.index(card.suit)]
    
    def __init__(self, *cards, shuffle=True, populate=False):
        self.deck = []
        
        if populate:
            self.populate52()
        elif len(cards) > 0:
            for card in cards:
                self.deck.append(card)
        if shuffle:
            self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.deck)
    def populate52(self):
        self.deck = []
        for suit in self.suits:
            for value in self.rank:
                self.deck.append(Card(suit, value))
    
    # Override some functions and operators
    def __str__(self):
        return_string = ""
        for i, card in enumerate(self.deck):
            return_string += str(i)+": "+str(card)+"\n"
        return return_string
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return self.deck.__next__()
        except:
            raise StopIteration
    def __len__(self):
        return len(self.deck)
    
    # Deal Cards. Make sure that the cards leave the deck. 
    # Rerutn the hands as a list of Decks
    def deal(self, num_hands=1, card_per_hand=1):
        hands = []
        for i in range(num_hands):
            hand = []
            for j in range(card_per_hand):
                hand.append(self.deck.pop())
            tmp = Deck(*hand, shuffle=False, populate=False)
            #print(hand)
            #print(tmp)
            hands.append(tmp)
        return hands
    
    # Add/Remove Cards
    def addCard(self, card):
        self.deck.append(card)
    def removeCard(self, suit, rank):
        for i, c in enumerate(self.deck):
            if c == Card(suit, rank):
                return self.deck.pop(i)

class Hand(Deck):
    hands = ['High Card', 'Pair', 'Two Pair', 'Trips', 'Straight', 'Flush',
             'Full House', 'Quads', 'Straight Flush', 'Royal Flush']
    
    # Converts a deck to a hand
    @staticmethod
    def deckToHand(deck):
        return Hand(*deck.deck)

    def __init__(self, *cards, size=5):
        self.size = size
        super().__init__(*cards, populate=False)

    # Check different hands
    # This is not complete or perfect!!! 
    def checkFlush(self):
        suit = self.deck[0].suit
        for card in self.deck:
            if card.suit != suit:
                return False
        return True
    def checkPair(self):
        #for i in self.deck:
        #    print(i)
        c = Counter([card.rank for card in self.deck])
        if 2 in c.values():
            return True
        return False
    def checkTrips(self):
        #for i in self.deck:
        #    print(i)
        c = Counter([card.rank for card in self.deck])
        if 3 in c.values():
            return True
        return False
    def checkQuads(self):
        #for i in self.deck:
        #    print(i)
        c = Counter([card.rank for card in self.deck])
        if 4 in c.values():
            return True
        return False
    def checkFullHouse(self):
        if self.checkPair() and self.checkTrips():
            return True
        return False

    
    # Check all the hands that we score and define a score
    def checkHand(self):
        if self.checkFullHouse():
            return 6
        elif self.checkFlush():
            return 5
        elif self.checkTrips():
            return 3
        elif self.checkPair():
            return 1
        else:
            return 0
        

    def __lt__(self, other):
        self_value = self.checkHand()
        other_value = other.checkHand()
        #print(self_value, other_value)
        return self_value < other_value
    
    # Card Swapping
    def dropCards(self, cards):
        for card in cards:
            self.deck.remove(card)
    
    def fillHand(self):
        while len(self.deck) < self.size:
            self.deck.append(self.deck.pop())
    
    def swapCards(self, cards):
        self.dropCards(cards)
        self.fillHand()

