from random import randint
from time import sleep


print('Pensei em um número, tente adivinhá-lo!')
cpu = randint(0, 5)
chute = int(input('Digite seu palpite: '))
print('Pensando...')
sleep(2)
if chute == cpu:
    print('Você acertou!')
else:
    print(f'Você errou, o número era {cpu}!')
