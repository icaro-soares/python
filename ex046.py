#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
import emoji
print('contagem regressiva para o revellion'.center(50).upper())
print('='*50)
for c in range(10, -1, -1):
    print(c, ' > ', end=' ')
print(f'feliz ano novo!!!{emoji.emojize(':fogos_de_artifício:', language='pt')}'.upper())