n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
maior = menor = n1
# verificando quem é o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
# verificando quem é o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
