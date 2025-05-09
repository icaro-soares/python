#Ler o preço de um produto e mostrar o preço com 5% de desconto
print('Bem-vindo(a) a loja Fechando as Portas!')
produto = float(input('Qual o valor do produto? R$'))
print(f'O valor total a se pagar é R${produto:.2f}'.replace('.', ','))
desconto = (0.05*produto)
valor_final = produto - desconto
print(f'Com desconto de 5% o valor final do seu produto é de R${valor_final:.2f}'.replace('.', ','))
