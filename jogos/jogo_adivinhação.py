from random import randint


pontos = 1000
chances = 0
número_secreto = randint(0, 100)
print('ADIVINHANDO'.center(60))
print('-='*30)
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
    #Condição p/ ganhar
    if chute == número_secreto:
        print('Parabéns! Você acertou!')
        print(f'Pontuação final: {pontos}')
        break
    #Condição de pontuação
    elif chute != número_secreto:
        chances-=1
        if chute > número_secreto:
            print('Errou! Tente um número menor')
            pontos-=chute
            print(f'Pontuação atual: {pontos}')
        elif chute < número_secreto:
            print('Errou! Tente um número maior')
            pontos-=chute
            print(f'Pontuação atual: {pontos}')
        if chances == 0:
            print(f'Suas chances acabaram! O número secreto era {número_secreto}')
            pontos = 0
            print(f'Pontuação final: {pontos}')
    #Condição para perder sem pontos
    elif pontos <= 0:
        print(f'Pontuação final: {pontos}')
        print('Seus pontos chegaram a zero, que pena, você perdeu.')
        print(f'O número secreto era {número_secreto}')
        break


