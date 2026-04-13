frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count('a')} vezes na frase.')
print(f'A primeira letra "a" apareceu no posição {frase.find('a')}.')
print(f'A última letra "a" apareceu na posição {frase.rfind('a')}.')
