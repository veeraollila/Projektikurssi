import random

# Building the UNO deck
def buildDeck():
    deck = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]

    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck

#Shuffle
def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)

print(unoDeck)