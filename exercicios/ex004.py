#Crie um programa que peça ao usuário que digite uma palavra e depois disseque fazendo perguntas sobre seu tipo


palavra = input('Digite algo: ')
print(f'Você digitou: {palavra}')
print(f'O tipo primitivo desse valor é {type(palavra)}')
print(f'Só tem espaços? {palavra.isspace()}')
print(f'É um número? {palavra.isnumeric()}')
print(f'É alfabético? {palavra.isalpha()}')
print(f'É alfanumérico? {palavra.isalnum()}')
print(f'Está em caixa alta (letras maiúsculas)? {palavra.isupper()}')
print(f'Está em caixa baixa (letras minúsculas)? {palavra.islower()}')
print(f'Está capitalizada? {palavra.istitle()}')