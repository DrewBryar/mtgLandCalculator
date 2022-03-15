from lib2to3.pgen2.pgen import generate_grammar
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.style import available

from sklearn.utils import shuffle


def deckbuilder(deckSize, landCount, oneDropMana, twoDropMana, threeDropMana):
    deck = []

    while (len(deck) < landCount):
        deck.append("Land")
    for x in range(oneDropMana):
        deck.append(1)
    for x in range(twoDropMana):
        deck.append(2)
    for x in range(threeDropMana):
        deck.append(3)
    while(len(deck) < deckSize):
        deck.append("Non-Land")
    
    print("Deck Finished!")
    print(deck)
    print(len(deck))
    return deck

newDeck = deckbuilder(99,36,1,3,3)

def drawToHand(arr1, arr2):
    if(len(arr2) != 0):
        arr1.append(arr2[0])
        arr2.pop(0)
    else:
        print("You drew yourself out! You lose.")
        return 0

def deadDrawSim(deck, mulligans = 0):
    testDeck = deck[:]
    # The above is to avoid pointer and make a shallow copy of the deck. We use this avoid making a new identical deck every time we run this. 
    ourHand = []
    startingHandCount = 7
    turn = 0
    generatedMana = 0
    
    random.shuffle(testDeck)

    while(len(ourHand) < (startingHandCount-mulligans)):
        drawToHand(ourHand, testDeck)
    
    # Mulligan Handler ***********
    if(ourHand.count("Land") <2):
        mulligans += 1
        deadDrawSim(deck, mulligans)
    
    while(ourHand.count("Land") > 0):

        drawToHand(ourHand, testDeck)

        # Land Drop
        
        ourHand.remove("Land")
        generatedMana += 1
        availableMana = generatedMana

        # Check to see if we can play dorks
        for card in ourHand:
            if(type(card)==int):
                if(card <= availableMana):
                    availableMana-=card
                    ourHand.remove(card)
                    generatedMana += 1
        # Next Turn
        turn += 1
    passedInfo = [mulligans, turn, generatedMana]
    print(passedInfo)
    return passedInfo

def simulateMultipleDraws(deck, x):
    totalData = []
    for i in range(x):
        totalData.append(deadDrawSim(deck))
    
    return totalData

def deckDataAnalysis(data):
    totalMulligans = []
    totalTurns = []
    totalMana = []
    manaPerTurn =[]
    for x in range(len(data)):
        totalMulligans.append(data[x][0])
        totalTurns.append(data[x][1])
        totalMana.append(data[x][2])
        manaPerTurn.append((data[x][2])/data[x][1])



    totalMulligans.sort()
    totalTurns.sort()
    totalMana.sort()
    manaPerTurn.sort()

    plt.plot(totalMulligans, 'r')
    plt.ylabel("Mulligans")
    plt.show()

    plt.plot(totalTurns, 'b')
    plt.ylabel("Turn Limit")
    plt.show()

    plt.plot(totalMana, 'g')
    plt.ylabel("Mana Generated")
    plt.show()

    
    plt.plot(manaPerTurn, 'p')
    plt.ylabel("Mana Generated Per Turn Limit")
    plt.show()


deadDrawSim(newDeck)
deckDataAnalysis(simulateMultipleDraws(newDeck, 20))