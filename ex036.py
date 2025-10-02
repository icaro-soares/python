#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos vai pagar? '))
print(f'A casa é R${valor_casa:.2f}'.replace('.', ','))
print(f'Seu salário é de R${salário:.2f}'.replace('.', ','))
meses = anos * 12
print(f'A casa será paga em {meses} meses')
prestação = valor_casa/meses
porcentagem_sal = 30/100*salário

if prestação > porcentagem_sal:
    print(f'A prestação fica em R${prestação:.2f}, lamento você não pode comprar a casa')
else:
    print(f'Você pode comprar a casa')