#Crie um programa que leia um ângulo qualquer e diga seu seno, cosseno e tangente
from math import sin, cos, tan, radians


angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno, cosseno e tangente de {angulo} vale: \n{seno}\n{tangente}\n{cosseno}')