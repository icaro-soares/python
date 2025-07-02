#Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira
from math import trunc


n = float(input('Digite um valor: '))
print(f'A porção inteira de {n} é {trunc(n)}')