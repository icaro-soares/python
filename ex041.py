'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Que ano você nasceu? '))
idade = ano_atual - ano_nasc
print(f'Idade: {idade} anos')
if idade <= 9:
    print('Você se encaixa na categoria MIRIM')
elif idade <= 14:
    print('Você se encaixa na categoria INFANTIL')
elif idade <= 19:
    print('Você se encaixa na categoria JÚNIOR')
elif idade <= 25:
    print('Você se encaixa na categoria SÊNIOR')
else:
    print('Você se encaixa na categoria MASTER')