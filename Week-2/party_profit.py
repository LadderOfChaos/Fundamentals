from math import floor
party_size = int(input())
days = int(input())
total_money = 0

# dayly_food = 2 * party_size
# every 3 days party = 3 * party_size
# every 5 days +20 * party_size if day 5 and 3    spent 2*party_size
# evert 10 days -2 party_size but every 15 days +5 party_size



for i in range(1,days+1):
    if i % 10 == 0:
       party_size -= 2

    if i % 15 == 0:
        party_size+=5

    total_money += 50 - (2 * party_size)

    if i % 3 == 0:
        total_money -= 3 * party_size
    if i % 5 == 0:
        total_money += 20 * party_size
    if i % 15 == 0:
        total_money -=2*party_size



sum = floor(total_money / party_size)
print(f"{party_size} companions received {sum} coins each.")


