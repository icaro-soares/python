#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu [0 ou menos p/ o ano atual]? '))
idade = ano_atual - ano_nascimento
if idade == 18:
    print(f'Você têm {idade} anos, já pode se alistar')
elif idade < 18:
    print(f'Você têm {idade} anos, ainda não pode se alistar')
else:
    print(f'Você têm {idade} anos, já passou do tempo de se alistar')
