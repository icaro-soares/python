#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Insira o 1º valor: '))
b = int(input('Insira o 2º valor: '))
c = int(input('Insira o 3º valor: '))

#verificando o menor
menor = a
if a > b < c:
    menor = b
if a > c < b:
    menor = c
print(f'O menor valor é {menor}')
#verificando o maior
maior = a
if a < b > c:
    maior = b
if b < c > a:
    maior = c
print(f'O maior valor é {maior}')