#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual seu nome completo: ')).strip().title()
print(f'Prazer em te conhecer {nome}!')
print(f'Tem "Silva" no nome: {"Silva" in nome}')