import random
#This class represents the cards in the deck
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
    
#This class represents the deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "clubs", "spades"]

        ranks = [{"rank": "2", "value": 2}, 
                {"rank": "3", "value": 3}, 
                {"rank": "4", "value": 4}, 
                {"rank": "5", "value": 5}, 
                {"rank": "6", "value": 6}, 
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9}, 
                {"rank": "10", "value": 10}, 
                {"rank": "J", "value": 10}, 
                {"rank": "Q", "value": 10}, 
                {"rank": "K", "value": 10}, 
                {"rank": "A", "value": 11}
                ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    #This function just shuffles the cards       
    def shuffle(self):
        if len(self.cards) <= 1:    
            return "No cards to shuffle"
        elif len(self.cards) > 1:
            random.shuffle(self.cards)
            return
        
    #This function deals the cards
    def deal(self, number):
        cards_dealt = []
        for i in range(number):
            if len(self.cards) == 0:
                return "No more cards to deal"
            elif len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        
        return cards_dealt
    
#This class represents the hand of cards
class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
#This function adds cards to the hand
    def add_card(self, card_list):
        self.cards.extend(card_list)
#This function calculates the value of the hand
    def calculate_value(self):
        self.value = 0 
        hasAce = False 
        for card in self.cards:
            self.value += int(card.rank['value'])
            if card.rank['rank'] == 'A':
                hasAce = True
        if hasAce and self.value > 21:
            self.value -= 10
#This function returns the value of the hand
    def getValue(self):
        self.calculate_value()
        return self.value
#This function checks if the hand is a blackjack
    def isBlackJack(self):
        return self.getValue == 21
#This function displays the hand   
    def display(self, showDealerCard = False):
        print (f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not showDealerCard and not self.isBlackJack():    
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print(f"Value: {self.getValue()}")
        print()

#          
class Game:
    def play(self):
        gameNumber = 0
        gamesToPlay = 0


        while gamesToPlay <= 0:
            try:
                gamesToPlay = int(input("How many games would you like to play? "))
            except ValueError:
                print("Please enter a number")
        
        while gameNumber < gamesToPlay:
            gameNumber += 1

            deck = Deck()
            deck.shuffle()
            playerHand = Hand()
            dealerHand = Hand(dealer = True)

            for i in range(2):
                playerHand.add_card(deck.deal(1))
                dealerHand.add_card(deck.deal(1))

            print()
            print("x" * 50)
            print(f"Game {gameNumber} of {gamesToPlay}")
            print("x" * 50)             
            print()
            playerHand.display()
            dealerHand.display() 

            if self.checkWinner(playerHand, dealerHand):
                continue

            choices= ""
            while playerHand.getValue() < 21 and choices not in ["stand", "s"]:
                choices = input("Do you want to hit or stand? ").lower()
                print()
                while choices not in ["hit", "h", "stand", "s"]:
                    choices = input("Please enter hit or stand (or H/S): ").lower()
                    print()
                if choices in ["hit", "h"]:
                    playerHand.add_card(deck.deal(1))
                    playerHand.display()
                    
            if self.checkWinner(playerHand, dealerHand):
                continue

            playerHandValue = playerHand.getValue()
            dealerHandValue = dealerHand.getValue()

            while dealerHandValue < 17:
                dealerHand.add_card(deck.deal(13))
                dealerHandValue = dealerHand.getValue()

            dealerHand.display(showDealerCard = True)

            if self.checkWinner(playerHand, dealerHand):
                continue

            print("Game Over")
            print("Final Results")
            print("Your hand: ", playerHandValue)
            print("Dealer's hand: ", dealerHandValue)

            self.checkWinner(playerHand, dealerHand, gameOver = True)

        print("\nThanks for playing")

#This function checks the winner of the game
    def checkWinner(self, playerHand, dealerHand, gameOver = False):
        if not gameOver:
            if playerHand.isBlackJack() and dealerHand.isBlackJack():
                print("It's a tie") 
                return True 
            elif playerHand.getValue() > 21:
                print ("You busted! Dealer wins")
                return True 
            elif dealerHand.getValue() > 21:                                                                    
                print("Dealer busted! You win")
                return True 
            elif playerHand.isBlackJack():
                print("Blackjack! You win")
                return True      
            elif dealerHand.isBlackJack():
                print("Dealer has Blackjack! Dealer wins")
                return True
            
        else:
            if playerHand.getValue() == dealerHand.getValue():
                print("It's a tie") 
            elif playerHand.getValue() > dealerHand.getValue():
                print("You win")
            else:
                print("Dealer wins")
            return True

        
    

         
        return False      

g = Game()
g.play()
