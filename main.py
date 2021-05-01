############### Blackjack Project #####################
import random
import art

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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

def isBlackjack(cards):
  # print("using blackjack")
  if 11 in cards and 10 in cards and score(cards) == 21:
    return True
  else:
    return False

def isPlayerWinner(player, bot):
  # print("using is player win")
  if score(player) > 21:
    return False
  elif score(bot) > 21:
    return True
  elif score(player) > score(bot):
    return True
  elif score(player) < score(bot):
    return False

def isDraw(player, bot):
  # print("using draw")
  if score(player) == score(bot):
    return True
  else:
    return False

def botTurn(cards):
  while True:
    if score(cards) < 17:
      addCard(cards)
      checkA(cards)
    else:
      break

def blackjackGame():

    playerCard = []
    addCard(playerCard)
    addCard(playerCard)

    botCard = []
    addCard(botCard)
    addCard(botCard)

    while True:
      print(f"Your cards: {playerCard}, your score: {score(playerCard)}")
      print(f"Computer's first card: {botCard[0]}")

      if isBlackjack(botCard):
        break
      elif isBlackjack(playerCard):
        break

      drawCard = input("Type 'y' to get another card, type 'n' to pass:")

      if drawCard == 'y':
        addCard(playerCard)
        checkA(playerCard)
        if score(playerCard) > 21:
          break
      elif drawCard == 'n':
        break
    
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





while True:
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == "n":
    break
  elif play == "y":
    print(art.logo)
    blackjackGame()


