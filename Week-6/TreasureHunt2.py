initial_loot = input().split("|")
line = input().split(" ")

while line[0] != "Yohoho!":
    command = line[0]
    if command == "Loot":
        for item in line[1::]:
            if item not in initial_loot:
                initial_loot.insert(0,item)
    elif command == "Drop":
        index = int(line[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))
    else:
        count_stolen = int(line[1])
        stolen_items = []
        if count_stolen <= len(initial_loot):
            count_stolen == len(initial_loot)
            for _ in range(count_stolen):
                stolen_items = initial_loot[len(initial_loot)- count_stolen::]
        else:
            stolen_items = initial_loot.copy()
            initial_loot.clear()
        print(", ".join(stolen_items))
    line = input().split()
if initial_loot:
    sum = 0
    for item in initial_loot:
        sum += len(item)
    print(f"Average treasure gain: {sum/len(initial_loot):.2f} pirate credits.")