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
    print('Jogada inválida, aplicação encerrada!')
    exit()

# Computador faz a jogada
comp = randrange(0, 3)
if comp == 0:
    print('O computador jogou pedra')
elif comp == 1:
    print('O computador jogou papel')
elif comp == 2:
    print('O computador jogou tesoura')
print('-='*30)

# Condições

# Pedra
if j1 == 0: 
    if comp == 0:
        print('Empatou!')
    elif comp == 1:
        print('O cpu venceu!')
    elif comp == 2:
        print('O jogador venceu!')
# Papel
elif j1 == 1:
    if comp == 0:
        print('O jogador venceu!')
    elif comp == 1:
        print('Empatou!')
    elif comp == 2:
        print('O cpu venceu!')
# Tesoura
elif j1 == 2:
    if comp == 0:
        print('O cpu venceu!')
    elif comp == 1:
        print('O jogador venceu!')
    elif comp == 2:
        print('Empate!')
