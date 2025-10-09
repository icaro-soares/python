#Faça um programa que calcule a soma entre todos os números que são múltiplos de três que se encontram no intervalo de 1 até 500.
print('Múltiplos de 3 no intervalo entre 1 e 500:')
soma = 0
for n in range(1, 501):
    if n%3==0:
        print(n, end=' ')
        soma += n
print(f'\nA soma entre os números múltiplos de 3 entre 1 e 500 é: {soma}')