from random import randint
from time import sleep

gestures = ["rock", "paper", "scissors"]
results = ["Tie", "CPU win", "Player win"]
n_rounds = 3

#4. Crie uma variável chamada rounds_to_win para armazenar o número de rodadas que um jogador deve vencer para vencer o jogo. ¶
#Dica : o valor armazenado em rounds_to_win depende do valor de n_rounds.

rounds_to_win = (n_rounds+1)/2

#5. Crie duas variáveis ​​para armazenar o número de rodadas que o computador e o jogador ganharam. 
# Chamar essas variáveis 

cpu_score = 0
player_score = 0

#6. Defina uma função que retorne aleatoriamente uma das 3 opções de gestos. 
#Você usará esta função para simular a escolha do gesto do computador.

def cpuoption():
    i = randint(0,2)
    return gestures[i]


#7. Defina uma função que pergunte ao jogador qual é o gesto que quer mostrar: 'pedra', 'papel' ou 'tesoura'. ¶
#O jogador deve ter permissão para escolher apenas uma das 3 opções de gestos. 
#Se a escolha do jogador não for pedra, papel ou tesoura, pergunte até que seja.

def playeroption():
    move = ""
    move = input('''
==============
What's your move? 
Type option.
rock
paper
scissor...
==============
''')
    move = move.lower()
    return move

def earner(cpu, player):
    def option(i):
        if i == "rock":
            return 0
        elif i == "paper":
            return 1
        else:
            return 2

    winner = (option(cpu) - option(player)) % 3
    return winner

def result(cpu, player, winner, cpu_score, player_score):
    print('rock')
    sleep(1)
    print ('paper')
    sleep(1)
    print ('scissor')
    sleep(1)
    print("-=" * 10)
    print(f"Cpu play {cpu}")
    print(f"Player play {player}")
    print("-" * 10)
    print(results[winner])
    print("-=" * 10)
    if results[winner] == "CPU win":
        cpu_score += 1
    if results[winner] == "Player win":
        player_score += 1
    return cpu_score, player_score


while max(cpu_score, player_score) < rounds_to_win:
    cpu = cpuoption()
    player = playeroption()
    winner = earner(cpu,player)
    cpu_score, player_score = result(cpu, player, winner, cpu_score, player_score)
    
if player_score == rounds_to_win:
    print(f"Congratulations you won, win {player_score} matches, against {cpu_score} losers")
else:
    print("Sorry try again")