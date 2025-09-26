#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 


from random import randint


print('Pensei em um número! Tente adivinha-lo!')
numero_aleatorio = randint(0, 5)
chute = int(input('Seu palpite: '))
if chute == numero_aleatorio:
    print('Parabéns! Você acertou número que pensei!')
else:
    print(f'Você errou, que pena. O número era: {numero_aleatorio}')
