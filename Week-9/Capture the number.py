import re
txt = input()
pattern = r"\d+"
while True:
    if not txt:
        break

    result = re.findall(pattern, txt)
    for num in result:
        print(num, end=" ")

    txt = input()