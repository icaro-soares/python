casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual seu salário: R$'))
anos = int(input('Em quantos anos vai pagar: '))
print('-='*30)
mínimo = sal * 0.30
prest = casa / (anos * 12)
print(f'30% do seu salário é R${mínimo:.2f} e a prestação R${prest:.2f}')
if prest > mínimo:
    print('Empréstimo negado!')
else:
    print('Empréstimo Aprovado')
