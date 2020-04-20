days = int(input())
plunder = int(input())
expected_plunder = float(input())
current_plunder = 0
for i in range(1,days+1):
    if True:
        current_plunder += plunder
        if i % 3 == 0:
            current_plunder += (0.5 * plunder)
            if i % 5 == 0:
                current_plunder -= (0.3 * current_plunder)
        elif i % 5 == 0:
            current_plunder -= (0.3 * current_plunder)


if current_plunder < expected_plunder:
    percentage = (current_plunder/expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
elif current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")