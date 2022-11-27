# create a class called cards
# suit, rank, value will be it's attributes
# create an object called Deck
# create an object called Player

import random
from random import shuffle

suits = ('Hearts' , 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', "Seven", 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King' , "Ace")
value = {"Two": 2 ,"Three": 3 ,"Four": 4 ,"Five": 5 ,"Six": 6, "Seven": 7 , "Eight" : 8, "Nine" : 9, "Ten" : 10 , "Jack" : 11, "Queen" : 12, "King" : 13, "Ace" : 14}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]    
    def __str__(self):
        return self.rank + " of " + self.suit
# we have to evaluate the value of the rank
# since rank is string we cannot compare it with other cards 
# so will maintain a dictionaries(key:value pair) representing rank & value resp
# print(two_of_hearts.rank) 
# print(three_of_clubs.suit)
# print(two_of_hearts.values > three_of_clubs.values)
class Deck:
    def __init__(self):
        self.all_cards = []
# maintianing an empty list as a deck of card in which each card object will get appended.
        for suit in suits:
            for rank in ranks:
                # two fo loops to iterate through two objects..
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)   
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop() 

# new_deck = Deck()
# new_deck.shuffle()
# mycard = new_deck.deal_one()
# print(mycard)
# print(type(mycard))
# first_card = new_deck.all_cards[0]
# bottom_card = new_deck.all_cards
# print(first_card)
# print(bottom_card)
# print(new_deck.all_cards[-1])
# for cards in new_deck.all_cards:
    # print(cards)        
# print(len(new_deck.all_cards))

class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = [] 
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #list of multiple cards if the cards that player won are more than one
            self.all_cards.extend(new_cards)
        else:
            #for a single card object
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards' 

# new_player = Player("Jose")
# print(new_player)
# print(mycard)
# new_player.add_cards(mycard)
# print(new_player)

# GAME LOGIC

#  Game Setup
player_one = Player("Jose")
player_two = Player("Kaustubh") 
new_deck = Deck()
new_deck.shuffle()

# Distribution of the Cards equally to both players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0  
while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print(f"Player One, Out of Cards!\n Player Two {player_two.name} Wins!")
        game_on = False
        break
# player.one.all_cards are the cards that a player one is holding

    if len(player_two.all_cards) == 0:
        print(f"Player Two, Out of Cards!\n Player One {player_one.name} Wins!")
        game_on = False
        break
# player.Two.all_cards are the cards that a player one is holding

# Start New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
# Player one/two cards are the ones that are on the table 

# while at war

# Three condtions to verify
# Player one > Player Two
# Player one < Player Two
# Player One == Player Two



    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR !!!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print(f"Player Two {player_two.name} Wins!")
                game_on = False
                break
        

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print(f"Player One {player_one.name} Wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())