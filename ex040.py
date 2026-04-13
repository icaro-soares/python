n1 = float(input('AV1: '))
n2 = float(input('AV2: '))
média = (n1 + n2) / 2
print(f'Sua média foi {média:.2f}')
print('Aluno: ', end='')
if média < 5.0:
    print('REPROVADO')
elif 5 <= média < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
