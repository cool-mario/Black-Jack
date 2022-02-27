import random
import time

def sumList(list):   # get the sum of the list
  hand = 0
  for number in list:
    hand += number
  return(hand)


print("Welcome to Blackjack!")
input("Press enter to start playing.")
play = True
print()



while True:     # you can play blackjack an infinite amount of times
  playerHand = []
  dealerHand = []
  for i in range(2):
    playerHand.append(random.randint(2,11)) # make the player's hand
    dealerHand.append(random.randint(2,11)) # make the dealer's hand
  
  print("Here is your hand:\n" + str(playerHand))
  
  
  while play:   # playing the blackjack game
    
    choice = input("Type H to hit or S to stay: ")
    
    if choice == "H" or choice == "h":      # The player can hit as long as their hand is smaller than 21
      playerHand.append(random.randint(2,11))   # add a card
      print("Here is your hand:\n" + str(playerHand))
      
      
      if sumList(playerHand) > 21:  # lose
        print("Oh no, you Busted! :(")
        break
        
      elif sumList(playerHand) == 21:   # win
        print("Blackjack! You win! :D")
        break
    
    
    elif choice == "S" or choice == "s":    # this means its the dealers turn
      print("Dealers Turn!\n")
      print("Here is the dealer's hand: \n" + str(dealerHand))
      
      while True:  # the dealer will hit as long as his hand is under 17
        time.sleep(0.4)   # the dealer make a decision
        
        if sumList(dealerHand) < 17: # under 17
          print("The dealer hit. Here is the dealer's new hand:")
          dealerHand.append(random.randint(2,11))
          print(dealerHand)
        
        if sumList(dealerHand) >= 17:  # not under 17
          print("The dealer finalized his hand.")
          dealerFinalized = True
          break
          
      # checks if the dealer has won or lost since it finalized his hand
      if dealerFinalized:
        if sumList(dealerHand) == 21:
          print("The dealer got Blackjack! :O")
          break
        
        if sumList(dealerHand) > 21:
          print("The dealer busted, You win! :)")
          break
        
        if sumList(dealerHand) < 21:  # in between 17 and 20
          if 21 - sumList(dealerHand) < 21 - sumList(playerHand):  # if the dealer is closer to 21 
            print("The dealer was closer to 21, you lose ;-;")
            break
          
          else:
            print("You're closer to 21, you win! :)")
            break
  
  input("\nPress enter to play again!")
  play = True
  print()
