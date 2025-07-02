#Crie um programa que leia os catetos de um triangulo retangulo e calculr sua hipotenusa
from math import hypot, radians


cateto_oposto = int(input('Digite a medida do cateto oposto: '))
cateto_oposto_radianos = radians(cateto_oposto)
cateto_adjacente = int(input('Digite a medida do cateto adjacente: '))
cateto_adjacente_radianos = radians(cateto_adjacente)
hipotenusa = hypot(cateto_adjacente_radianos, cateto_adjacente_radianos)
print(f'A hipotenusa do triangulo retangulo é {hipotenusa}')
