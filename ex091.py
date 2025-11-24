from random import randint


num = {}
print('Sorteio de Números'.center(30))
num['jogador1'] = randint(1, 6)
num['jogador2'] = randint(1, 6)
num['jogador3'] = randint(1, 6)
num['jogador4'] = randint(1, 6)
print('-='*30)
for k, v in num.items():
    print(f'{k} tirou o número {v} no dado.')
print('-='*30)
print('Ranking'.upper().center(30))
print('-='*30)
