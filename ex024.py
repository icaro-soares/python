#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).title().strip()
print(f'O nome da cidade digitada foi {cidade}')
cidade_separado = cidade.split()
print('Santo' in cidade_separado[0])