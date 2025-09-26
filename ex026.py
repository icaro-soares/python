#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite sua frase: ')).lower().strip()
qnt_letra_a = frase.count('a')
print(f'Sua frase tem {qnt_letra_a} letras "a"')
primeiro_a = frase.find('a')
print(f'A primeira letra "a" aparece em {primeiro_a}')
último_a = frase.rfind('a')
print(f'A última letra "a" aparece em {último_a}')