import random

cardIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
currentCard = 0
previousCard = 0
previousCard2 = 0
previousCard3 = 0
previousCard4 = 0
previousCard5 = 0
posDealerTotal = [17, 18, 19, 20, 21, 22, 23]
playerTotal = 0

def asciiCard(card):
    if card == 1:
        print(""" ---------
| A       |
|         |
|         |
|       A |
 ---------""")
    elif card == 2:
        print(""" ---------
| 2       |
|         |
|         |
|       2 |
 ---------""")
    elif card == 3:
        print(""" ---------
| 3       |
|         |
|         |
|       3 |
 ---------""")
    elif card == 4:
        print(""" ---------
| 4       |
|         |
|         |
|       4 |   
 ---------""")
    elif card == 5:
        print(""" ---------
| 5       |
|         |
|         |
|       5 |   
 ---------""")
    elif card == 6:
        print(""" ---------
| 6       |
|         |
|         |
|       6 |   
 ---------""")
    elif card == 7:
        print(""" ---------
| 7       |
|         |
|         |
|       7 |   
 ---------""")
    elif card == 8:
        print(""" ---------
| 8       |
|         |
|         |
|       8 |   
 ---------""")
    elif card == 9:
        print(""" ---------
| 9       |
|         |
|         |
|       9 |   
 ---------""")
    elif card == 10:
        print(""" ---------
| 10      |
|         |
|         |
|      10 |   
 ---------""")
    elif card == 11:
        print(""" ---------
| J       |
|         |
|         |
|       J |   
 ---------""")
    elif card == 12:
        print(""" ---------
| Q       |
|         |
|         |
|       Q |   
 ---------""")
    elif card == 13:
        print(""" ---------
| K       |
|         |
|         |
|       K |   
 ---------""")
        

def askRestart():
    global previousCard
    global previousCard2
    global previousCard3
    global previousCard4
    global previousCard5
    global currentCard
    global dealerTotal
    global posDealerTotal

    restart = int(input("Press 1 to play again, 2 to quit. "))

    if restart == 1:
        #resetting all card values
        currentCard = 0
        previousCard = 0
        previousCard2 = 0
        previousCard3 = 0
        previousCard4 = 0
        previousCard5 = 0
        dealerTotal = random.choice(posDealerTotal)

        currentCard = random.choice(cardIndex)
        asciiCard(currentCard)
        previousCard = currentCard
        hitOrStay()
    else:
        print("You have quit, thanks for playing.")

def hitOrStay():
    global previousCard
    global previousCard2
    global previousCard3
    global previousCard4
    global previousCard5
    global currentCard
    global cardIndex
    global dealerTotal
    global posDealerTotal
    global playerTotal

    h_or_s = int(input("Press 1 to hit, 2 to stay. "))

    while h_or_s == 1:
        currentCard = random.choice(cardIndex)
        dealerTotal = random.choice(posDealerTotal)
        #prints all cards as long as they have a value greater than zero
        asciiCard(previousCard5)
        asciiCard(previousCard4)
        asciiCard(previousCard3)
        asciiCard(previousCard2)
        asciiCard(previousCard)
        asciiCard(currentCard)

        playerTotal = previousCard + previousCard2 + previousCard3 + previousCard4 + previousCard5 + currentCard
        print("Your total: ", playerTotal)

        #stores cards in the next back card variable
        previousCard5 = previousCard4
        previousCard4 = previousCard3
        previousCard3 = previousCard2
        previousCard2 = previousCard
        previousCard = currentCard

        if playerTotal > 21:
            print("Bust, you lose!")
            h_or_s = 0
        elif playerTotal < 22:
            h_or_s = int(input("Press 1 to hit, 2 to stay. "))
    else:
        if h_or_s == 2:
            print("You have chosen to stay.")
            if dealerTotal <= 21 and dealerTotal > playerTotal:
                print("Dealer has higher score of " + str(dealerTotal) + ", you lose.")
            else:
                print("You win!")
                print("Dealer score:", dealerTotal)
    askRestart()


#begins program
play = input("Welcome to black jack press enter to play ")

if play == "":
    currentCard = random.choice(cardIndex)
    asciiCard(currentCard)
    previousCard = currentCard
    hitOrStay()