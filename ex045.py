#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
jogador = int(input('Jogada [1 - Pedra][2 - Papel][3 - Tesoura]: '))
cpu = randint(1, 3)
