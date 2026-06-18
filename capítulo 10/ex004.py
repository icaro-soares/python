try:
    n1 = int(input('1º valor: '))
    n2 = int(input('2º valor: '))
except ValueError:
    print('Apenas números são aceitos!')
else:
    s = n1 + n2
    print(f'A soma vale {s}')
