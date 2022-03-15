import random
from deckBuilder import *
from drawMethod import *

# So we don't have to check the parameters, in order for deckBuilder:
# Number of Cards in Deck. If you have partner or companions, this number can go down to 97.
# Land Count. 
# One Drop Mana. I've auto-included Sol Ring. This is more like Llanowar Elves, Birds of Paradise, etc.
# Two Drop Mana. Signets mostly, but I want to make an argument about land retrieval. At this level, I don't think it matters.
# Three Drop Mana. Same arguments about Two Drop dorks.


def deadDrawSim(deck):
    testDeck = deck[:]
    # The above is to avoid pointer and make a shallow copy of the deck. We use this avoid making a new identical deck every time we run this. 
    ourHand = []
    inPlay = []
    startingHandCount = 7
    turn = 0
    generatedMana = 0
    
    random.shuffle(testDeck)

    # Draw Opening Hand
    while(len(ourHand) < (startingHandCount)):
        drawToHand(ourHand, testDeck)

    while((ourHand.count("Land") > 0) or testDeck[0] == "Land" ):
        # Start of Turn
        turn += 1
        # Draw a card
        drawToHand(ourHand, testDeck)
        # Land Drop
        inPlay.append("Land")
        ourHand.remove("Land")
        # Check to see if we can play dorks
        for card in ourHand:
            if(type(card)==int):
                if(card <= inPlay.count("Land")):
                    inPlay.append(card)
                    ourHand.remove(card)
            elif(card == "Sol Ring"):
                inPlay.append(card)
                ourHand.remove(card)
                generatedMana += 1
        # The turn ends and loops.
    generatedMana += len(inPlay)
    passedInfo = [turn, generatedMana, ourHand, inPlay]
    return passedInfo

