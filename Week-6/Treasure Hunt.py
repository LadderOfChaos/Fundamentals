initial_loot = input().split("|")
command = input().split(" ")

while command[0] != "Yohoho!":

    if command[0] == "Loot":
        for item in range(1,len(command)):
            initial_loot.insert(0,command[item])

    elif command[0] == "Drop":
        index_int = list(map(int, command[1]))
        drop_list =[]
        drop_list.append(initial_loot.pop(index_int[0]))
        initial_loot.append(drop_list[0])


    elif command[0] == "Steal":
        command = list(map(int, command[1]))
        a = command[0]
        stolen_loot =[]
        b = 0
        while b < a:

            stolen_loot.append(initial_loot.pop(-len(initial_loot))
        print(stolen_loot)


    command = input().split(" ")


