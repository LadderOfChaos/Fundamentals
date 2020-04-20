snowballs = int(input())
Value = -99999999
snow = 0
time = 0
quality = 0
for i in range(1,snowballs+1):

    snow2 = int(input())
    time2 = int(input())
    quality2 = int(input())
    current_value = (int(snow2 / time2)) ** quality2

    if Value < current_value:
        Value = current_value
        snow = snow2
        quality = quality2
        time = time2

print(f"{snow} : {time} = {Value} ({quality})")