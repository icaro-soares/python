tot = 0
while True:
    produto = str(input('Produto: ')).strip().upper()
    preço = float(input('Preço: '))
    tot+=preço
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar [S/N]: ')).strip()[0]
    if r in 'Nn':
        print(f'O valor total de suas compras foi R${tot:.2f}'.replace('.', ','))
        break