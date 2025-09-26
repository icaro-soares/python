#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome_completo = str(input('Seu nome completo: ')).title().strip()
print(f'Prazer em te conhecer, {nome_completo}!')
nome_separado = nome_completo.split()
print(f'Seu primeiro nome é {nome_separado[0]}')
print(f'Seu último nome é {nome_separado[-1]}')