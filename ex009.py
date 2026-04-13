n = int(input('Digite um número: '))
print(f'Mostrando a tabuada de {n}')
print('-'*40)
for c in range(0, 11):
    print(f'{c:2} x {n} = {c*n:3}')