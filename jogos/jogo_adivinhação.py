from random import randint
chances = 0
número_secreto = randint(0, 100)
dificuldade = int(input('Escolha a dificuldade [1 - Fácil][2 - Médio][3 - Difícil]: '))
match dificuldade:
    case 1:
        print('Facil: 20 chances')
        chances = 20
    case 2:
        print('Médio: 10 chances')
        chances = 10
    case 3:
        print('Difícil: 5 chances')
        chances = 5
while chances > 0:
    chute = int(input('Tente adivinhar o número secreto: '))
    if chute == número_secreto:
        print('Parabéns! Você acertou!')
        break
    elif chute != número_secreto:
        chances-=1
        if chute > número_secreto:
            print('Errou! Tente um número menor')
        elif chute < número_secreto:
            print('Errou! Tente um número maior')
        if chances == 0:
            print(f'Suas chances acabaram! O número secreto era {número_secreto}')
