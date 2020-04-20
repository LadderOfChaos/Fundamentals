past_letter = ""
for i in input():
    if len(past_letter) == 0:
        past_letter = i
    else:
        if i != past_letter[-1]:
            past_letter += i
print(past_letter)