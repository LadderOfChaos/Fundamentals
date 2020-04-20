def lala(a,b):
    a = ord(a)
    b = ord(b)
    for i in range(a+1, b):
        print(chr(i), end = " ")



a = input()
b = input()
lala(a,b)