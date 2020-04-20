word = input()
counter = 0
for i in word:
    if i == ":":
        print(":"+ word[counter+1])
    counter+=1