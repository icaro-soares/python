#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira (R$) e mostre quantos dólares ela pode comprar.
dinheiro = float(input('Quantos reais você tem na carteira: R$'))
dolar = 5.31
valor_convertido = dinheiro/dolar
print(f'Com esse valor em reais, você pode comprar US${valor_convertido:.2f} dólares'.replace('.', ','))
