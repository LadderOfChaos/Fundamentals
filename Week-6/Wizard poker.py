all_cards = input().split(":")
new_deck = []

while True:
    line = input()
    if line == "Ready":
        print(" ".join(new_deck))
        break
    line = line.split(" ")
    command = line[0]
    card_name = line[1]
    if command == "Add":
        if card_name not in all_cards:
            print("Card not found.")
        else:
            new_deck.append(card_name)
    elif command == "Insert":
        index = int(line[2])
        if card_name not in all_cards or 0 > index >= len(all_cards):
            print("Error!")
        else:
            new_deck.insert(index, card_name)
    elif command == "Remove":
        if card_name not in new_deck:
            print("Card not found.")
        else:
            new_deck.remove(card_name)
    elif command == "Swap":
        second_card_name = line[2]
        i = new_deck.index(card_name)
        j = new_deck.index(second_card_name)
        new_deck[i], new_deck[j] = new_deck[j], new_deck[i]
    elif command == "Shuffle":
        new_deck.reverse()