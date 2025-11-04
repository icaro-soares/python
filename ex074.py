from random import randint
números = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0,10), 
           randint(0, 10))
print('Números sorteados'.center(40))
print('='*40)
for número in números:
    print(f'{número}', end=' ')
print(f'\nMaior número da tupla: {max(números)}')
print(f'Menor número da tupla: {min(números)}')
