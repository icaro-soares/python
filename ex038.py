n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
n3 = int(input('3º valor: '))
maior = 0
if n1 == n2 == n3:
    print('Os valores são iguais!')
else:
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n2 and n3 > n1:
        maior = n3
    print(f'O maior valor é {maior}')
