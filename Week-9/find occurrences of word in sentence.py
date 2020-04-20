import re

text = input()
txt = input()
pattern = fr"\b{txt}\b"
words_count = re.findall(pattern,text, re.IGNORECASE)
output = []
for match in words_count:
    output.append(match)

print(len(output))