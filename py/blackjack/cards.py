# cards module
import random


def createDeck():
    suits = ["of Spades", "of Clubs", "of Diamonds", "of Hearts"]
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = [(card, category) for category in suits for card in list]
    random.shuffle(deck)
    return deck


def blackjackdeck():
    suits = ["of Spades", "of Clubs", "of Diamonds", "of Hearts"]
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    global deck
    deck = [(card, category) for category in suits for card in list]
    random.shuffle(deck)
    return deck


def dealInit(deck, num_of_cards):
    hand = []
    i = 0
    while i <= num_of_cards:
        hand.append(deck.pop())
        i += 1
    return hand


def blackjackscore(hand):
    score = 0
    for card in hand:
        score = score + card[0]
    return score


def draw(deck, hand, num_of_cards):
    i = 0
    while i <= num_of_cards:
        hand.append(deck.pop())
        i += 1
