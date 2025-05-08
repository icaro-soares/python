#Dolár = R$5.71
#dividido p/real multiplicar p/ dolar

real = float(input('Quanto você têm na carteira? R$'))
dolar = real/5.69
euro = real/6.44
iene = real/0.039
print(f'Você tem em dólares US${dolar:.2f}\nVocê tem em euros €{euro:.2f}\nVocê tem em ienes ¥{iene:.2f}')
