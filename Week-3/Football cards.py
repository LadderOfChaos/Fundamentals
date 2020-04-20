cards = input().split()

teama = [1] * 11
teamb = [1] * 11

for i in cards:
    tokens = i.split("-")
    team = tokens[0]
    player = int(tokens[1])
    if team == "A":
        teama[player - 1] = 0
    else:
        teamb[player - 1] = 0

team_a_count = 0
team_b_count = 0

for i in range(11):
    team_a_count += teama[i]
    team_b_count += teamb[i]
if team_a_count < 7 or team_b_count < 7:
    print(f"Team A - {team_a_count}; Team B - {team_b_count}")
    print("Game was terminated")

else:
    print(f"Team A - {team_a_count}; Team B - {team_b_count}")