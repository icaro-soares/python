#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.


nome = str(input('Qual seu nome completo? ')).strip()
nome_separado = nome.split()
tam_nome = len(nome)
tam_primeiro_nome = len(nome_separado[0])

print(f'Seu nome em letras maiúsculas é {nome.upper()}\nE em letras minúsculas é {nome.lower()}')
print(f'Seu nome tem {tam_nome} letras ao todo')
print(f'O primeiro nome tem {tam_primeiro_nome}')