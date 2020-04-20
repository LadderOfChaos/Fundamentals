lines = int(input())
volume = 255
for i in range(lines):
    water = int(input())

    if volume - water < 0:
        print("Insufficient capacity!")
    else:
        volume-= water


print(255-volume)

