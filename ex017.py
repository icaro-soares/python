from math import sqrt, hypot, radians
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cateto_oposto = float(input('Cateto oposto do triângulo retangulo: '))
cateto_adjacente = float(input('Cateto adjacente do triângulo retângulo: '))
#soma do quadrado dos catetos é igual ao quadrado da hipotenusa
hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2)
