#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
from random import randint


aleatório = randint(0, 5)
print('Pensei em um número entre 0 e 5, tente adivinhá-lo!')
chute = int(input('Seu palpite: '))
if chute == aleatório:
    print('Parabéns! Você acertou o número que pensei!')
else:
    print(f'Que pena! O número que pensei foi {aleatório}')
