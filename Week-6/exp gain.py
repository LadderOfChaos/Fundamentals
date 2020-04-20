exp_needed = float(input())
battles_count = int(input())
current_exp = 0
for battle in range(1,battles_count+1):
    exp_battle = float(input())
    current_exp+=exp_battle
    if current_exp >= exp_needed:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

    elif battle % 3 == 0:
        current_exp += (0.15 * exp_battle)
        if battle % 5 == 0:

            current_exp -=(0.10 * exp_battle)
    elif battle % 5 == 0:
        current_exp -=(0.1 * exp_battle)


if exp_needed > current_exp:
    remainining_exp = exp_needed - current_exp
    print(f"Player was not able to collect the needed experience, {remainining_exp:.2f} more needed.")