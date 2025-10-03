#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Valor da casa: R$'))
sal_comprador = float(input('Salário: R$'))
anos_pagar = int(input('Em quantos anos pretende pagar? '))
meses_pagar = anos_pagar * 12 #converte anos em meses
prestação_mensal = valor_casa/meses_pagar #valor da prestação por mês
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_pagar} anos, a prestação mesal será de R${prestação_mensal:.2f}')
trinta_porcento = sal_comprador * 30/100
if prestação_mensal > trinta_porcento:
    print(f'Empréstimo negado!')
else:
    print(f'Empréstimo aprovado!')