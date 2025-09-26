#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Seu nome completo: ')).strip()
print(f'Prazer em te conhecer, {nome}')
nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()
print(f'Seu nome em letras maiúsculas: {nome_maiuscula}\nSeu nome em letras minúsculas: {nome_minuscula}')
nome_comprimento = len(nome)
espaços = nome.count(' ')
print(f'Seu nome sem espaços têm {nome_comprimento - espaços} letras')
nome_separado = nome.split()
print(f'O primeiro nome é composto por {len(nome_separado[0])} letras')