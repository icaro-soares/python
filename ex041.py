from datetime import date


nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
print(f'Sua idade é {idade} anos, você se encaixa na categoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
