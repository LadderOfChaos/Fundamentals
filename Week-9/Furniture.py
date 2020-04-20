import re
#pattern = r">>(?P<furniture>[A-Za-z0-9]+)<<(?P<price>[0-9]+\.?[0-9]+)!(?P<broika>[0-9]+)"
pattern = r">>(?P<furniture>[A-Za-z0-9]+)<<(?P<price>\[0-9]+(\.[0-9]+)?)!(?P<broika>[0-9]+)"
items = []
total_price = 0
while True:
    current_item = input()
    if current_item == "Purchase":
        break

    match = re.finditer(pattern, current_item,)
    for element in match:
        items.append(element.group('furniture'))
        total_price += float(element.group('price')) * int(element.group('broika'))


print("Bought furniture:")
for item in items:
    print(item)

print(f"Total money spend: {total_price:.2f}")



