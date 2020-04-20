numbers = input()
remove = int(input())

numbers_list = numbers.split()
for i in range(0, len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])



for _ in range(remove):
    numbers_list.remove(min(numbers_list))
print(numbers_list)