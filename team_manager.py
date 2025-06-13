import ast
import fileinput
file = "Teams.txt"

# ["Team name", [player_num, Attack, Defense],[player_num, Attack, Defense],[player_num, Attack, Defense],[player_num, Attack, Defense],[player_num, Attack, Defense],[player_num, Attack, Defense],]
def CreateTeam():
    team_list = []
    teams = GetAllTeamNames(file)
    team_name = input("What will your team be called?: ")

    while team_name in teams:
        team_name = input("Team already exists. Please enter a different name: ")
    team_list.append(team_name)

    print("\nPlease print the attack and defense stats for each player in format attack,defense")
    print("The total attack AND defense stats for the team cannot be more than 35")
    print("Max attack is 10")
    print("Max defense is 7")
    total_stats = 0
    for i in range(1, 7):
        while True:
            player_input = input(f"Enter the stats for player {i}: ")
            try:
                attack_str, defense_str = player_input.split(',')
                attack = int(attack_str.strip())
                defense = int(defense_str.strip())
                if attack < 0 or attack > 10:
                    print(f"Player {i}'s attack stat is invalid: ")
                    attack = ""
                    while True:
                        attack = int(input(f"Please enter player {i}'s attack stat: "))
                        if attack < 10 and attack > 0 and str(attack) != "":
                            break
                if defense < 0 or defense > 7:
                    print(f"Player {i}'s defense stat is invalid: ")
                    defense = ""
                    while defense == "":
                        defense = int(input(f"Please enter player {i}'s defense stat: "))
                        if defense < 7 and defense > 0 and str(attack) != "":
                            break
                total_stats += defense + attack
                if (total_stats > 35):
                    user_input = input(
                        "Total stats of all team players is greater than 60, would you like to restart the team creation process? (y/n): ").lower()
                    if user_input == "yes":
                        CreateTeam()
                    else:
                        quit()
                team_list.append([i, attack, defense])
                print(f"total stats = {total_stats}")
                break
            except ValueError:
                print("Invalid input. Please enter values in the format: attack,defense (e.g. 3,4)")
    team_list.append(0)
    team_list.append(0)
    lines = GetLines(file)

    with open(file, "a+") as f:
        f.seek(0)
        content = f.read()
        if content and not content.endswith('\n'):
            f.write("\n")
        f.write(str(team_list) + "\n")

    return team_list

def PrintTeamValues():
    lines = 0
    with open(file, "r") as f:
        for line in f:
            lines += 1
            team = ast.literal_eval(line)
            print(f"Team: {team[0]}")
            for i in range(1,7):
                stats=team[i]
                print(f"    =>Player {i} has {stats[1]} attack and {stats[2]} defense")

def GetLines(file):
    with open(file, "r") as f:
        return len(f.readlines())

def GetAllTeamNames(file):
    teams_list = []
    with open(file, "r") as f:
        for line in f:
            team = ast.literal_eval(line)
            teams_list.append(team[0])
    return teams_list

def GetTeamDataFromName(name):
    with open(file, "r") as f:
        for line in f:
            team = ast.literal_eval(line)
            if team[0] == name:
                return team
    return ValueError(f"Team {name} could not be found")

def SortTeams(name):
    pass

import ast

def updateTeams(team1, team2, file_path='Teams.txt'):
    old_team_1 = str(team1[:-2])  # Without score data
    old_team_2 = str(team2[:-2])

    new_team_1 = str(team1)
    new_team_2 = str(team2)

    with open(file_path, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        original_line = line.strip()
        parsed_line = ast.literal_eval(original_line)
        line_without_scores = str(parsed_line[:-2])

        if line_without_scores == old_team_1:
            updated_lines.append(new_team_1 + '\n')
        elif line_without_scores == old_team_2:
            updated_lines.append(new_team_2 + '\n')
        else:
            updated_lines.append(original_line + '\n')  # Preserve untouched line

    with open(file_path, 'w') as f:
        f.writelines(updated_lines)

import ast

def sortWins(amount):
    all_wins = []
    
    with open(file, "r") as f:
        for line in f:
            line = ast.literal_eval(line.strip())
            wins = line[-2]  # Assuming this is the wins count (an int)
            name = line[0]
            all_wins.append([name, wins])
    
    # Sort all_wins by wins descending (most wins first)
    all_wins_sorted = sorted(all_wins, key=lambda x: x[1], reverse=True)
    
    # Take top `amount` teams
    top_teams = all_wins_sorted[:amount]
    
    # Print results with rank
    for i, (team, wins) in enumerate(top_teams, start=1):
        print(f"   {i}) Team {team} has {wins} wins")

def sortConceded(amount):
    all_conceded = []
    
    with open(file, "r") as f:
        for line in f:
            line = ast.literal_eval(line.strip())
            conceded = line[-1]
            name = line[0]
            all_conceded.append([name, conceded])
    
    # Sort all_wins by wins descending (most wins first)
    all_conceded_sorted = sorted(all_conceded, key=lambda x: x[1], reverse=True)
    
    # Take top `amount` teams
    top_teams = all_conceded_sorted[:amount]
    
    # Print results with rank
    for i, (team, conceded) in enumerate(top_teams, start=1):
        print(f"   {i}) Team {team} has conceded {conceded} goals")


if __name__ == "__main__":
    # updateTeams(['Pandas', [1, 10, 7], [2, 10, 7], [3, 1, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], 1, 2], ['Test', [1, 1, 2], [2, 1, 2], [3, 1, 2], [4, 1, 2], [5, 1, 2], [6, 1, 2], 2, 2])
    sortWins(3)