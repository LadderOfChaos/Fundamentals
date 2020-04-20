n = int(input())
sum = 0
for i in range (n):
    line = input()
    sum += ord(line)

print(f'The sum equals: {sum}')