from math import sqrt


#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número qualquer: '))
dobro = n*2
triplo = n*3
raiz = sqrt(n)
print(f'O número digitado foi {n}')
print(f'Seu dobro é {dobro}\nO triplo é {triplo}\nA raiz quadrada é {raiz:.2f}')
