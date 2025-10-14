n = int(input('Digite um valor para ver sua tabuada: '))
print(f'Tabuada de {n}'.center(20))
print('='*20)
for cont in range(0, 11):
    print(f'{cont:3} x {n} = {cont*n:3}')