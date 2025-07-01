#Escreva um programa que leia a quantidade de km rodados e a quantidade de dias que ele foi alugado calcule o preço a pagar sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado


km_rodados = float(input('Digite a quantidade de km rodados pelo carro: '))
qnt_dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco_dia = qnt_dias*60.00
preco_km = km_rodados*0.15
preco_total = preco_dia+preco_km
print(f'O valor total a se pagar pelo carro será de R${preco_total:.2f}')
