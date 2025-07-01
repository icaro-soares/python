#Crie um programa que leia o salário de um funcionário e depois mostre o novo salario com 15% de aumento


salario = float(input('Digite o seu salário: R$'))
novo_salario = salario + (salario * 15/100)
print(f'Seu salário é R${salario:.2f}\nSeu novo salário com o aumento de 15% será de {novo_salario:.2f}')