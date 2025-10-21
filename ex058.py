from random import randint

cpu = randint(0, 10)
tentativa = 0
jogador = int(input('Qual seu palpite: '))
tentativa+=1
while jogador != cpu:
    if jogador > cpu:
        print('Menos... tente novamente!')
    elif jogador < cpu:
        print('Mais... tente novamente!')
    jogador = int(input('Qual seu palpite: '))
    tentativa+=1
if jogador == cpu:
    print(f'Você acertou em {tentativa} tentativas!')
