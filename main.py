############### Blackjack Project #####################
import random
import art

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 is A and all the 10 are face-cards

def score(cards): #sum of total points
    result = 0
    for index in range(0, len(cards)):
        result += cards[index]

    return result


def checkA(cards): #check if A is 1 or 11
    if (11 in cards):
        if (score(cards) > 21):
            cards[cards.index(11)] = 1


def addCard(cards): #add random card
    cards.append(deck[random.randint(0,len(deck)-1)])

def isBlackjack(cards):#check is there is a blackjack
  # print("using blackjack")
  if 11 in cards and 10 in cards and score(cards) == 21:
    return True
  else:
    return False

def isPlayerWinner(player, bot):#check if player won
  # print("using is player win")
  if score(player) > 21:
    return False
  elif score(bot) > 21:
    return True
  elif score(player) > score(bot):
    return True
  elif score(player) < score(bot):
    return False

def isDraw(player, bot): # check if there is a draw
  # print("using draw")
  if score(player) == score(bot):
    return True
  else:
    return False

def botTurn(cards): # bot draw card
  while True:
    if score(cards) < 17:
      addCard(cards)
      checkA(cards)
    else:
      break

def blackjackGame(): # main code

    playerCard = []
    addCard(playerCard)
    addCard(playerCard)

    botCard = []
    addCard(botCard)
    addCard(botCard)

    #first two card appear

    while True: #loop for player turn
      print(f"Your cards: {playerCard}, your score: {score(playerCard)}")
      print(f"Computer's first card: {botCard[0]}")

      if isBlackjack(botCard):
        break #bot win
      elif isBlackjack(playerCard):
        break #plater win

      drawCard = input("Type 'y' to get another card, type 'n' to pass:")

      if drawCard == 'y':
        addCard(playerCard)
        checkA(playerCard) #11 or 1
        if score(playerCard) > 21:
          break #player lose
      elif drawCard == 'n':
        break #player pass turn to the bot
    
    botTurn(botCard)

    print(f"Your cards: {playerCard}, your score: {score(playerCard)}")
    print(f"Bot cards: {botCard}, bot score: {score(botCard)}")

    if isBlackjack(botCard):
      print("player lose1")

    elif isBlackjack(playerCard):
      print("Player Win1")

    elif isDraw(playerCard, botCard):
      print("Draw")

    elif(isPlayerWinner(playerCard, botCard)):
      print("Player Win3")

    elif(isPlayerWinner(playerCard, botCard)) == False:
      print("Player Lose3")





while True: # repeat game until not
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == "n":
    break
  elif play == "y":
    print(art.logo)
    blackjackGame()


