#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('Qual o salário do trabalhador: R$'))
if salário > 1250.00:
    novo_salário = salário + (salário * 0.10)
    print(f'Seu novo salário será de R${novo_salário:.2f}'.replace('.', ','))
else:
    novo_salário = salário + (salário * 0.15)
    print(f'Seu novo salário será de R${novo_salário:.2f}'.replace('.', ','))