# Note - I decided to play with this a little more to force a winner so the current implementation is best of 3 ignoring any ties.
import random

gesture = ["rock", "paper", "scissors"]
results = ["Tie", "CPU won", "Player won"]
n_rounds = 3
rounds_to_win = (n_rounds + 1) / 2
cpu_score = 0
player_score = 0
result = 0


# function to pick a random choice for the CPU
def randompick():
    rand = random.randrange(0, 3)
    return gesture[rand]


# function for the player to pick a choice
def playerpick():
    pick = ""
    while (pick != "rock") & (pick != "paper") & (pick != "scissors"):
        pick = input("Choose wisely, rock, paper or scissors")
        pick = pick.lower()
    return pick


# function to work out who won
def whowon(cpu, player):
    # function to convert string to int value
    def numericpick(choice):
        if choice == "rock":
            return 0
        elif choice == "paper":
            return 1
        else:
            return 2

    winner = (numericpick(cpu) - numericpick(player)) % 3
    print(winner, numericpick(cpu), numericpick(player))
    return winner


# function to show the results of the round
def roundresult(cpu, player, winner, cpu_score, player_score):
    print(cpu)
    print(player)
    print(results[winner])
    if results[winner] == "CPU won":
        cpu_score += 1
    if results[winner] == "Player won":
        player_score += 1
    return cpu_score, player_score


while max(cpu_score, player_score) < rounds_to_win:
    cpu = randompick()
    player = playerpick()
    winner = whowon(cpu, player)
    cpu_score, player_score = roundresult(cpu, player, winner, cpu_score, player_score)

if cpu_score == rounds_to_win:
    print("Computer Says No")
else:
    print("Get back in your box Ava")
