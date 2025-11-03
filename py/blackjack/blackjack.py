#!/usr/bin/env python3
import random
import cards

deck = cards.blackjackdeck()

PLAYERHAND = cards.dealInit(deck, 1)
DEALERHAND = cards.dealInit(deck, 1)
player_score = 0
dealer_score = 0

end = False
endturn = False

while end == False:
    while endturn == False:
        player_score = cards.blackjackscore(PLAYERHAND)
        dealer_score = cards.blackjackscore(DEALERHAND)

        print(f"your hand: {PLAYERHAND}; your score: {player_score}")

        playerturn = int(input("Hit (0) or stand (1): "))
        if playerturn == 0:

            cards.draw(deck, PLAYERHAND, 0)
            player_score = cards.blackjackscore(PLAYERHAND)
            print(f"playerhand: {PLAYERHAND}; playerscore : {player_score}")

        if player_score == 21:
            end = True
            print("Blackjack! You Win")
            break
        elif dealer_score == 21:
            end = True
            print("You lose")
            break
        elif dealer_score > 21:
            end = True
            print("Dealer is busted. You win.")
            break
        elif player_score > 21:
            end = True
            print("You are busted. You lose")
            break

        cont = int(input("Continue (0) or End Turn (1): "))

        if cont != 0:
            endturn = True

    if end == False:

        print("\ndealers turn")
        print(f"dealerhand: {DEALERHAND}")

        while dealer_score <= 15:
            print("Dealer: hit")
            cards.draw(deck, DEALERHAND, 0)
            dealer_score = cards.blackjackscore(DEALERHAND)

        else:
            print("Dealer: Stand")

        dealer_score = cards.blackjackscore(DEALERHAND)
        print(f"Dealerhand: {DEALERHAND}; Dealer Score: {dealer_score}")

        if player_score == 21:
            end = True
            print("Blackjack! You Win")
            break
        elif dealer_score == 21:
            end = True
            print("You lose")
            break
        elif dealer_score > 21:
            end = True
            print("Dealer is busted. You win.")
            break
        elif player_score > 21:
            end = True
            print("You are busted. You lose")
        elif dealer_score < player_score < 21:
            end = True
            print("You win")
        elif player_score < dealer_score < 21:
            end = True
            print("You lose, dealer wins")
        elif dealer_score == player_score:
            end = True
            print("Since its a tie; dealer wins")
