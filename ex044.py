'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('lojas soares & cia.'.upper().center(40))
print('='*40)
preço = float(input('Qual o valor do produto: R$'))
opção = int(input('[1 - À vista dinheiro/cheque desconto 10%][2 - À vista cartão desconto 5%][3 - Até 2x cartão preço normal][4 - Cartão 3x ou mais com juros de 20%]: '))
if opção == 1:
    print('Você pagará à vista')
    novo_preço = preço - (preço*0.10)
    print(f'Preço com desconto de 10%: R${novo_preço:.2f}')
elif opção == 2:
    print('Você pagará à vista no cartão e terá desconto de 5%')
    novo_preço = preço - (preço*0.05)
    print(f'Preço com desconto de 5%: R${novo_preço:.2f}')
elif opção == 3:
    print('Você pagará no cartão em até 2x sem desconto')
    parcelas = int(input('Quantas vezes (até 2x? '))
    valor_parcelas = preço/parcelas
    print(f'Cada parcela ficará no valor de R${valor_parcelas:.2f}')
elif opção == 4:
    print('Você pagará no cartão em 3x ou mais com juros de 20%')
    novo_preço = preço + (preço*0.20)
    parcelas = int(input('Quantas vezes (3x ou mais)? '))
    valor_parcelas = novo_preço/parcelas
    print(f'Cada parcela ficará no valor de R${valor_parcelas:.2f}')
else:
    print('Algo deu errado, por favor tente novamente.')
