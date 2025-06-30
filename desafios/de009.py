#Crie um programa que leia um número inteiro e mostre sua tabuada
cont = 0
n = int(input('Digite um número inteiro: '))
print(f'Tabuada de {n}')
print('-'*20)
while (cont <= 10):
    print(f'{n} x {cont} = {n*cont}')
    cont+=1
