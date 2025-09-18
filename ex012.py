#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o valor do produto: R$'))
desconto = 5/100 * preço
novo_preço = preço - desconto
print(f'Seu produto de valor R${preço:.2f}, vai ficar por R${novo_preço:.2f}')
