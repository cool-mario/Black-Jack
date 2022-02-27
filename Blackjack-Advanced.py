
import random
import time

card_dic = {1:"ace", 11:"jack", 12:"queen", 13:"king"} # for converting numbers to ace, jack, queen, or king
def printHand(numList):  
  hand = []  
  
  for num in numList:
    if num > 1 and num < 11:
      hand.append(num)
    else:       
      hand.append(card_dic[num])   # ace, jack, queen, king
      
  return(hand) # this will be shown to the user


def sumCards(hand):  # get the sum of a hand. Hand argument is in all numbers
  sumOfCards = 0
  allAcesCalculated = False
  
  for cardNum in hand:
    if cardNum >= 11:  
      sumOfCards += 10 # jack, queen, king = 10
      
    elif cardNum == 1:  # ace = 1 or 11
      aceNum = 0     
      for card in hand:   # count how many aces there are for multiple aces in a hand
        if card == 1:
          aceNum += 1
      
      # hand is converted to words because if there are multiple aces, the find ace function would add 11 to the hand, but that's the number for the jack!
      if not allAcesCalculated:
        for aceNum in findAce(printHand(hand),aceNum):
          sumOfCards += aceNum # add ace numbers to sum
          
        allAcesCalculated = True # prevents the aces being added multiple times
      
    else:
      sumOfCards += cardNum  # add normal amount

  return(sumOfCards)

  
def findAce(handWithWords,aceNum):
  aces = [] # stores the number for each ace. 
  
  for i in range(0,aceNum):  # each time find the number for one ace
    # finds the sum of the card but without the ace
    sumOfCardsWoutAce = 0
    for card in handWithWords:
      if card == "jack" or card == "queen" or card == "king":
        sumOfCardsWoutAce += 10
      
      elif card != "ace":  # anything except ace
        sumOfCardsWoutAce += card
    
    # figures out if the ace is 1 or 11
    if (11 + sumOfCardsWoutAce) == 21 and aceNum == 1: 
      handWithWords.append(11)
      handWithWords.remove("ace")
      aces.append(11)

    elif (11 + sumOfCardsWoutAce) < 21: 
      handWithWords.append(11)
      handWithWords.remove("ace")
      aces.append(11)
    
    else: 
      handWithWords.append(1)
      handWithWords.remove("ace")
      aces.append(1)

  return(aces)


print("Welcome to Blackjack!")
input("Press enter to start playing.")




while True:  # playing the whole game multiple times
  
  playerHand = []
  dealerHand = []
  
  for i in range(2):  # make the hands
    playerHand.append(random.randint(1,13))
    dealerHand.append(random.randint(1,13)) 
  
  print("\nHere is your hand:\n" + str(printHand(playerHand)))
  playerHandSum = sumCards(playerHand)
  print("The sum of your cards: " + str(playerHandSum))
  
  while True:  # playing the blackjack game 
    choice = input("Type in H to hit or S to stay: ")
    
    if choice == "H" or choice == "h":
      playerHand.append(random.randint(1,13))   # add a card
      
      print("\nHere is your hand:\n" + str(printHand(playerHand)))
      playerHandSum = sumCards(playerHand)
      print("The sum of your cards: " + str(playerHandSum))
      
      if playerHandSum > 21:  # lose
        print("Oh no, you Busted! :(")
        break
      
      elif playerHandSum == 21:   # win
        print("Blackjack! You win! :D")
        break
    
    if choice == "S" or choice == "s":
      print("\nDealers Turn!\n")
      print("Here is the dealer's hand: \n" + str(printHand(dealerHand)))
      
      while True:  
        time.sleep(0.5)   # the dealer makes a decision
        dealerHandSum = sumCards(dealerHand)
        
        if dealerHandSum < 17: # the dealer will hit as long as his hand is under 17
          print("\nThe dealer hit. Here is the dealer's new hand:")
          dealerHand.append(random.randint(1,13))    # add a card
          dealerHandSum = sumCards(dealerHand) # update the sum because it changed
          
          print(printHand(dealerHand))
          print("The sum of the dealer's cards: " + str(dealerHandSum))
        
        if dealerHandSum >= 17:  # finalize
          time.sleep(0.4)
          print("\nThe dealer finalized his hand.")
          dealerFinalized = True
          break
      
      # checks if the dealer has won or lost since it finalized its hand
      if dealerFinalized:
        
        if sumCards(dealerHand) == 21:
          print("The dealer got Blackjack! :O")
          break
        
        if sumCards(dealerHand) > 21:
          print("The dealer busted, You win! :)")
          break
        
        if sumCards(dealerHand) < 21:  # the sum of dealerHand is in between 17 and 20
          if 21 - dealerHandSum < 21 - sumCards(playerHand):  # if the dealer is closer to 21 
            print("The dealer was closer to 21, you lose ;-;")
            break
          
          elif dealerHandSum == sumCards(playerHand):
            print("It's a tie!! ¯\_(ツ)_/¯")
            break
          
          else:
            print("You're closer to 21, you win! :)")
            break
  
  input("\nPress enter to play again!")


  
  
  
  
