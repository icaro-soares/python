from datetime import date
from time import sleep


ano = int(input('Digite um ano (0 p/ o ano atual): '))
if ano == 0:
    ano = date.today().year
print(f'Verificando se {ano} é bissexto...')
sleep(2)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')
