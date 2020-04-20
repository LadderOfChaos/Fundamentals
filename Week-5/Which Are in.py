list1 = input().split(', ')
list2 = input().split(', ')
output = []
for string1 in list1:
    for string2 in list2:
        if string1 in string2 and string1 not in output:
             output.append(string1)
        else:
            continue
print(output)