def validation(dictionary,key, def_value = 0):
    if key not in dictionary:
        my_dict[key] = def_value
text = input()
my_dict = {}
for ch in text:
    if ch == " ":
        continue
    validation(my_dict, ch)
    my_dict[ch] += 1

for k,v in my_dict.items():
    print(f"{k} -> {v}")
