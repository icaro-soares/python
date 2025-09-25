#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome_completo = str(input('Digite seu nome completo: ')).title().strip()
print(f'Muito prazer {nome_completo}')
nome_silva = 'Silva' in nome_completo
print(nome_silva)