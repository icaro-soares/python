lista = []
for c in range(0, 5):
    n = int(input(f'{c+1}º valor: '))
    lista.append(n)
print(f'Sua lista de valores: {lista}')
print(f'Menor valor da lista: {min(lista)}\nPosição do menor valor: {lista.index(min(lista))}')
print(f'Maior valor da lista: {max(lista)}\nPosição do maior valor: {lista.index(max(lista))}')
