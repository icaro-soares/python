#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Em que cidade você nasceu? ')).title().strip()
print(f'Você nasceu em {cidade}')
separado = cidade.split()
print(f'A cidade que você nasceu começa com "Santo": {"Santo" in separado[0]}')