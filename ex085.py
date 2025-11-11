num = [[], []]
for c in range(0, 7):
    n = int(input(f'{c+1}º valor: '))
    if n%2==0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Lista de pares: {sorted(num[0])}\nLista de ímpares: {sorted(num[1])}')
