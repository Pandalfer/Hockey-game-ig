import random
import time

Player1Score = 0
Player2Score = 0
Player1Goals = 0
Player2Goals = 0
Player1Conceded = 0
Player2Conceded = 0
def interaction(attack, defense):
    chance = 0.5 + (attack - defense) * 0.1  # base 50%, ±10% per point difference
    chance = max(0.1, min(chance, 0.9))     # limit chance between 10% and 90%
    return random.random() < chance
    
def get_defender(team):
    defender = random.choice(team[1:-3])
    team.remove(defender)
    return defender, team

def turn(attacker, defender, isPlayer1):
    global Player1Score, Player2Score, Player1Goals, Player1Conceded, Player2Goals, Player2Conceded
    attack = int(attacker[1])
    defense = int(defender[2])
    successful = interaction(attack, defense)
    print(f"Attack", end=' ', flush=True) 
    time.sleep(2)
    print(f"{ "WAS" if successful else "WAS NOT"}", end=' ', flush=True)    
    if successful:
        Player1Score += 1 if isPlayer1 else 0
        Player2Score += 1 if not isPlayer1 else 0
        Player1Goals += 1 if isPlayer1 else 0
        Player2Goals += 1 if not isPlayer1 else 0
        Player1Conceded += 1 if not isPlayer1 else 0
        Player2Conceded += 1 if isPlayer1 else 0
    time.sleep(0.8)
    print("successful")

def returnScores():
    return Player1Score, Player2Score, Player1Goals, Player1Conceded, Player2Goals, Player2Conceded

if __name__ == "__main__":
    turn([2, 5, 7],  [1, 10, 7])