def number(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum+=x

    return sum == num

num = int(input())
if number(num) == True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")