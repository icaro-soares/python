#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
print('Contagem regressiva do revellion')
for cont in range(10, 0, -1):
    sleep(.5)
    print(cont)
print('FELIZ ANO NOVO!')