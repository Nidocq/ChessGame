import random

deck = ['noget', 'andet noget', 'cancer', 'hop', 2, 3, 4, 5, 6, 7, 8, 9, 190, 304]


print(deck)
for i in range(30):
    ranint = random.randint(0,len(deck)-1)
    value = deck[ranint]
    del deck[ranint]
    deck.append(value)

print(deck)
