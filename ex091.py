from random import randint
from operator import itemgetter
from time import sleep


num = {
    'jogador1':randint(1, 6),
    'jogador2':randint(1, 6),
    'jogador3':randint(1, 6),
    'jogador4':randint(1, 6)
}
ranking = []
print('Sorteio de Números'.center(30))
print('-='*30)
for k, v in num.items():
    print(f'{k} tirou o número {v} no dado.')
    sleep(.5)
print('-='*30)
print('Ranking'.upper().center(30))
ranking = sorted(num.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v}')