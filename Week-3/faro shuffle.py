# list=[1,2,3,4,5,6,7,8,]
# print(len(list))

cards = input()
shuffle = int(input())
cards_list = cards.split()
lenght = len(cards_list)
mid = int(lenght / 2)
final_list =[]
for i in range(mid+1):
    final_list.append(cards_list[i])
    final_list.append(cards_list[mid+i-1])

print(final_list)