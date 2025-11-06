lista_n = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um valor: '))
    lista_n.append(num)
    if num%2==0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
print(f'Lista completa: {lista_n}')
print(f'Lista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')
