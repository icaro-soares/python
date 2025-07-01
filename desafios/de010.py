#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e converta para dólares


dolar = 5.43
reais = float(input('Quanto você tem na carteira? R$'))
#Conversão  REAL PARA DÓLAR divide valor em REAL pela cotação do DÓLAR
valor_convertido = reais/dolar
print(f'Com R${reais:.2f}, posso comprar US${valor_convertido:.2f}')
