frase = str(input('Digite uma frase: ')).strip().lower()
frase_invertida = (frase[::-1])
print(f'A sua frase invertida:\n{frase_invertida}')
if frase == frase_invertida:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')