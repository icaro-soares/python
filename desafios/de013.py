#Faça um algoritmo que leia o salário de um funcionário e mostre o novo salário com 15% de aumento


salario = float(input('Qual seu salário: R$'))
novo_salario = salario + (salario * 0.15)
print(f'Seu salário é de R${salario:.2f}\nCom aumento ele será de R${novo_salario:.2f}')
