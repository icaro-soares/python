from math import sin, cos, tan, radians
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
angulo = float(input('Ângulo usado para realizar o cálculo: '))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)
print(f'Seno, cosseno e tangente de {angulo}°')
print(f'Seno: {seno:.1f}\nCosseno: {cosseno:.1f}\nTangente: {tangente:.1f}')