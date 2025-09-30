#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = int(input('Qual a medida do 1º lado (cm): '))
r2 = int(input('Qual a medida do 2º lado (cm): '))
r3 = int(input('Qual a medida do 3º lado (cm): '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
    