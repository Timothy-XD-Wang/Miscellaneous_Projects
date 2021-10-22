# printing a deck of 52 cards organized by suit and rank
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cardValues = ["Ace", 2, 3, 3, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

for suit in suits:
    for cardValue in cardValues:
        print(cardValue, "of", suit)

print()
