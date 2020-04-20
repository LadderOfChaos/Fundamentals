import re
pattern = r"\b(_)([a-zA-Z0-9]+\b)"
text = input()
matches = re.findall(pattern, text)
list = []
for match in matches:
    list.append(match[1])

print(",".join(list))