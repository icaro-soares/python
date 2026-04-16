from random import randrange


itens = ('Pedra', 'Papel', 'Tesoura')
j1 = int(input('''Faça sua jogada:
               [0 - Pedra]
               [1 - Papel]
               [2 - Tesoura]: '''))
comp = randrange(0, 3)
print('-=' * 30)
print(f'J1 jogou {itens[j1]}')
print(f'CPU jogou {itens[comp]}')
print('-=' * 30)
if itens[j1] == 'Pedra':
    if itens[comp] == 'Pedra':
        print('Deu empate!')
    elif itens[comp] == 'Papel':
        print('Você perdeu')
    elif itens[comp] == 'Tesoura':
        print('Você ganhou!')
elif itens[j1] == 'Papel':
    if itens[comp] == 'Pedra':
        print('Você ganhou!')
    elif itens[comp] == 'Papel':
        print('Deu empate!')
    elif itens[comp] == 'Tesoura':
        print('Você perdeu!')
elif itens[j1] == 'Tesoura':
    if itens[comp] == 'Pedra':
        print('Você perdeu!')
    elif itens[comp] == 'Papel':
        print('Você ganhou!')
    elif itens[comp] == 'Tesoura':
        print('Deu empate!')
