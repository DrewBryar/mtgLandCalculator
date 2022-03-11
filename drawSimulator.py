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
    return deck

newDeck = deckbuilder(99,36,1,3,3)

def drawToHand(arr1, arr2):
    arr1.append(arr2[0])
    arr2.pop(0)

def deadDrawSim(deck, mulligans = 0):
    testDeck = deck
    ourHand = []
    startingHandCount = 7
    turn = 1
    generatedMana = 0
    random.shuffle(testDeck)
    while(len(ourHand) < (startingHandCount-mulligans)):
        drawToHand(ourHand, testDeck)
    
    # Mulligan Handler
    if(ourHand.count("Land") <2):
        mulligans += 1
        deadDrawSim(deck, mulligans)
    
    while(ourHand.count("Land") >= turn):

        drawToHand(ourHand, testDeck)

        # Land Drop
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
    print(len(testDeck))
    return passedInfo

deadDrawSim(newDeck)
deadDrawSim(newDeck)
deadDrawSim(newDeck)

