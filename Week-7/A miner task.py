def validation(dictionary,key, def_value = 0):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary,templete):
    for k, v in dictionary.items():
        print(templete.format(k, v))
commands = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())

    validation(commands, command)
    commands[command] += quantity


print_dict(commands, '{} -> {}')