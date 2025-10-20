
soma_idade = 0
tot_pessoa = 0
mais_velho = 0
nome_velho = ''
menos_vinte = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input(f'Nome da {pessoa}ª pessoa: ')).strip()
    idade = int(input(f'Idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Sexo da {pessoa}ª pessoa: ')).strip()[0]
    if pessoa == 1 and sexo in 'Mm':
        nome_velho = nome
        mais_velho = idade
    else:
        if idade > mais_velho and sexo in 'Mm':
            nome_velho = nome
            mais_velho = idade
    if sexo in 'Ff' and idade < 20:
        menos_vinte+=1
    soma_idade += idade
    tot_pessoa+=1
media_idade = soma_idade/tot_pessoa
print('-'*10)
print(f'A média de idade é {media_idade:.0f}')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')
print(f'{menos_vinte} mulheres têm menos de vinte anos.')