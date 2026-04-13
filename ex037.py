n = int(input('Digite um número: '))
opc = int(input('Selecione uma opção: [1 - binário][2 - octal]'
'[3 - hexadecimal]: '))
if opc == 1:
    print(bin(n))
elif opc == 2:
    print(oct(n))
elif opc == 3:
    print(hex(n))
else:
    print('Opção inválida!')
