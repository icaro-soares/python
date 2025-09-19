from math import hypot
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa têm: {hipotenusa:.2f}cm²')
