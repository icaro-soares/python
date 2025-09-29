#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado_a = int(input('Qual a medida do 1º lado (cm): '))
lado_b = int(input('Qual a medida do 2º lado (cm): '))
lado_c = int(input('Qual a medida do 3º lado (cm): '))
if lado_a + lado_b > lado_c or lado_b + lado_c > lado_a:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')