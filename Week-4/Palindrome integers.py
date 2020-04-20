def is_palindrome(num_str):
    reversed_num = num_str[::-1]

    return True if num_str == reversed_num else False

def is_palindrome_two(num_str):
    lenght = len(num_str)
    is_palindrome = True

    for i in range(lenght // 2):
        if num_str[i] != num_str[lenght -1 - i]:
            is_palindrome = False
            break

    return is_palindrome

text = input().split(", ")
for i in text:
    print(is_palindrome_two(i))