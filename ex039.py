#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nasc = int(input('Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Idade: {idade} anos')
if idade <= 17:
    print('Você ainda tem que esperar para se alistar no exécito')
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Está na hora de se alistar no exército')
else:
    print('Já passou do tempo do alistamento militar')
    saldo = idade - 18
    print(f'Já se passaram {saldo} anos do alistamento')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}')