books_collection = list(map(str, input().split("&")))
check_book = ''

while True:
    command_line = input()
    if 'Done' in command_line:
        break
    else:
        command_line = command_line.split(' | ')
        operation = command_line[0]
        book = command_line[1]

        if 'Add Book' in operation and book not in books_collection:
            books_collection.insert(0, book)
        elif 'Take Book' in operation and book in books_collection:
            books_collection.remove(book)
        elif 'Swap Books' in operation and book in books_collection and command_line[2] in books_collection:
            book2 = command_line[2]
            # ATTENTION! Books indices finding!
            indices = [] # book=|0|, book2=|1|
            for i in range(0, len(books_collection)):
                if books_collection[i] == book or books_collection[i] == book2:
                    indices.append(i)
            # ATTENTION! SWAP!
            books_collection[indices[0]], books_collection[indices[1]]\
                = books_collection[indices[1]], books_collection[indices[0]]
        elif 'Insert Book' in operation:
            books_collection.append(book)
        elif command_line[0] == 'Check Book' and int(command_line[1]) < len(books_collection):
            check_book = books_collection[int(book)]
print(f'{check_book}\n{", ".join(books_collection)}')