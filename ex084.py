temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 1:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar [S/N]? ')).strip()[0]
    if r in 'Nn':
        break
print(f'No total foram cadastradas {len(princ)}')
print(f'Maior peso de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Menor peso de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
