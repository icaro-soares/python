lista = []
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        lista.append(c)
print(f'\nForam registrados {len(lista)} valores. E a soma vale: {sum(lista)}')
