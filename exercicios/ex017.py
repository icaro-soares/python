#Crie um programa que leia os catetos de um triangulo retangulo e calcule sua hipotenusa
from math import hypot


oposto = float(input('Digite um ângulo: '))
adjacente = float(input('Digite um ângulo: '))
hipotenusa = hypot(oposto, adjacente)
print(f'A hipotenusa calculada foi: {hipotenusa}')