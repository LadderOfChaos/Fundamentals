def available_chairs(word):                #xxxxx
    return len(word[0])

def needed(word):                  #INT
    map(int, word)
    return word[1]
rooms = int(input())
for room in range(rooms):
    word = input().split(" ")
    taken = 0
    free = 0
    if available_chairs(word) > needed(word):
        free += available_chairs(word) - needed(word)
    elif available_chairs(word) < needed(word):
        needed_chairs = needed(word) - available_chairs(word)
        print(f"{needed_chairs} more chairs needed in room {room}")
