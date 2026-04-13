km = float(input('KM rodados: '))
dias = int(input('Dias alugado: '))
preço_dias = dias * 60
preço_km = km * 0.15
tot = preço_dias + preço_km
print(f'Valor dia: R${preço_dias:.2f}\nValor KM: R${preço_km:.2f}\nValor total: R${tot:.2f}')
