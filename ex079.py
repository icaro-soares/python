lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Sua lista: {lista}')