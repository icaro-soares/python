valor_total = mais_mil = barato = cont = 0
nome_barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Valor do produto: R$'))
    valor_total+=preço
    if preço > 1000:
        mais_mil+=1
    cont+=1
    if cont == 1 or preço < barato:
        barato = preço
        nome_barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total de compras é R${valor_total:.2f}')
print(f'{mais_mil} produto(s) custa(m) mais de R$1000,00')
print(f'O produto mais barato foi {nome_barato} custando R${barato:.2f}')