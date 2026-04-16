n = int(input('Digite um número: '))
print('-' * 30)
print(f'Tabuada de {n}'.center(30))
print('-' * 30)
for c in range(1, 11):
    print(f'{c:2} x {n:3} = {n*c:3}'.center(30))
print('-' * 30)
