from deckAnalysis import *

testing = False

sizeOfDeck = 99
landCount = 36
oneDropMana = 0
twoDropMana = 6
threeDropMana = 1

oneLessLand = deckBuilder(sizeOfDeck,landCount-1,oneDropMana,twoDropMana,threeDropMana)
ourDeck = deckBuilder(sizeOfDeck,landCount,oneDropMana,twoDropMana,threeDropMana)
oneMoreLand = deckBuilder(sizeOfDeck,landCount+1,oneDropMana,twoDropMana,threeDropMana)


if testing == True:
    testData = deadDrawSim(ourDeck)
    print(testData)
else:
    print("Our Deck")
    simulateMultipleDraws(ourDeck,100000, 3)
    print("One Less Land")
    simulateMultipleDraws(oneLessLand,100000, 3)
    print("One More Land")
    simulateMultipleDraws(oneMoreLand,100000, 3)