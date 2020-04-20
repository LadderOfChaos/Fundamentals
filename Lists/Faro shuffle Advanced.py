from itertools import chain

cards = input()
cards = cards.split()
shuffles = int(input())
length = len(cards)

for i in range(shuffles):
    list_1 = cards[:length // 2]
    list_2 = cards[length // 2:]
    cards = [[*(list_1[x], list_2[x])] for x in range(length // 2)]
    cards = list(chain(*cards))

print(cards)