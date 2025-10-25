pessoas_cadastradas = mais_dezoito = homem_cadastrado = menos_vinte = 0
while True:
    print('='*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas_cadastradas+=1
    if idade > 18:
        mais_dezoito+=1
    if sexo == 'M':
        homem_cadastrado+=1
    if sexo == 'F' and idade < 20:
        menos_vinte+=1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'S': continue
    else: break
print('='*20)
print(f'Foram cadastradas {pessoas_cadastradas}.\n{mais_dezoito} pessoas tem mais de 18 anos.')
print(f'{homem_cadastrado} homens foram cadastrados.\n{menos_vinte} mulheres tem menos de 20 anos.')
