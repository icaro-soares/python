#Crie um algoritmo que leia o preço de um produto e mostre seu preço com 5% de desconto


preco = float(input('Digite o valor do produto: R$'))
novo_preco = preco - (preco * 0.05)
print(f'O valor do produto é R${preco:.2f}.\nCom desconto o valor ficará R${novo_preco:.2f}')
