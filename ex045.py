from random import randrange


# Jogador 1 faz jogada
j1 = int(input('''Faça sua escolha
    [0 - Pedra]
    [1 - Papel]
    [2 - Tesoura]: '''))
print('-='*30)
if j1 == 0:
    print('Você jogou pedra')
elif j1 == 1:
    print('Você jogou papel')
elif j1 == 2:
    print('Você jogou tesoura')
else:
    print('Jogada inválida')

# Computador faz a jogada
comp = randrange(0, 3)
if comp == 0:
    print('O computador jogou pedra')
elif comp == 1:
    print('O computador jogou papel')
elif comp == 2:
    print('O computador jogou tesoura')
else:
    print('Jogada inválida')
