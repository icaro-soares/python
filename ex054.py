from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento a {c}ª pessoa? '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior+=1
    else:
        menor+=1
print(f'Pessoas maiores de idade: {maior}\nPessoas menores de idade: {menor}')