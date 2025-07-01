#Leia o preço de um produto e depois mostre seu novo preço com 5% de desconto


preco = float(input('Digite o preço do produto: R$'))
novo_preco = preco - (preco * 5/100)
print(f'O valor do produto é R${preco:.2f}\nO novo valor do produto é R${novo_preco:.2f}')
