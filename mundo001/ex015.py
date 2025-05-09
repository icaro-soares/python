#Perguntar qnts dias o carro foi alugado, qnts km rodados
#Cobrar R$60,00/dia e R$0,15/km rodado
dias = int(input('O carro foi alugado por quantos dias? '))
km_rodados = int(input('Quantos km foram rodados com o carro? '))
print(f'O carro foi alugado por {dias} dias e rodou {km_rodados}km.')

preco_dia = dias*60
preco_km = km_rodados*0.15
valor_total = preco_dia + preco_km

print(f'O valor a ser pago pelo número de dias será de R${preco_dia:.2f}'.replace('.', ','))
print(f'O valor a ser pago pelos km rodados será de R${preco_km:.2f}'.replace('.', ','))
print(f'O valor total a ser pago será de R${valor_total:.2f}'.replace('.', ','))
