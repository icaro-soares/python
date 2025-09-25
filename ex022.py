#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input('Nome: ')).strip()
print(f'Seu nome é {nome}, prazer em te conhecer!')
nome_maiusculas = nome.upper()
print(f'Seu nome em MAIÚSCULAS: {nome_maiusculas}')
nome_minusculas = nome.lower()
print(f'Nome em minúsculas {nome_minusculas}: ')
nome_tamanho = len(nome)
print(f'Seu nome têm {nome_tamanho} letras')
nome_separado = nome.split()
letras_primeiro = len(nome_separado[0])
print(f'Seu primeiro nome têm {letras_primeiro} letras')
