num = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print('Valores digitados: '.center(40))
print('='*40)
for n in num:
    print(n, end=' ')
#Número de vezes que o valor 9 aparece
print(f'\nO número 9 apareceu: {num.count(9)} vezes')
#Que posição apareceu o número 3
if 3 in num:
    print(f'O número 3 apareceu na posição: {num.index(3)}')
else:
    print('O número 3 não está na lista')
#Números pares
print('Lista dos pares: ', end='')
for n in num:
    if n%2==0:
        print(n, end=' ')
