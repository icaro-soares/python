frase = str(input('Digite uma frase: ')).strip().lower()
frase_unica = ''.join(frase.split())
print(frase_unica)
frase_invertida = (frase_unica[::-1])
print(frase_invertida)
if frase_unica == frase_invertida:
    print('A frase acima é um palíndromo!')
else:
    print('A frase acima não é um palíndromo!')