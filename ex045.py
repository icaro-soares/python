#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
j1 = int(input('Escolha sua jogada\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura: '))
if j1 == 0:
    j1 = 'Pedra'
elif j1 == 2:
    j1 ='Papel'
else: 
    j1 = 'Tesoura'
cpu = randint(0, 2)
if cpu == 0:
    cpu = 'Pedra'
elif cpu == 1:
    cpu = 'Papel'
else:
    cpu = 'Tesoura'
print(f'O jogador escolheu {j1}')
print(f'A cpu escolheu {cpu}')
#empate
if j1 == cpu:
    print('Empatou'.upper())
#j1 vence
if j1 == 'Pedra' and cpu == 'Tesoura':
    print('O jogador 1 venceu!')
elif j1 == 'Papel' and cpu == 'Pedra':
    print('O jogador 1 venceu!')
elif j1 == 'Tesoura' and cpu == 'Papel':
    print('O jogador 1 venceu!')
#cpu vence
if cpu == 'Pedra' and j1 == 'Tesoura':
    print('A cpu venceu!')
elif cpu == 'Papel' and j1 =='Pedra':
    print('A cpu venceu!')
elif cpu == 'Tesoura' and j1 == 'Papel':
    print('A cpu venceu!')