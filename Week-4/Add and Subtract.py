def sum_numbers(a, b):
    return a + b


def subtract(first, second):
    return first - second


def add_and_sub(numone, numtwo, numthree):
    sum = sum_numbers(numone, numtwo)
    res = subtract(sum, numthree)
    print(res)


a = int(input())
b = int(input())
c = int(input())
add_and_sub(a,b,c)