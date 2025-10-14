import emoji
from time import sleep

print('Contagem Regressiva para ano novo'.upper().center(50))
print('='*54)
for cont in range(10, -1, -1):
    print(cont, end=' > ')
    sleep(.5)
print(f'feliz ano novo!!!! {emoji.emojize(':fogos_de_artifício:', language='pt')}'.upper())