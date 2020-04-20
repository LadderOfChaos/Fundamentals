lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
repair = 0
for i in range(1,lost_fights+1):
    if i % 2 == 0:
        repair+=helmet
    if i % 3 == 0:
        repair+=sword
    if i % 6 == 0:
        repair+=shield
    if i % 12 == 0:
        repair+=armor
print(f"Gladiator expenses: {repair:.2f} aureus")