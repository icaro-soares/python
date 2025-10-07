#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
import emoji
from time import sleep

print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
itens = (emoji.emojize(':punho_levantado:', language='pt'), emoji.emojize(':dorso_da_mão_levantado:', language='pt'), emoji.emojize(':mão_em_v_de_vitória:', language='pt'))
computador = randint(0, 2)
jogador = int(input('Faça sua jogada: '))
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PÔ!!!')
print('='*11)
print(f'Jogador escolheu {itens[jogador]}')
print(f'Computador escolheu {itens[computador]}')
print('='*11)

if computador == 0: #computador joga pedra
    if jogador == 0: #jogador joga pedra
        print('Empatou!')
    elif jogador == 1: #jogador joga papel
        print('Jogador vence!')
    elif jogador == 2: #jogador joga tesoura
        print('Computador vence!')
elif computador == 1: #computador joga papel
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador vence!')
elif computador == 2: #computador joga tesoura
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empatou!')
