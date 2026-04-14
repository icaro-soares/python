from random import randrange


# Escolha J1
j1 = int(input('Qual sua jogada: '))
if j1 == 1:
    print('Você jogou pedra')
elif j1 == 2:
    print('Você jogou papel')
elif j1 == 3:
    print('Você jogou tesoura')
else:
    print('Jogada inválida!')
# Escolha CPU
cpu = randrange(0, 3)