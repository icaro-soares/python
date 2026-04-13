from datetime import date


atual = date.today().year
nasc = int(input('Nascimento: '))
idade = atual - nasc
falta = 0
print(f'Você têm {idade} anos.')
if idade < 18:
    print('Com essa idade você NÃO PODE SE ALISTAR!')
    falta = 18 - idade
    print(f'Faltam {falta} anos')
elif 18 <= idade < 45:
    print('Com essa idade você DEVE SE ALISTAR!')
else:
    print('Com essa idade você DEVIA TER SE ALISTADO!')
    falta = idade - 18
    print(f'Já se passaram {falta} anos do alistamento')
