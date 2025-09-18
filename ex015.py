#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_percorridos = float(input('Quantos km foram percorridos com o carro: '))
quantidade_dias = int(input('Quantos dias o carro foi alugado: '))
preço_dia = quantidade_dias*60
preço_km = km_percorridos*0.15
preço_total = preço_dia+preço_km
print('Nota Fiscal')
print('-'*20)
print(f'Dias alugado: {quantidade_dias} dia(s)\nValor por dia alugado: R${preço_dia:.2f}')
print(f'Quilômetros percorridos: {km_percorridos:.2f}km\nValor por quilômetro: R${preço_km:.2f}')
print(f'Valor total a ser pago: R${preço_total:.2f}')