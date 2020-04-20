import re
s = input()
pattern = r"( |^)[a-z0-9]+([\_\-.]+[a-z0-9]+)*@[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
output = re.finditer(pattern, s)

for match in output:
    email = match[0].strip()
    print(email)
