import team_manager
import interactions
import time
import math
print("Hello, welcome to the hockey game!")

player_1_turn = True
teams = team_manager.GetAllTeamNames("Teams.txt")
def HandleCommands(team_data):
    global teams
    if team_data[0] == "/":
        if team_data[-6:] == "create":
            team_data = team_manager.CreateTeam()
            teams.append(team_data)
        elif "sort wins" in team_data:
            team_manager.sortWins(int(team_data[team_data.rfind(' ') + 1:]))
        elif "sort conceded" in team_data:
            team_manager.sortConceded(int(team_data[team_data.rfind(' ') + 1:]))
    return team_data

if len(teams) >= 2:
    print("These are the following teams available: ")
    for team in teams:
        print(f"    => {team}")
    team_1 = input("Player 1, please select a team: ")
    team_1 = HandleCommands(team_1)

    while team_1 not in teams:
        print("Team not found. Please select a valid team.")
        team_1 = input("Player 1, please select a team: ")
        team_1 = HandleCommands(team_1)
    print("Player 2, please a DIFFERENT team to player 1: ")
    team_2 = input("Player 2, please select a team: ")
    team_2 = HandleCommands(team_2)
    while team_2 not in teams or team_2 == team_1:
        print("Team not found. Please select a valid DIFFERENT team.")
        team_2 = input("Player 2, please select a team: ")
        team_2 = HandleCommands(team_2)
    if isinstance(team_1, str):
        team_1 = team_manager.GetTeamDataFromName(team_1)
    if isinstance(team_2, str):
        team_2 = team_manager.GetTeamDataFromName(team_2)
else:
    print("Player 1, please create a team: ")
    team_1 = team_manager.CreateTeam()
    print("\n Player 2, please create a team: ")
    team_2 = team_manager.CreateTeam()
    
old_team_1 = team_1.copy()
old_team_2 = team_2.copy()
team_1_defender, team_1 = interactions.get_defender(team_1)
team_2_defender, team_2 = interactions.get_defender(team_2)

print(f"Player 1. Your chosen defender was player {team_1_defender[0]}")
time.sleep(0.2)
print(f"Player 2. Your chosen defender was player {team_2_defender[0]}")

def main():
    global player_1_turn, team_1, team_2
    for i in range(1, 11):
        time.sleep(0.5)
        if player_1_turn:
            print("\nPlayer 1's turn")
            attacker = team_1[math.ceil(i / 2)]
            print(f"Player {attacker[0]} is attacking against Player 2's defender")
            interactions.turn(attacker, team_2_defender, player_1_turn)
        else:
            print("\nPlayer 2's turn")
            attacker = team_2[int(i / 2)]
            print(f"Player {attacker[0]} is attacking against Player 1's defender")
            interactions.turn(attacker, team_1_defender, player_1_turn)
        player_1_turn =  not player_1_turn
    p1Score, p2Score, p1Goals, p1Conceded, p2Goals, p2Conceded = interactions.returnScores()
    old_team_1[-2] += (p1Goals)
    old_team_1[-1] += (p1Conceded)
    old_team_2[-2] += (p2Goals)
    old_team_2[-1] += (p2Conceded)


    team_manager.updateTeams(old_team_1, old_team_2)

    if p1Score != p2Score:
        print(f"{"Player 1" if p1Score > p2Score else "Player 2"} won with {p1Score if p1Score > p2Score else p2Score} score!!!!!")
    else:
        print("TIED")

    

if __name__ == "__main__":
    main()