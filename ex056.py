#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
maior = 0
idade_h_velho = 0
nome_h_velho = ''
mulher_vinte = 0
print('Verificador de Pessoas'.center(30))
for p in range(1, 5):
    print('='*32)
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()[0]
    soma_idade += idade
    if idade > maior:
        maior = idade
    if sexo == 'M' and idade > idade_h_velho:
        idade_h_velho = idade
        if sexo == 'M' and idade_h_velho:
            nome_h_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_vinte += 1
media_idade = soma_idade/4
print(f'A média de idade do grupo é: {media_idade:.0f}')
print(f'O homem mais velho tem {idade_h_velho} anos e se chama {nome_h_velho}')
print(f'Mulheres comm menos de vinte anos: {mulher_vinte}')