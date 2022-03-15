def deckBuilder(deckSize, landCount, oneDropMana, twoDropMana, threeDropMana):
    # Set Up an Empty Deck
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
    deck.append("Sol Ring")
    print("Deck Finished!")
    return deck