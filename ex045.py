#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
import emoji

j1 = int(input('Escolha sua jogada\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura: '))
if j1 == 0:
    escolha_j1 = emoji.emojize(':curling_stone:')
elif j1 == 1:
    escolha_j1 = emoji.emojize(':newspaper:')
elif j1 == 2:
    escolha_j1 = emoji.emojize(':scissors:')

cpu = randint(0, 2)
if cpu == 0:
    escolha_cpu = emoji.emojize(':curling_stone:')
elif cpu == 1:
    escolha_cpu = emoji.emojize(':newspaper:')
elif cpu == 2:
    escolha_cpu = emoji.emojize(':scissors:')

print('='*20)
print(f'O jogador escolheu {escolha_j1}')
print(f'A cpu escolheu {escolha_cpu}')
print('='*20)

#empate
if j1 == cpu:
    print('Empatou'.upper())

#j1 vence
if j1 == 0 and cpu == 2:
    print('O jogador 1 venceu!')
elif j1 == 1 and cpu == 0:
    print('O jogador 1 venceu!')
elif j1 == 2 and cpu == 1:
    print('O jogador 1 venceu!')

#cpu vence
if cpu == 0 and j1 == 2:
    print('A cpu venceu!')
elif cpu == 1 and j1 == 0:
    print('A cpu venceu!')
elif cpu == 2 and j1 == 1:
    print('A cpu venceu!')