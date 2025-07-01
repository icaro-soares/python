#Crie um programa que disseque uma palavra


obj1 = str(input('Digite algo: '))
print(f'O valor digitado foi {obj1}')
print(f'É uma string? {obj1.isalpha()}')
print(f'É um número? {obj1.isnumeric()}')
print(f'É alfa numérico? {obj1.isalnum()}')
