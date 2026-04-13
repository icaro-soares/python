#1 dólar = R$5.10
#1 euro = R$5.96
dinheiro_reais = float(input('Quanto dinheiro você tem na carteira: R$'))
dinheiro_dólar = dinheiro_reais/5.10
dinheiro_euro = dinheiro_reais/5.96
print(f'Valor convertido em dólares: US${dinheiro_dólar:.2f}')
print(f'Valor convertido em euro: €{dinheiro_euro:.2f}')
