#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal
n = int(input('Digite um inteiro qualquer: '))
escolha = int(input('Escolha o tipo de conversão [1 - binário] [2 - octal] [3 - hexadecimal]: '))
if escolha == 1:
    print(f'Número em BINÁRIO: {bin(n)[2:]}')
elif escolha == 2:
    print(f'Número em OCTAL: {oct(n)[2:]}')
elif escolha == 3:
    print(f'Número em HEXADECIMAL: {hex(n)[2:]}')
else:
    print('Escolha inválida, por favor, tente novamente')