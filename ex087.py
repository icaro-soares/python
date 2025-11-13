matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
soma_col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'a) Os valores pares é {sum(pares)}')
for l in range(0, 3):
    soma_col+=matriz[l][2]
print(f'b) A soma dos valores da 3ª coluna é {soma_col}')
for c in range(0, 3):
    if c == 1 or matriz[1][c]:
        maior = matriz[1][c]
print(f'c) O maior valor da 2ª linha é {maior}')