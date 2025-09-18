#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salário: R$'))
aumento = 15/100 * salario
novo_salario = salario + aumento
print(f'O funcionário que recebia um salário de R${salario:.2f}, vai passar a receber R${novo_salario:.2f}')
