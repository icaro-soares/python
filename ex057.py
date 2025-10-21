sexo = str(input('Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Dado inválido, por favor, digite novamente!')
    sexo = str(input('Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} informado')