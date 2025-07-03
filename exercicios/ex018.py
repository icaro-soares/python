#Crie um programa que leia um ângulo qualquer e diga seu seno, cosseno e tangente
from math import sin, cos, tan, radians


angulo = int(input('Digite um ângulo qualquer: '))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)
print(f'O seno de {angulo}° é {seno:.2f}\nO cosseno de {angulo}° é {cosseno:.2f}\nA tangente de {angulo}° é {tangente:.2f}')