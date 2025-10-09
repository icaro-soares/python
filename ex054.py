#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
mais_18 = 0
menos_18 = 0
ano_atual = date.today().year
for pessoa in range(1, 8):
    ano_nasc = int(input('Em que ano você nasceu? '))
    idade = ano_atual - ano_nasc
    print(f'Idade da {pessoa}ª pessoa: {idade}')
    if idade < 18:
        menos_18 += 1
    elif idade >= 18:
        mais_18 += 1
print(f'Pessoas maiores de idade: {mais_18}\nPessoas menores de idade: {menos_18}')