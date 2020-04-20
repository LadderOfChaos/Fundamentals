two_strings = input().split()
one = two_strings[0]
two = two_strings[1]

min_len = min(len(one), len(two))
total_sum = 0
for i in range(min_len):
    total_sum += ord(one[i]) * ord(two[i])
long_word = ""
short_word = ""
if len(one) > len(two):
    long_word= one
    short_word = two
else:
    long_word = two
    short_word = one

for i in range(min_len,len(long_word)):
    total_sum += ord(long_word[i])


print(total_sum)