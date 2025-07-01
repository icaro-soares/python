#Crie um programa que leia quanto de dinheiro você tem na carteira e converta para dólares


carteira = float(input('Quanto você têm na sua carteira: R$'))
dolar = 5.46
valor_convertido = carteira/dolar
print(f'Você tem R${carteira:.2f}\nVocê pode comprar US${valor_convertido:.2f}')